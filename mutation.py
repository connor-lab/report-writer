from utils import *

def extract_drug_resistance_mutations(input_json):
    try:
        DRM_dict = makehash()
        for i in input_json['drugResistance']:
            if 'PR' in i['gene']['name']:
                for j in i['drugScores']:
                    for k in j['partialScores']:
                        for l in k['mutations']:
                            for m in l['comments']:
                                mut_type = l['primaryType']
                                mutation = l['text']
                                drugclass = j['drugClass']['name']
                                comment = m['text']
                                DRM_dict[drugclass][mut_type][mutation] = comment
            else:
                for j in i['drugScores']:
                    for k in j['partialScores']:
                        for l in k['mutations']:
                            for m in l['comments']:
                                mutation = l['text']
                                drugclass = j['drugClass']['name']
                                comment = m['text']
                                DRM_dict[drugclass][mutation] = comment
    except:
       print("Failed to extract DRMs")
    return DRM_dict


def extract_all_mutations(input_json):
    try:
        mut_dict = {}
        for i in input_json['alignedGeneSequences']:
            gene = i['gene']['name']
            mut_list = []
            for j in i['mutations']:
                consensus = str(j['consensus'])
                position = str(j['position'])
                mutation = str(j['AAs'])
                mut_string = consensus + position + mutation
                mut_list.append(mut_string)
            mut_dict[gene] = mut_list
    except:
        print("Failed to extract non-DRM mutations")
    return mut_dict

