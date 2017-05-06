from Parser.JsonFileMonsterParser import JsonFileMonsterParser

fileLocation = "../Resources/5e-SRD-Monsters[DMTOOLS].json"
invalidJsonFile = "../Resources/InvalidJson.json"
decoded = []

file_parser = JsonFileMonsterParser(fileLocation)
monster_list = file_parser.get_monster_list()

for monster in monster_list:
    print("Monster name: ", monster.name)
    print("Monster size: ", monster.size)
    print("Monster subtype: ", monster.subtype)

    print("\nMonster special_abilities: ")
    for special in monster.special_abilities:
        print("name: ", special.name)
        print("attack_bonus: ", special.attack_bonus)
        print("desc: ", special.description)

    print("\nMonster actions: ")
    for action in monster.actions:
        print("name: ", action.name)
        print("attack_bonus: ", action.attack_bonus)
        print("desc: ", action.description)
        print("damage_bonus: ", action.damage_bonus)

    print("\nMonster legendary actions: ")
    for leg_action in monster.legendary_actions:
        print("name: ", leg_action.name)
        print("attack bonus: ", leg_action.attack_bonus)
        print("desc: ", leg_action.description)
        print("damage_bonus: ", leg_action.damage_bonus)
