import collections
import os

def makehash():
    return collections.defaultdict(makehash)

def create_output_directory(directory):
    try:
        if not os.path.exists(directory):
            os.mkdir(directory)
    except:
        print("Failed to create output directory")

def create_output_prefix(directory, prefix):
    try:
        output_prefix = os.path.join(directory, prefix)
    except:
        print("Couldn't create output prefix")
    return output_prefix

def convert_gene_name(short_name):
    longformatgene = { 'IN' : 'Integrase',
                       'PR' : 'Protease',
                       'RT' : 'Reverse Transcriptase' }
    long_name = longformatgene[short_name]
    return long_name
