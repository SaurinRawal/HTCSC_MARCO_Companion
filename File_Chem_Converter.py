import os
import csv
import encodings

def get_well_number(file_path):
    '''
    Pulls the cocktail number out of the filename and returns it
    as a string
    '''
    return os.path.basename(file_path)[10:14].lstrip('0')
    # leading zeros are removed using lstrip b/c
    # csv file keys will not have leading zeros

def set_up_cockail_csv(cocktail_path):
    '''
    Reads the cocktail list as a csv file and returns a dictionary with
    cocktail number as key and the line as the value
    '''
    chem_dict = {}
    try:
        with open(cocktail_path, encoding='mac_roman') as path:
            csv_reader = csv.reader(path, delimiter = ',', quotechar = '"')
            for line in csv_reader:
                chem_dict[line[0]] = str(line).replace(',', ' ')
        return chem_dict
    except FileNotFoundError as e:
        return e
