import os

def extract_database_version(mykrobe_data):
    try:
        for item in mykrobe_data.values():
            versions_dict = {}
            for software,version in item['version'].items():
                versions_dict[software] = version
            for item in mykrobe_data.values():
                probe_set_list = []
                for probe_sets in item['probe_sets']:
                    probe_set_list.append(os.path.basename(probe_sets).split('.')[0])
                    probe_sets = ','.join(probe_set_list)
                versions_dict['Probe Sets'] = probe_sets
    except:
        print("Failed to extract database version data")
    return versions_dict
