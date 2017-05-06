import json
from Parser.Monster import Monster
from Parser.JsonMonsterAttributeParser import JsonMonsterAttributeParser


class JsonBlobMonsterParser(object):
    def __init__(self, json_blob):
        self.json_blob = json_blob

    @staticmethod
    def get_monster(entry):
        monster = None
        monster_entry_parser = JsonMonsterAttributeParser(entry)
        name = monster_entry_parser.get_name()
        if name != "":
            monster = Monster(name)
            monster.size = monster_entry_parser.get_size()
            monster.subtype = monster_entry_parser.get_subtype()
            monster.special_abilities = monster_entry_parser.get_special_abilities()
            monster.actions = monster_entry_parser.get_actions()
            monster.special_abilities = monster_entry_parser.get_special_abilities()
            monster.legendary_actions = monster_entry_parser.get_legendary_actions()
        return monster

    def get_monster_list(self):
        monster_list = []
        try:
            decoded_json = json.loads(self.json_blob)
        except (ValueError, KeyError, TypeError):
            print("Error loading input JSON. Invalid format.")
            raise

        for entry in decoded_json:
                monster = self.get_monster(entry)
                if monster:
                    monster_list.append(monster)

        return monster_list


class JsonFileMonsterParser(object):
    def __init__(self, file_path):
        self.file_path = file_path
        self.json_blob_parser = None

    def get_monster_list(self):
        try:
            with open(self.file_path, 'r') as inputFile:
                json_input = inputFile.read().replace('\n', '')
                self.json_blob_parser = JsonBlobMonsterParser(json_input)
        except FileNotFoundError:
            print("Error: File not found. ", self.file_path)
            raise
        if self.json_blob_parser:
            return self.json_blob_parser.get_monster_list()
        else:
            print("Error: cannot get monster list from Json")
