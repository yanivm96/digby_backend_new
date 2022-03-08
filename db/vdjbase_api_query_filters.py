
# API filter definitions, based on the SQLAlchemy class definitions

# This file is created programmatically by db/vdjbase_create_filters.py. DO NOT UPDATE BY HAND. 

from sqlalchemy import func
from db.vdjbase_airr_model import GenoDetection, Sample, Patient, Study, TissuePro, SeqProtocol, DataPro
from db.vdjbase_model import Allele, Gene, AlleleConfidenceReport

sample_info_filters = {    'repertoire_id': {'model': Sample, 'field': Sample.repertoire_id, 'help': 'Identifier for the repertoire object. This identifier should be globally unique so that repertoires from multiple studies can be combined together without conflict. The repertoire_id is used to link other AIRR data to a Repertoire. Specifically, the Rearrangements Schema includes repertoire_id for referencing the specific Repertoire for that Rearrangement.', 'example': '' },
    'repertoire_name': {'model': Sample, 'field': Sample.repertoire_name, 'help': 'Short generic display name for the repertoire', 'example': '' },
    'repertoire_description': {'model': Sample, 'field': Sample.repertoire_description, 'help': 'Generic repertoire description', 'example': '' },
    'sample_processing_id': {'model': Sample, 'field': Sample.sample_processing_id, 'help': 'Identifier for the sample processing object. This field should be unique within the repertoire. This field can be used to uniquely identify the combination of sample, cell processing, nucleic acid processing and sequencing run information for the repertoire.', 'example': '' },
    'sample_id': {'model': Sample, 'field': Sample.sample_id, 'help': 'Sample ID assigned by submitter, unique within study', 'example': 'SUP52415' },
    'sample_type': {'model': Sample, 'field': Sample.sample_type, 'help': 'The way the sample was obtained, e.g. fine-needle aspirate, organ harvest, peripheral venous puncture', 'example': 'Biopsy' },
    'tissue_id': {'model': Sample, 'field': Sample.tissue_id, 'help': 'CURIE of the concept, encoding the ontology and the local ID', 'example': '' },
    'anatomic_site': {'model': Sample, 'field': Sample.anatomic_site, 'help': 'The anatomic location of the tissue, e.g. Inguinal, femur', 'example': 'Iliac crest' },
    'disease_state_sample': {'model': Sample, 'field': Sample.disease_state_sample, 'help': 'Histopathologic evaluation of the sample', 'example': 'Tumor infiltration' },
    'collection_time_point_relative': {'model': Sample, 'field': Sample.collection_time_point_relative, 'help': 'Time point at which sample was taken, relative to `Collection time event`', 'example': '14' },
    'collection_time_point_relative_unit_id': {'model': Sample, 'field': Sample.collection_time_point_relative_unit_id, 'help': 'CURIE of the concept, encoding the ontology and the local ID', 'example': '' },
    'collection_time_point_relative_unit_label': {'model': Sample, 'field': Sample.collection_time_point_relative_unit_label, 'help': 'Label of the concept in the respective ontology', 'example': '' },
    'collection_time_point_reference': {'model': Sample, 'field': Sample.collection_time_point_reference, 'help': 'Event in the study schedule to which `Sample collection time` relates to', 'example': 'Primary vaccination' },
    'biomaterial_provider': {'model': Sample, 'field': Sample.biomaterial_provider, 'help': 'Name and address of the entity providing the sample', 'example': 'Tissues-R-Us, Tampa, FL, USA' },
    'sequencing_run_id': {'model': Sample, 'field': Sample.sequencing_run_id, 'help': 'ID of sequencing run assigned by the sequencing facility', 'example': '160101_M01234' },
    'total_reads_passing_qc_filter': {'model': Sample, 'field': Sample.total_reads_passing_qc_filter, 'help': 'Number of usable reads for analysis', 'example': '10365118' },
    'sequencing_run_date': {'model': Sample, 'field': Sample.sequencing_run_date, 'help': 'Date of sequencing run', 'example': '16/12/2016' },
    'file_type': {'model': Sample, 'field': Sample.file_type, 'help': 'File format for the raw reads or sequences', 'example': '' },
    'filename': {'model': Sample, 'field': Sample.filename, 'help': 'File name for the raw reads or sequences. The first file in paired-read sequencing.', 'example': 'MS10R-NMonson-C7JR9_S1_R1_001.fastq' },
    'read_direction': {'model': Sample, 'field': Sample.read_direction, 'help': 'Read direction for the raw reads or sequences. The first file in paired-read sequencing.', 'example': 'forward' },
    'paired_filename': {'model': Sample, 'field': Sample.paired_filename, 'help': 'File name for the second file in paired-read sequencing', 'example': 'MS10R-NMonson-C7JR9_S1_R2_001.fastq' },
    'paired_read_direction': {'model': Sample, 'field': Sample.paired_read_direction, 'help': 'Read direction for the second file in paired-read sequencing', 'example': 'reverse' },
    'sample_name': {'model': Sample, 'field': Sample.sample_name, 'help': 'Sample name as allocated by VDJbase', 'example': '' },
    'reads': {'model': Sample, 'field': Sample.reads, 'sort': 'numeric', 'help': 'Reads processed by VDJbase pipeline', 'example': '' },
    'genotype': {'model': Sample, 'field': Sample.genotype, 'help': 'Link to genotype report', 'example': '' },
    'igsnper_plot_path': {'model': Sample, 'field': Sample.igsnper_plot_path, 'help': 'Path for igsnper plot', 'example': '' },
    'sample_group': {'model': Sample, 'field': Sample.sample_group, 'help': 'Sample group', 'example': '' },
    'genotype_stats': {'model': Sample, 'field': Sample.genotype_stats, 'help': 'Path to genotype stats file', 'example': '' },
    'genotype_report': {'model': Sample, 'field': Sample.genotype_report, 'help': 'Path to genotype report', 'example': '' },
    'subject_id': {'model': Patient, 'field': Patient.subject_id, 'help': 'Subject ID assigned by submitter, unique within study', 'example': 'SUB856413' },
    'synthetic': {'model': Patient, 'field': Patient.synthetic, 'help': 'TRUE for libraries in which the diversity has been synthetically generated (e.g. phage display)', 'example': '' },
    'species_id': {'model': Patient, 'field': Patient.species_id, 'help': 'CURIE of the concept, encoding the ontology and the local ID', 'example': '' },
    'species_label': {'model': Patient, 'field': Patient.species_label, 'help': 'Label of the concept in the respective ontology', 'example': '' },
    'organism_id': {'model': Patient, 'field': Patient.organism_id, 'help': 'CURIE of the concept, encoding the ontology and the local ID', 'example': '' },
    'organism_label': {'model': Patient, 'field': Patient.organism_label, 'help': 'Label of the concept in the respective ontology', 'example': '' },
    'sex': {'model': Patient, 'field': Patient.sex, 'help': 'Biological sex of subject', 'example': 'female' },
    'age_min': {'model': Patient, 'field': Patient.age_min, 'help': 'Specific age or lower boundary of age range.', 'example': '60' },
    'age_max': {'model': Patient, 'field': Patient.age_max, 'help': 'Upper boundary of age range or equal to age_min for specific age. This field should only be null if age_min is null.', 'example': '80' },
    'age_unit_id': {'model': Patient, 'field': Patient.age_unit_id, 'help': 'CURIE of the concept, encoding the ontology and the local ID', 'example': '' },
    'age_unit_label': {'model': Patient, 'field': Patient.age_unit_label, 'help': 'Label of the concept in the respective ontology', 'example': '' },
    'age_event': {'model': Patient, 'field': Patient.age_event, 'help': 'Event in the study schedule to which `Age` refers. For NCBI BioSample this MUST be `sampling`. For other implementations submitters need to be aware that there is currently no mechanism to encode to potential delta between `Age event` and `Sample collection time`, hence the chosen events should be in temporal proximity.', 'example': 'enrollment' },
    'age': {'model': Patient, 'field': Patient.age, 'help': '', 'example': '' },
    'ancestry_population': {'model': Patient, 'field': Patient.ancestry_population, 'help': 'Broad geographic origin of ancestry (continent)', 'example': 'list of continents, mixed or unknown' },
    'ethnicity': {'model': Patient, 'field': Patient.ethnicity, 'help': 'Ethnic group of subject (defined as cultural/language-based membership)', 'example': 'English, Kurds, Manchu, Yakuts (and other fields from Wikipedia)' },
    'race': {'model': Patient, 'field': Patient.race, 'help': 'Racial group of subject (as defined by NIH)', 'example': 'White, American Indian or Alaska Native, Black, Asian, Native Hawaiian or Other Pacific Islander, Other' },
    'strain_name': {'model': Patient, 'field': Patient.strain_name, 'help': 'Non-human designation of the strain or breed of animal used', 'example': 'C57BL/6J' },
    'linked_subjects': {'model': Patient, 'field': Patient.linked_subjects, 'help': 'Subject ID to which `Relation type` refers', 'example': 'SUB1355648' },
    'link_type': {'model': Patient, 'field': Patient.link_type, 'help': 'Relation between subject and `linked_subjects`, can be genetic or environmental (e.g.exposure)', 'example': 'father, daughter, household' },
    'study_group_description': {'model': Patient, 'field': Patient.study_group_description, 'help': 'Designation of study arm to which the subject is assigned to', 'example': 'control' },
    'disease_diagnosis_id': {'model': Patient, 'field': Patient.disease_diagnosis_id, 'help': 'CURIE of the concept, encoding the ontology and the local ID', 'example': '' },
    'disease_diagnosis_label': {'model': Patient, 'field': Patient.disease_diagnosis_label, 'help': 'Label of the concept in the respective ontology', 'example': '' },
    'disease_length': {'model': Patient, 'field': Patient.disease_length, 'help': 'Time duration between initial diagnosis and current intervention', 'example': '23 months' },
    'disease_stage': {'model': Patient, 'field': Patient.disease_stage, 'help': 'Stage of disease at current intervention', 'example': 'Stage II' },
    'prior_therapies': {'model': Patient, 'field': Patient.prior_therapies, 'help': 'List of all relevant previous therapies applied to subject for treatment of `Diagnosis`', 'example': 'melphalan/prednisone' },
    'immunogen': {'model': Patient, 'field': Patient.immunogen, 'help': 'Antigen, vaccine or drug applied to subject at this intervention', 'example': 'bortezomib' },
    'intervention': {'model': Patient, 'field': Patient.intervention, 'help': 'Description of intervention', 'example': 'systemic chemotherapy, 6 cycles, 1.25 mg/m2' },
    'medical_history': {'model': Patient, 'field': Patient.medical_history, 'help': 'Medical history of subject that is relevant to assess the course of disease and/or treatment', 'example': 'MGUS, first diagnosed 5 years prior' },
    'receptor_genotype_set_id': {'model': Patient, 'field': Patient.receptor_genotype_set_id, 'help': 'A unique identifier for this Receptor Genotype Set.', 'example': '' },
    'mhc_genotype_set_id': {'model': Patient, 'field': Patient.mhc_genotype_set_id, 'help': 'A unique identifier for this MHC Genotype Set.', 'example': '' },
    'mhc_genotype_id': {'model': Patient, 'field': Patient.mhc_genotype_id, 'help': 'A unique identifier for this MHC Genotype, assumed to be unique in the context of the study.', 'example': '' },
    'genotype_class': {'model': Patient, 'field': Patient.genotype_class, 'help': '', 'example': 'MHC' },
    'gene_symbol': {'model': Patient, 'field': Patient.gene_symbol, 'help': 'The accepted name for this gene', 'example': '' },
    'germline_set_ref': {'model': Patient, 'field': Patient.germline_set_ref, 'help': 'Repository and list from which it was taken (issuer/name/version)', 'example': '' },
    'genotype_process': {'model': Patient, 'field': Patient.genotype_process, 'help': 'Information on how the genotype was acquired. Controlled vocabulary.', 'example': 'repertoire_sequencing' },
    'patient_name': {'model': Patient, 'field': Patient.patient_name, 'help': 'Subject name as allocated by VDJbase', 'example': '' },
    'study_id': {'model': Study, 'field': Study.study_id, 'help': 'Unique ID assigned by study registry', 'example': 'PRJNA001' },
    'study_title': {'model': Study, 'field': Study.study_title, 'help': 'Descriptive study title', 'example': 'Effects of sun light exposure of the Treg repertoire' },
    'study_type_id': {'model': Study, 'field': Study.study_type_id, 'help': 'CURIE of the concept, encoding the ontology and the local ID', 'example': '' },
    'study_type_label': {'model': Study, 'field': Study.study_type_label, 'help': 'Label of the concept in the respective ontology', 'example': '' },
    'study_description': {'model': Study, 'field': Study.study_description, 'help': 'Generic study description', 'example': 'Longer description' },
    'inclusion_exclusion_criteria': {'model': Study, 'field': Study.inclusion_exclusion_criteria, 'help': 'List of criteria for inclusion/exclusion for the study', 'example': 'Include: Clinical P. falciparum infection; Exclude: Seropositive for HIV' },
    'grants': {'model': Study, 'field': Study.grants, 'help': 'Funding agencies and grant numbers', 'example': 'NIH, award number R01GM987654' },
    'study_contact': {'model': Study, 'field': Study.study_contact, 'help': 'Full contact information of the contact persons for this study This should include an e-mail address and a persistent identifier such as an ORCID ID.', 'example': 'Dr. P. Stibbons, p.stibbons@unseenu.edu, https://orcid.org/0000-0002-1825-0097' },
    'collected_by': {'model': Study, 'field': Study.collected_by, 'help': 'Full contact information of the data collector, i.e. the person who is legally responsible for data collection and release. This should include an e-mail address.', 'example': 'Dr. P. Stibbons, p.stibbons@unseenu.edu' },
    'lab_name': {'model': Study, 'field': Study.lab_name, 'help': 'Department of data collector', 'example': 'Department for Planar Immunology' },
    'lab_address': {'model': Study, 'field': Study.lab_address, 'help': 'Institution and institutional address of data collector', 'example': 'School of Medicine, Unseen University, Ankh-Morpork, Disk World' },
    'submitted_by': {'model': Study, 'field': Study.submitted_by, 'help': 'Full contact information of the data depositor, i.e. the person submitting the data to a repository. This is supposed to be a short-lived and technical role until the submission is relased.', 'example': 'Adrian Turnipseed, a.turnipseed@unseenu.edu' },
    'pub_ids': {'model': Study, 'field': Study.pub_ids, 'help': 'Publications describing the rationale and/or outcome of the study', 'example': 'PMID:85642' },
    'keywords_study': {'model': Study, 'field': Study.keywords_study, 'help': '', 'example': '' },
    'adc_publish_date': {'model': Study, 'field': Study.adc_publish_date, 'help': 'Date the study was first published in the AIRR Data Commons.', 'example': '02/02/2021' },
    'adc_update_date': {'model': Study, 'field': Study.adc_update_date, 'help': 'Date the study data was updated in the AIRR Data Commons.', 'example': '02/02/2021' },
    'num_subjects': {'model': Study, 'field': Study.num_subjects, 'sort': 'numeric', 'help': 'Number of subjects in the study', 'example': '' },
    'num_samples': {'model': Study, 'field': Study.num_samples, 'sort': 'numeric', 'help': 'Number of samples in the study', 'example': '' },
    'accession_reference': {'model': Study, 'field': Study.accession_reference, 'help': 'URL of the study in the registry', 'example': '' },
    'study_name': {'model': Study, 'field': Study.study_name, 'help': 'Study name', 'example': '' },
    'tissue_label': {'model': TissuePro, 'field': TissuePro.tissue_label, 'help': 'Label of the concept in the respective ontology', 'example': '' },
    'tissue_processing': {'model': TissuePro, 'field': TissuePro.tissue_processing, 'help': 'Enzymatic digestion and/or physical methods used to isolate cells from sample', 'example': 'Collagenase A/Dnase I digested, followed by Percoll gradient' },
    'cell_subset_id': {'model': TissuePro, 'field': TissuePro.cell_subset_id, 'help': 'CURIE of the concept, encoding the ontology and the local ID', 'example': '' },
    'cell_subset_label': {'model': TissuePro, 'field': TissuePro.cell_subset_label, 'help': 'Label of the concept in the respective ontology', 'example': '' },
    'cell_phenotype': {'model': TissuePro, 'field': TissuePro.cell_phenotype, 'help': 'List of cellular markers and their expression levels used to isolate the cell population', 'example': 'CD19+ CD38+ CD27+ IgM- IgD-' },
    'cell_species_id': {'model': TissuePro, 'field': TissuePro.cell_species_id, 'help': 'CURIE of the concept, encoding the ontology and the local ID', 'example': '' },
    'cell_species_label': {'model': TissuePro, 'field': TissuePro.cell_species_label, 'help': 'Label of the concept in the respective ontology', 'example': '' },
    'single_cell': {'model': TissuePro, 'field': TissuePro.single_cell, 'help': 'TRUE if single cells were isolated into separate compartments', 'example': '' },
    'cell_number': {'model': TissuePro, 'field': TissuePro.cell_number, 'help': 'Total number of cells that went into the experiment', 'example': '1000000' },
    'cells_per_reaction': {'model': TissuePro, 'field': TissuePro.cells_per_reaction, 'help': 'Number of cells for each biological replicate', 'example': '50000' },
    'cell_storage': {'model': TissuePro, 'field': TissuePro.cell_storage, 'help': 'TRUE if cells were cryo-preserved between isolation and further processing', 'example': 'TRUE' },
    'cell_quality': {'model': TissuePro, 'field': TissuePro.cell_quality, 'help': 'Relative amount of viable cells after preparation and (if applicable) thawing', 'example': '90% viability as determined by 7-AAD' },
    'cell_isolation': {'model': TissuePro, 'field': TissuePro.cell_isolation, 'help': 'Description of the procedure used for marker-based isolation or enrich cells', 'example': 'Cells were stained with fluorochrome labeled antibodies and then sorted on a FlowMerlin (CE) cytometer.' },
    'cell_processing_protocol': {'model': TissuePro, 'field': TissuePro.cell_processing_protocol, 'help': 'Description of the methods applied to the sample including cell preparation/ isolation/enrichment and nucleic acid extraction. This should closely mirror the Materials and methods section in the manuscript.', 'example': 'Stimulated wih anti-CD3/anti-CD28' },
    'sub_cell_type': {'model': TissuePro, 'field': TissuePro.sub_cell_type, 'help': 'Sub cell type', 'example': '' },
    'template_class': {'model': SeqProtocol, 'field': SeqProtocol.template_class, 'help': 'The class of nucleic acid that was used as primary starting material for the following procedures', 'example': 'RNA' },
    'template_quality': {'model': SeqProtocol, 'field': SeqProtocol.template_quality, 'help': 'Description and results of the quality control performed on the template material', 'example': 'RIN 9.2' },
    'template_amount': {'model': SeqProtocol, 'field': SeqProtocol.template_amount, 'help': 'Amount of template that went into the process', 'example': '1000' },
    'template_amount_unit_id': {'model': SeqProtocol, 'field': SeqProtocol.template_amount_unit_id, 'help': 'CURIE of the concept, encoding the ontology and the local ID', 'example': '' },
    'template_amount_unit_label': {'model': SeqProtocol, 'field': SeqProtocol.template_amount_unit_label, 'help': 'Label of the concept in the respective ontology', 'example': '' },
    'library_generation_method': {'model': SeqProtocol, 'field': SeqProtocol.library_generation_method, 'help': 'Generic type of library generation', 'example': 'RT(oligo-dT)+TS(UMI)+PCR' },
    'library_generation_protocol': {'model': SeqProtocol, 'field': SeqProtocol.library_generation_protocol, 'help': 'Description of processes applied to substrate to obtain a library that is ready for sequencing', 'example': 'cDNA was generated using' },
    'library_generation_kit_version': {'model': SeqProtocol, 'field': SeqProtocol.library_generation_kit_version, 'help': 'When using a library generation protocol from a commercial provider, provide the protocol version number', 'example': 'v2.1 (2016-09-15)' },
    'pcr_target_locus': {'model': SeqProtocol, 'field': SeqProtocol.pcr_target_locus, 'help': 'Designation of the target locus. Note that this field uses a controlled vocubulary that is meant to provide a generic classification of the locus, not necessarily the correct designation according to a specific nomenclature.', 'example': 'IGK' },
    'forward_pcr_primer_target_location': {'model': SeqProtocol, 'field': SeqProtocol.forward_pcr_primer_target_location, 'help': 'Position of the most distal nucleotide templated by the forward primer or primer mix', 'example': 'IGHV, +23' },
    'reverse_pcr_primer_target_location': {'model': SeqProtocol, 'field': SeqProtocol.reverse_pcr_primer_target_location, 'help': 'Position of the most proximal nucleotide templated by the reverse primer or primer mix', 'example': 'IGHG, +57' },
    'complete_sequences': {'model': SeqProtocol, 'field': SeqProtocol.complete_sequences, 'help': 'To be considered `complete`, the procedure used for library construction MUST generate sequences that 1) include the first V gene codon that encodes the mature polypeptide chain (i.e. after the leader sequence) and 2) include the last complete codon of the J gene (i.e. 1 bp 5" of the J->C splice site) and 3) provide sequence information for all positions between 1) and 2). To be considered `complete & untemplated`, the sections of the sequences defined in points 1) to 3) of the previous sentence MUST be untemplated, i.e. MUST NOT overlap with the primers used in library preparation. `mixed` should only be used if the procedure used for library construction will likely produce multiple categories of sequences in the given experiment. It SHOULD NOT be used as a replacement of a NULL value.', 'example': 'partial' },
    'physical_linkage': {'model': SeqProtocol, 'field': SeqProtocol.physical_linkage, 'help': 'In case an experimental setup is used that physically links nucleic acids derived from distinct `Rearrangements` before library preparation, this field describes the mode of that linkage. All `hetero_*` terms indicate that in case of paired-read sequencing, the two reads should be expected to map to distinct IG/TR loci. `*_head-head` refers to techniques that link the 5" ends of transcripts in a single-cell context. `*_tail-head` refers to techniques that link the 3" end of one transcript to the 5" end of another one in a single-cell context. This term does not provide any information whether a continuous reading-frame between the two is generated. `*_prelinked` refers to constructs in which the linkage was already present on the DNA level (e.g. scFv).', 'example': 'hetero_head-head' },
    'sequencing_platform': {'model': SeqProtocol, 'field': SeqProtocol.sequencing_platform, 'help': 'Designation of sequencing instrument used', 'example': 'Alumina LoSeq 1000' },
    'sequencing_facility': {'model': SeqProtocol, 'field': SeqProtocol.sequencing_facility, 'help': 'Name and address of sequencing facility', 'example': 'Seqs-R-Us, Vancouver, BC, Canada' },
    'sequencing_kit': {'model': SeqProtocol, 'field': SeqProtocol.sequencing_kit, 'help': 'Name, manufacturer, order and lot numbers of sequencing kit', 'example': 'FullSeq 600, Alumina, #M123456C0, 789G1HK' },
    'read_length': {'model': SeqProtocol, 'field': SeqProtocol.read_length, 'help': 'Read length in bases for the first file in paired-read sequencing', 'example': '300' },
    'paired_read_length': {'model': SeqProtocol, 'field': SeqProtocol.paired_read_length, 'help': 'Read length in bases for the second file in paired-read sequencing', 'example': '300' },
    'data_processing_id': {'model': DataPro, 'field': DataPro.data_processing_id, 'help': 'Identifier for the data processing object.', 'example': '' },
    'primary_annotation': {'model': DataPro, 'field': DataPro.primary_annotation, 'help': 'If true, indicates this is the primary or default data processing for the repertoire and its rearrangements. If false, indicates this is a secondary or additional data processing.', 'example': '' },
    'software_versions': {'model': DataPro, 'field': DataPro.software_versions, 'help': 'Version number and / or date, include company pipelines', 'example': 'IgBLAST 1.6' },
    'paired_reads_assembly': {'model': DataPro, 'field': DataPro.paired_reads_assembly, 'help': 'How paired end reads were assembled into a single receptor sequence', 'example': 'PandaSeq (minimal overlap 50, threshold 0.8)' },
    'quality_thresholds': {'model': DataPro, 'field': DataPro.quality_thresholds, 'help': 'How sequences were removed from (4) based on base quality scores', 'example': 'Average Phred score >=20' },
    'primer_match_cutoffs': {'model': DataPro, 'field': DataPro.primer_match_cutoffs, 'help': 'How primers were identified in the sequences, were they removed/masked/etc?', 'example': 'Hamming distance <= 2' },
    'collapsing_method': {'model': DataPro, 'field': DataPro.collapsing_method, 'help': 'The method used for combining multiple sequences from (4) into a single sequence in (5)', 'example': 'MUSCLE 3.8.31' },
    'data_processing_protocols': {'model': DataPro, 'field': DataPro.data_processing_protocols, 'help': 'General description of how QC is performed', 'example': 'Data was processed using [...]' },
    'data_processing_files': {'model': DataPro, 'field': DataPro.data_processing_files, 'help': '', 'example': '' },
    'germline_database': {'model': DataPro, 'field': DataPro.germline_database, 'help': 'Source of germline V(D)J genes with version number or date accessed.', 'example': 'ENSEMBL, Homo sapiens build 90, 2017-10-01' },
    'analysis_provenance_id': {'model': DataPro, 'field': DataPro.analysis_provenance_id, 'help': 'Identifier for machine-readable PROV model of analysis provenance', 'example': '' },

    'allele': {'model': None, 'field': None},

    'haplotypes': {'model': None, 'field': None},
    'genotypes': {'model': None, 'field': None},

    'dataset': {'model': None, 'field': None, 'fieldname': 'dataset', 'no_uniques': True},
}

sequence_filters = {    'name': {'model': Allele, 'field': Allele.name, 'help': '', 'example': '' },
    'pipeline_name': {'model': Allele, 'field': Allele.pipeline_name, 'help': '', 'example': '' },
    'seq': {'model': Allele, 'field': Allele.seq, 'help': '', 'example': '' },
    'seq_len': {'model': Allele, 'field': Allele.seq_len, 'help': '', 'example': '' },
    'similar': {'model': Allele, 'field': Allele.similar, 'help': '', 'example': '' },
    'appears': {'model': Allele, 'field': Allele.appears, 'sort': 'numeric', 'help': '', 'example': '' },
    'is_single_allele': {'model': Allele, 'field': Allele.is_single_allele, 'help': '', 'example': '' },
    'low_confidence': {'model': Allele, 'field': Allele.low_confidence, 'help': '', 'example': '' },
    'novel': {'model': Allele, 'field': Allele.novel, 'help': '', 'example': '' },
    'max_kdiff': {'model': Allele, 'field': Allele.max_kdiff, 'help': '', 'example': '' },
    'gene_name': {'model': Gene, 'field': Gene.name.label('gene_name'), 'fieldname': 'name', 'help': '', 'example': '' },
    'type': {'model': Gene, 'field': Gene.type, 'help': '', 'example': '' },
    'family': {'model': Gene, 'field': Gene.family, 'help': '', 'example': '' },
    'species': {'model': Gene, 'field': Gene.species, 'help': '', 'example': '' },
    'igsnper_plot_path': {'model': Gene, 'field': Gene.igsnper_plot_path, 'help': '', 'example': '' },

    'notes': {'model': Allele, 'field': func.group_concat(AlleleConfidenceReport.notes, '\n').label('notes')},
    'notes_count': {'model': Allele, 'field': func.count(AlleleConfidenceReport.id).label('notes_count'), 'sort': 'numeric'},

    'sample_id': {'model': None, 'field': None, 'fieldname': 'sample_id'},
    'dataset': {'model': None, 'field': None, 'fieldname': 'dataset', 'no_uniques': True},    
}

