import json
import logging
import logging.config
from Parser.Monster import Monster
from Parser.JsonMonsterAttributeParser import JsonMonsterAttributeParser

logging.config.fileConfig('../../Resources/Logging/logging.conf')
logger = logging.getLogger('basicLog')


class JsonBlobMonsterParser(object):
    def __init__(self, json_blob):
        try:
            self.decoded_json = json.loads(json_blob)
        except (ValueError, KeyError, TypeError):
            logger.error("Context=" + __class__.__name__ +
                         "|Message=" + "Problem loading input JSON. Invalid format." +
                         "|Json=" + json_blob)
            raise

    @staticmethod
    def get_monster(entry):
        monster = None
        monster_entry_parser = JsonMonsterAttributeParser(entry)
        name = monster_entry_parser.get_name()
        if name != "":
            """basics"""
            monster = Monster(name)
            monster.size = monster_entry_parser.get_size()
            monster.subtype = monster_entry_parser.get_subtype()

            """complex types"""
            monster.special_abilities = monster_entry_parser.get_special_abilities()
            monster.actions = monster_entry_parser.get_actions()
            monster.legendary_actions = monster_entry_parser.get_legendary_actions()
        return monster

    def get_monster_list(self):
        monster_list = []

        for entry in self.decoded_json:
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
            logger.error("Context=" + __class__.__name__ + "|Message=" + "File not found." + "|Path=" + self.file_path)
            raise
        if self.json_blob_parser:
            return self.json_blob_parser.get_monster_list()
        else:
            logger.error("Context=" + __class__.__name__ +
                         "|Message=" + "Cannot get monster list from Json." +
                         "|Path=" + self.file_path)
