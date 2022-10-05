import os

base_path = '.\\migration'

data_folder_dict = {
    "csvSF": {
        "root": "csvSourceFiles",
        "subfolders": [
#             'charm',
#             'decoration',
#             'equipment',
#             'skill',
#             'weapon',
        ]
    },
    "jsonSF": {
        "root": "jsonSourceFiles",
        "subfolders": [
            'charm',
            'decoration',
            'equipment',
            'skill',
            'weapon',
        ]
    },
    "newSrcDF": {
        "root": "newData",
        "subfolders": [
            'charm',
            'decoration',
            'equipment',
            'skill',
            'weapon',
        ]
    }
}

def createMigrationFolderStruct():

    for key in data_folder_dict:
        folder = data_folder_dict.get(key)
        for subfolder in folder.get("subfolders"):
            folder_path = os.path.join(base_path, folder.get("root"), subfolder)
            os.makedirs(folder_path, exist_ok=True)

def checkMigrationFolderStruct() -> bool:

    if os.path.exists(base_path):
        for key in data_folder_dict:
            folder = data_folder_dict.get(key)
            for subfolder in folder.get("subfolders"):
                folder_path = os.path.join(base_path, folder.get("root"), subfolder)
                if not os.path.exists(folder_path):
                    return False
        return True
    else:
        return False

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
