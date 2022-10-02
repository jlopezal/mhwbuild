import csv
import json
import os

csv_ext = '.csv'
json_ext = '.json'
 
def to_json(csv_base_path, json_base_path):

    data = []
    files = []

    files = get_files(csv_base_path)
    
    for file in files:

        csv_file_path = os.path.join(csv_base_path, file + csv_ext)
        with open(csv_file_path) as csvf:
            csv_reader = csv.DictReader(csvf, delimiter=',')
            for row in csv_reader:
                data.append(row)

        json_file_path = os.path.join(json_base_path, file + json_ext)
        with open(json_file_path, 'w', encoding='utf-8') as jsonf:
            jsonf.write(json.dumps(data, indent=4))

        data.clear()


def get_files(path) -> list:

    filenames = []

    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)):
            filenames.append(filename.split('.')[0])

    return filenames


csvBasePath = r'.\\baseFiles'
jsonBasePath = r'.\\rawFiles'


to_json(csvBasePath, jsonBasePath)