
def extract_subtype_information(input_json):
    try:
        subtype = input_json['subtypeText']
    except:
        print("Subtype data not found")
    return subtype
