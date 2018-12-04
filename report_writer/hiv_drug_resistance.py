from .utils import *

def extract_resistance_summary(input_json):
    try:
        gene_resistance_summary = makehash()
        for i in input_json['drugResistance']:
            for j in i['drugScores']:
                text = j['text']
                drug = j['drug']['displayAbbr']
                drugclass = j['drugClass']['name']
                gene = i['gene']['name']
                if '/' in drug:
                    drug = drug.split('/')[0]
                gene_resistance_summary[gene][drugclass][drug] = text
    except:
        print("Failed to parse drug resistance information")

    return gene_resistance_summary

