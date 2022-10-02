import os
import json

def weapon_full_file_etl(jsonRawBasePath, jsonOutBasePath):

    weapon_folder = 'weapons'
    out_file_name = 'weapon.json'

    pass

def armor_full_file_etl(jsonRawBasePath, jsonOutBasePath):

    armor_folder = 'armors'
    armor_file = 'Armaduras_Charm.json'
    # set_folder = 'sets'

    out_json = []
    out_file_name = 'equipment.json'

    equip_slot_alignment = {
        "Head": "head",
        "Chest": "chest",
        "Arms": "arm",
        "Waist": "waist",
        "Legs": "leg"

    }

    raw_armor_path = os.path.join(jsonRawBasePath, armor_folder, armor_file)
    with open(raw_armor_path, 'r', encoding='utf-8') as jsonf:
        raw_armor_json = json.load(jsonf)
        for armor in raw_armor_json:
            out_armor = {
                    "part": str(equip_slot_alignment.get(armor.get("Equip Slot"))),
                    "skills": [],
                    "name": str(armor.get("Name")),
                    "slots": [
                        armor.get("Slot 1 size"),
                        armor.get("Slot 2 size"),
                        armor.get("Slot 3 size")
                    ],
                    "rank": str(armor.get("Variant")),
                    "set": str(armor.get("Set Skill 1").split(": ")[0])
            }
            for i in range(1, 4):
                key_name = "Skill " + str(i)
                skill = armor.get(key_name)
                if skill and not skill.startswith('0:'):
                    out_armor["skills"].append(
                        {
                            "name": str(skill.split(': ')[1]),
                            "level": armor.get("Skill " + str(i) + " Level")
                        }
                    )

            out_json.append(out_armor)

    out_armor_path = os.path.join(jsonOutBasePath, armor_folder, out_file_name)
    with open(out_armor_path, "w", encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(out_json, indent=4))



def generate_set_bonus(jsonRawBasePath, jsonOutBasePath):



    pass

def get_files(path) -> list:

    filenames = []

    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)):
            filenames.append(filename.split('.')[0])

    return filenames


jsonRawBasePath = r'.\\rawFiles'
jsonOutBasePath = r'.\\newFiles'


armor_full_file_etl(jsonRawBasePath, jsonOutBasePath)
