from Monster import Monster, JsonMonsterParser
import json

fileLocation = "/Users/chris.mattera/Desktop/5e-SRD-Monsters.json"
invalidFileLocation = "/Users/chris.mattera/Desktop/invalidJson.json"
decoded = []

with open(fileLocation, 'r') as inputFile:
    json_input = inputFile.read().replace('\n', '')

try:
    decoded = json.loads(json_input)
except (ValueError, KeyError, TypeError):
    print("Error loading input file JSON. Invalid format.")

    # pretty printing of json-formatted string
    # print(json.dumps(decoded, sort_keys=True, indent=4))
    #
    # print("JSON parsing example: ", decoded['one'])
    # print("Complex JSON parsing example: ", decoded['two']['list'][1]['item'])

for entry in decoded:
    parser = JsonMonsterParser(entry)
    name = parser.get_name()
    if name != "":
        matteramon = Monster(name)
        matteramon.size = parser.get_size()
        matteramon.subtype = parser.get_subtype()
        matteramon.special_abilities = parser.get_special_abilities()
        matteramon.actions = parser.get_actions()
        matteramon.special_abilities = parser.get_special_abilities()
        matteramon.legendary_actions = parser.get_legendary_actions()

        print("Monster name: ", matteramon.name)
        print("Monster size: ", matteramon.size)
        print("Monster subtype: ", matteramon.subtype)

        print("\nMonster special_abilities: ")
        for special in matteramon.special_abilities:
            print("name: ", special.name)
            print("attack_bonus: ", special.attack_bonus)
            print("desc: ", special.description)

        print("\nMonster actions: ")
        for action in matteramon.actions:
            print("name: ", action.name)
            print("attack_bonus: ", action.attack_bonus)
            print("desc: ", action.description)
            print("damage_bonus: ", action.damage_bonus)

        print("\nMonster legendary actions: ")
        for leg_action in matteramon.legendary_actions:
            print("name: ", leg_action.name)
            print("attack bonus: ", leg_action.attack_bonus)
            print("desc: ", leg_action.description)
            print("damage_bonus: ", leg_action.damage_bonus)
