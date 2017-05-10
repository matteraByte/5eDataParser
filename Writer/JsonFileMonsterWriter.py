import json
from Parser.Monster import Monster, MonsterSpecialAbility
from Objects.MonsterFieldsJson import MonsterFieldsJson, MonsterFieldsSpecialAbilities


class JsonBlobMonsterBuilder(object):
    """
    :type monster_list: list of Monster
    """
    def __init__(self, monster_list):
        self.monster_list = monster_list
        self.fields = MonsterFieldsJson()
        self.special_abilities_fields = MonsterFieldsSpecialAbilities()

    def build_json_blob(self):
        json_root = []
        raw_blob = {}
        my_monster = self.monster_list[0]

        raw_blob[self.fields.NAME] = my_monster.name
        raw_blob[self.fields.SIZE] = my_monster.size
        raw_blob[self.special_abilities_fields.ROOT] = self.build_special_abilities(my_monster.special_abilities)
        json_root.append(raw_blob)
        json_blob = json.dumps(json_root)
        return json_blob

    def build_special_abilities(self, monster_special_abilities):
        print("length of special abilities: ", len(monster_special_abilities))
        special_abilities = []

        for monster_special_ability in monster_special_abilities:
            ability = MonsterSpecialAbility()
            ability = monster_special_ability
            json_special_ability = {}
            json_special_ability[self.special_abilities_fields.NAME] = ability.name
            json_special_ability[self.special_abilities_fields.DESCRIPTION] = ability.description
            json_special_ability[self.special_abilities_fields.ATTACK_BONUS] = ability.attack_bonus
            special_abilities.append(json_special_ability)

        return special_abilities


class JsonFileMonsterWriter(object):
    def __init__(self, file_path):
        self.file_path = file_path
        self.json_blob_parser = None