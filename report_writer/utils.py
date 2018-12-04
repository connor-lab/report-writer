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

def convert_mykrobe_susceptibility(short_susceptibility):
    longformatsusceptibility = { 'S' : 'Susceptible',
                                 'I' : 'Intermediate',
                                 'R' : 'Resistant' }
    long_susceptibility = longformatsusceptibility[short_susceptibility]
    return long_susceptibility

def mykrobe_susceptibility_line(drug):
    fist_line_drugs = [ 'Isoniazid', 'Ethambutol', 'Pyrazinamide', 'Rifampicin' ]
    second_line_drugs = ['Streptomycin', 'Kanamycin', 'Capreomycin', 'Amikacin', 'Quinolones']
    if drug in fist_line_drugs:
        drug_line = 'First Line'
    elif drug in second_line_drugs:
        drug_line = 'Second Line'
    else:
        drug_line = 'N/A'
    return drug_line
