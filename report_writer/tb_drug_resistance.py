from .utils import *

def extract_resistance_summary(mykrobe_data):
    try:
        for key,value in mykrobe_data.items():
            susceptibility_dict = makehash()
            for drug,value in value['susceptibility'].items():
                line = mykrobe_susceptibility_line(drug)
                status = convert_mykrobe_susceptibility(value['predict'])
                susceptibility_dict[line][drug]['status'] = status
                for key,value in value.items():
                    if 'called_by' in key:
                        for key,value in value.items():
                            gene = key.split('_')[0]
                            mutation = key.split('-')[1]
                            mutation_string = gene + ' (' + mutation + ')'
                            susceptibility_dict[line][drug]['mutation'] = mutation_string
    except:
        print("Failed to extract drug susceptibility data")

    return susceptibility_dict

