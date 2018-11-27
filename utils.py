import collections

def makehash():
    return collections.defaultdict(makehash)

def convert_gene_name(short_name):
    longformatgene = { 'IN' : 'Integrase',
                       'PR' : 'Protease',
                       'RT' : 'Reverse Transcriptase' }
    long_name = longformatgene[short_name]
    return long_name
