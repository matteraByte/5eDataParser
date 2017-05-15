import unittest
import json
import logging
import logging.config
import Definitions
import os
from Parser.JsonFileMonsterParser import JsonBlobMonsterParser
from Parser.Monster import Monster

logging.config.fileConfig(Definitions.LOGGING_CONFIG_PATH)
logger = logging.getLogger('basicLog')


class JsonBlobMonsterParserTest(unittest.TestCase):

    def setUp(self):
        self.entry_file_path_monster = "../../Resources/DMTools/Aboleth.json"
        self.srd_monsters_file_path = "../../Resources/DMTools/5e-SRD-Monsters[DMTOOLS].json"

        with open(self.entry_file_path_monster, 'r') as inputFile:
            self.monster_json_blob = inputFile.read().replace('\n', '')

        try:
            self.decoded_monster = json.loads(self.monster_json_blob)
        except (ValueError, KeyError, TypeError):
            logger.error("Context=" + __class__.__name__ +
                         "|Message=" + "Error loading input JSON. Invalid format." +
                         "|Json=" + self.monster_json_blob)
            raise

        with open(self.srd_monsters_file_path, 'r') as inputFile:
            self.srd_json_blob = inputFile.read().replace('\n', '')

    def test_get_monster(self):
        json_blob_parser = JsonBlobMonsterParser(self.monster_json_blob)

        expected = Monster("Aboleth")
        expected.size = ("Large")

        result = json_blob_parser.get_monster(self.decoded_monster)

        self.assertEquals(result.name, expected.name)
        # self.assertEquals(result.type, expected.type)
        self.assertEquals(result.size, expected.size)

    def test_get_monsters(self):
        json_blob_parser = JsonBlobMonsterParser(self.srd_json_blob)
        expected = 325

        monster_list = json_blob_parser.get_monster_list()

        self.assertEquals(len(monster_list), expected)
