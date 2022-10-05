import csv
import json
import os
from site import abs_paths

from utils import base_path, data_folder_dict
from utils import checkMigrationFolderStruct, createMigrationFolderStruct

csv_ext = '.csv'
json_ext = '.json'

def to_json(csv_base_path, json_base_path):

    data = []
    files = []

    files = get_files(csv_base_path)
    
    for file in files:

        csv_file_path = os.path.join(csv_base_path, (file + csv_ext))
        with open(csv_file_path, 'r', encoding='utf-8-sig') as csvf:
            csv_reader = csv.DictReader(csvf, delimiter=',')
            for row in csv_reader:
                data.append(row)

        json_file_path = os.path.join(json_base_path, (file + json_ext))
        with open(json_file_path, 'w', encoding='utf-8') as jsonf:
            jsonf.write(json.dumps(data, indent=4))

        data.clear()


def get_files(path) -> list:

    out_paths = []

    elements = os.listdir(path)
    for i, e in enumerate(elements):
        elements[i] = os.path.abspath(os.path.join(path, e))
    for e in elements:
        if os.path.isfile(e):
            out_paths.append(os.path.abspath(e))
        # if os.path.isdir(e):
        #     elements.append(os.path.abspath(e))

    # Normalize output paths
    delimiter = path
    for i, e in enumerate(out_paths):
        out_paths[i] = e.split(delimiter.replace(".", ""))[1].split('.')[0].replace("\\", "").replace("/", "")

    return out_paths


csvBasePath = os.path.join(base_path, data_folder_dict.get("csvSF").get("root"))
jsonBasePath = os.path.join(base_path, data_folder_dict.get("jsonSF").get("root"))

if not checkMigrationFolderStruct():
    createMigrationFolderStruct()

to_json(csvBasePath, jsonBasePath)