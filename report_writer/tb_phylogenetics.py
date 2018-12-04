from .utils import *

def extract_phylogenetics_summary(mykrobe_data):
    try:
        for item in mykrobe_data.values():
            phylogenetics_dict = {}
            for level,value in item['phylogenetics'].items():
                for interpretation,value in value.items():
                    interpretation = interpretation.replace('_', ' ')
                    phylogenetics_dict[level] = interpretation
    except:
        print("Failed to extract phylogenetic information")
    return phylogenetics_dict
