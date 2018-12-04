from datetime import date

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

