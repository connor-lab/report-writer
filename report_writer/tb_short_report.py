from .tb_database import *
from .tb_drug_resistance import *
from .tb_phylogenetics import *
from .utils import *

from datetime import datetime
from prettytable import PrettyTable

def extract_sample_id(mykrobe_data, sample_id=None):
    try:
        if sample_id:
            return sample_id
        else:
            for key,value in mykrobe_data.items():
                sample_id = key
                return sample_id
    except:
        print("Failed to determine sample ID")

def create_sample_table(mykrobe_data, sample_id=None):
    try:
        sample_table_title = "Mycobacterium Genotyping & Resistance Report [Short Format] - PHW Pathogen Genomics Unit"
        sample_id = str(extract_sample_id(mykrobe_data, sample_id))
        date_created = str(datetime.now().strftime('%d-%m-%Y %H:%M'))
        cell_width = round(len(sample_table_title) / 2 + 0.5)
        sample_id_pad = '{content: <{width}}'.format(content=sample_id, width=cell_width)
        date_created_pad = '{content: <{width}}'.format(content=date_created, width=cell_width)
        sample_table = PrettyTable()
        sample_table.field_names = [ 'Sample ID', 'Report Date' ]
        sample_table.add_row([sample_id_pad , date_created_pad ])
        sample_table.title = sample_table_title
        sample_table.align = "l"
    except:
        print("Failed to create sample information table")
    return sample_table


def create_phylogenetics_summary_table(mykrobe_data):
    try:
        phylogenetics_summary = extract_phylogenetics_summary(mykrobe_data)
        phylogenetics_summary_table = PrettyTable()
        phylogenetics_summary_table.field_names = ['Phylo Group', 'Species', 'Lineage', 'Sub Complex']
        phylo_group = phylogenetics_summary['phylo_group']
        species = phylogenetics_summary['species']
        sub_complex = phylogenetics_summary['sub_complex']
        lineage = phylogenetics_summary['lineage']
        phylogenetics_summary_table.add_row([phylo_group, species, lineage, sub_complex])
        phylogenetics_summary_table.title = "Organism Summary"
        phylogenetics_summary_table.align = "l"
    except:
        print("Failed to create phylogenetics summary table")
    return phylogenetics_summary_table

def create_resistance_summary_table(mykrobe_data):
    try:
        drug_resistance_summary = extract_resistance_summary(mykrobe_data)
        resistance_table_list = []
        for line,drug in drug_resistance_summary.items():
            resistance_summary_table = PrettyTable()
            resistance_summary_table.field_names = ['Interpretation', 'Drug', 'Resistance Gene (Mutation)']
            for drug,status in drug.items():
                interpretation = status['status']
                if not status['mutation']:
                    mutation = 'No mutation detected'
                else:
                    mutation = status['mutation']
                resistance_summary_table.title = str( 'Drug Susceptibility [' + line + ' Therapeutics]')
                resistance_summary_table.add_row([interpretation, drug, mutation])
                resistance_summary_table.sortby = "Interpretation"
                resistance_summary_table.align = "l"
            resistance_table_list.append(resistance_summary_table)
    except:
        print("Failed to create resistance summary table")
    return resistance_table_list

def create_database_summary_table(mykrobe_data):
    try:
        version_dict = extract_database_version(mykrobe_data)
        database_summary_table = PrettyTable()
        database_summary_table.field_names = version_dict.keys()
        database_summary_table.add_row(version_dict.values())
        database_summary_table.title = "Software & Database Summary"
    except:
        print("Failed to create software and database summary table")
    return database_summary_table


def write_report_tables(output_prefix, mykrobe_data, sample_id=None):
    report_tables = []
    report_tables.append(create_sample_table(mykrobe_data, sample_id))
    report_tables.append(create_phylogenetics_summary_table(mykrobe_data))
    resistance_tables = create_resistance_summary_table(mykrobe_data)
    for table in sorted(resistance_tables, key=lambda table:table.title):
        report_tables.append(table)
    report_tables.append(create_database_summary_table(mykrobe_data))
    with open(output_prefix + '.report.txt', 'w', newline='\r\n') as file:
        for i in report_tables:
            file.write(i.get_string() + '\r\n')

