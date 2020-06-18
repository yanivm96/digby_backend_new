from lxml import html
import requests
from db.shared import delete_dependencies

from app import db
from db.feature_db import Species, RefSeq, Feature, Sequence, Sample, SampleSequence, Study

type = {
    "5'UTR": 'five_prime_UTR',
    'L-PART1': 'CDS',
    'V-INTRON': 'intron',
    'L-PART2': 'CDS',
    'V-REGION': 'CDS',
    'D-REGION': 'CDS',
    'J-REGION': 'CDS',
    "3'UTR": 'three_prime_UTR',
}

def update():
#    delete_dependencies('Atlantic Salmon')
#    return ""

    ctg = 'GU129139'
    ret = "Importing Salmon IGHV from %s\n" % ctg

    page = requests.get('http://www.imgt.org/ligmdb/view?id=GU129139')
    tree = html.fromstring(page.content)

    seq_text = tree.xpath('//div[@class="sequence"]/pre')[0]

    sequence = ''
    for row in seq_text.text.split('\n'):
        if len(row) > 75:
            sequence += row[1:70].replace(' ', '')

    sp = db.session.query(Species).filter_by(name='Atlantic Salmon').one_or_none()

    if not sp:
        sp = Species(name='Atlantic Salmon')
        db.session.add(sp)

    study = Study(name='Salmon',
                  institute='Virologie et Immunologie Moléculaires (VIM), Institut National de la Recherche Agronomique (INRA), Université Paris-Saclay, Jouy-en-Josas, France',
                  researcher='Pierre Boudinot',
                  reference='https://www.frontiersin.org/articles/10.3389/fimmu.2019.02541/full',
                  contact='smaga@uvigo.es',
                  accession_id='GU129139',
                  accession_reference='https://www.ncbi.nlm.nih.gov/nuccore/GU129139')
    db.session.add(study)
    db.session.commit()

    ref_seq = RefSeq(name=ctg, locus='IGH', species=sp, sequence=sequence, length=len(sequence))
    db.session.add(ref_seq)

    sample = db.session.query(Sample).filter_by(name='GU129139').one_or_none()

    if not sample:
        sample = Sample(name='GU129139', type='Reference', date='2020-06-10', study=study, species_id=sp.id, ref_seq_id=ref_seq.id)
        db.session.add(sample)

    features = tree.xpath('//div[@class="features"]/table')[0]
    rows = iter(features)

    state = None
    name = None
    gene_range = None
    strand = None
    parent_id = 0

    for row in rows:
        values = [col.text for col in row]

        if len(values) < 3:
            continue

        def get_range(s):
            gene_range = s.split('..')
            if len(gene_range) < 2:
                print('Invalid gene range found: %s' % s)
                return (('1', '1'), '+')

            for i in (0, 1):
                gene_range[i] = gene_range[i].replace('>', '').replace('<', '')

            strand = '+'

            if 'complement(' in gene_range[0]:
                gene_range[0] = gene_range[0].replace('complement(', '')
                gene_range[1] = gene_range[1].replace(')', '')
                strand = '-'

            try:
                if int(gene_range[1]) - int(gene_range[0]) > 10000000 or int(gene_range[0]) > int(gene_range[1]):
                    print('Invalid gene range found: %s' % s)
                    return (('1', '1'), '+')
            except:
                print('Invalid gene range found: %s' % s)
                return (('1', '1'), '+')

            return (gene_range, strand)

        if not state and values[0] in ['V-GENE', 'D-GENE', 'J-GENE']:
            gene_range, strand = get_range(values[2])
            state = values[0]

        elif state and not name:
            if values[1] == 'IMGT_allele':
                name = values[2].split('*')[0]
                parent_id += 1
                fp = Feature(
                    name=name,
                    feature='gene',
                    start=gene_range[0],
                    end=gene_range[1],
                    strand=strand,
                    attribute='Name=%s;ID=%s' % (name, parent_id),
                    feature_id=parent_id,
                )
                ref_seq.features.append(fp)
                parent_id += 1

                f = Feature(
                    name=name,
                    feature='mRNA',
                    start=gene_range[0],
                    end=gene_range[1],
                    strand=strand,
                    attribute='Name=%s;ID=%s;Parent=%s' % (name, parent_id, parent_id-1),
                    feature_id=parent_id,
                    parent_id=parent_id-1,
                )
                ref_seq.features.append(f)

        elif state and name:
            if (state == 'V-GENE' and values[0] in ["5'UTR", 'L-PART1', 'V-INTRON', 'L-PART2', 'V-REGION', "3'UTR"]) \
                    or (state == 'D-GENE' and values[0] in ["5'UTR", 'D-REGION', "3'UTR"]) \
                    or (state == 'J-GENE' and values[0] in ["5'UTR", 'D-REGION', "3'UTR"]):
                gene_range, strand = get_range(values[2])

                f = Feature(
                    name=name + '_' + values[0],
                    feature=type[values[0]],
                    start=gene_range[0],
                    end=gene_range[1],
                    strand=strand,
                    attribute='Name=%s;Parent=%s' % (name + '_' + values[0], parent_id),
                    parent_id=parent_id,
                )

                ref_seq.features.append(f)

                s = Sequence(
                    name=name + '_' + values[0],
                    imgt_name=name,
                    type=values[0],
                    sequence=ref_seq.sequence[int(gene_range[0])-1:int(gene_range[1])],
                    species=sp,
                    novel=False,
                )

                s.features.append(f)
                SampleSequence(sample=sample, sequence=s, chromosome='h1,h2', chromo_count=2)

        if state and name and values[0] == "3'UTR":
            state = None
            name = None

    db.session.commit()
    return ret
