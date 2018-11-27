from utils import *

from datetime import date
from prettytable import PrettyTable

def extract_subtype_information(input_json):
    try:
        subtype = input_json['subtypeText']
    except:
        print("Subtype data not found")
    return subtype


def create_subtype_table(sample_id, input_json):
    try:
        subtype = extract_subtype_information(input_json)
        subtype_table = PrettyTable()
        subtype_table.field_names = ['PHW Episode Number', 'Subtype (Divergence from subtype reference)']
        subtype_table.add_row([sample_id , subtype])
        subtype_table.title = "HIV Resistance Genotyping Report [Short format] - PHW Pathogen Genomics Unit" 
        subtype_table.align = "l"
    except:
        print("Failed to create subtype table")
    return subtype_table



def extract_lengths(input_json):
    try:
        gene_lengths = {}
        for gene in input_json['alignedGeneSequences']:
            genename = gene['gene']['name']
            gene_lengths[genename] = { 'firstAA' : gene['firstAA'],
                                        'lastAA' : gene['lastAA'],
                                        'length' : gene['gene']['length'] }
    except:
        print('Gene length data not found')
    return gene_lengths


def extract_resistance_summary(input_json):
    try:
        gene_resistance_summary = makehash()
        for i in input_json['drugResistance']:
            for j in i['drugScores']:
                text = j['text']
                drug = j['drug']['name']
                drugclass = j['drugClass']['name']
                gene = i['gene']['name']
                gene_resistance_summary[gene][drugclass][drug] = text
    except:
        print("Failed to parse drug resistance information")

    return gene_resistance_summary

def create_resistance_summary_table(input_json):
    try:
        sequence_lengths = extract_lengths(input_json)
        drug_resistance_summary = extract_resistance_summary(input_json)
        resistance_table_list = []
        for gene,drugclass in drug_resistance_summary.items():
            resistance_summary_table = PrettyTable()
            resistance_summary_table.field_names = ['Drug Class', 'Drug', 'Status']
            for drugclass,drug in drugclass.items():
                for drug,status in drug.items():
                    resistance_summary_table.add_row([drugclass, drug, status])

            long_name = convert_gene_name(gene)
            firstAA = str(sequence_lengths[gene]['firstAA'])
            lastAA = str(sequence_lengths[gene]['lastAA'])
            genelength = str(sequence_lengths[gene]['length'])
            table_title = long_name + " [Codons analysed " + firstAA + "-" + lastAA + "/" + genelength + "]"
            resistance_summary_table.title = table_title
            resistance_summary_table.align = "l"

            resistance_table_list.append(resistance_summary_table)
    except:
        print('Failed to make resistance summary tables')
    return resistance_table_list

def extract_database_version(input_json):
    try:
        version_dict = {}
        for i in input_json['drugResistance']:
            version = i['version']['text']
            publish_date = i['version']['publishDate']
            access_date = str(date.today())
        version_dict.update({'version' : version, 'publishDate' : publish_date, 'accessDate' : access_date })
    except:
        print("Failed to make database version table")
    return version_dict

def create_version_table(input_json):
    try:
        database_information = extract_database_version(input_json)
        database_information_table = PrettyTable()
        database_information_table.title = 'Stanford HIVdb Information'
        database_information_table.align = 'l'
        database_information_table.field_names = ['HIVdb Version', 'HIVdb Date', 'Access Date']
        database_information_table.add_row([database_information['version'], database_information['publishDate'], database_information['accessDate']])
    except:
        print("Failed to create database information table")
    return database_information_table

def write_report_tables(output_prefix, sample_id, input_json):
#    try:
        report_tables = []
        report_tables.append(create_subtype_table(sample_id, input_json))
        for table in create_resistance_summary_table(input_json):
            report_tables.append(table)
        report_tables.append(create_version_table(input_json))
        with open(output_prefix + '.report.txt', 'w', newline='\r\n') as file:
                for i in report_tables:
                    file.write(i.get_string() + '\r\n')
