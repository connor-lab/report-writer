from utils import *

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

def make_sequence_object_list(seq_dict):
    try:
        seq_list = []
        for gene,sequence in seq_dict.items():
            long_name = convert_gene_name(gene)
            record = SeqRecord(Seq(sequence), id=gene, description="[" + long_name + "]")
            seq_list.append(record)
    except:
        print("Couldn't make sequence object")
    return seq_list


def extract_gene_sequences(input_json):
    try:
        nucleic_acid = {}
        for gene in input_json['alignedGeneSequences']:
            genename = gene['gene']['name']
            nucleic_acid[genename] = gene['alignedNAs']
        nucleic_acid = make_sequence_object_list(nucleic_acid)
    except:
        print("Nucleic acid alignment not found")
    return nucleic_acid


def extract_aa_sequences(input_json):
    try:
        amino_acid = {}
        for gene in input_json['alignedGeneSequences']:
            genename = gene['gene']['name']
            amino_acid[genename] = gene['alignedAAs']
        amino_acid = make_sequence_object_list(amino_acid)
    except:
        print("Amino acid alignment not found")
    return amino_acid


def write_sequences_to_file(output_prefix, SampleID, input_json):
    aa_seqs = extract_aa_sequences(input_json)
    nt_seqs = extract_gene_sequences(input_json)
    with open(output_prefix + ".faa", "w") as output_handle:
        for record in aa_seqs:
            record.id = SampleID + "|" + record.id
            SeqIO.write(record, output_handle, "fasta")
    with open(output_prefix + ".fna", "w") as output_handle:
        for record in nt_seqs:
            record.id = SampleID + "|" + record.id
            SeqIO.write(record, output_handle, "fasta")
