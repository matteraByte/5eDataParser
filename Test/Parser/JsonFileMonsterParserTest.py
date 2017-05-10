import unittest
import definitions
import os
from Parser.JsonFileMonsterParser import JsonFileMonsterParser


class JsonFileMonsterParserTest(unittest.TestCase):

    def setUp(self):
        self.srd_monsters_json = os.path.join(definitions.JSON_RESOURCES_PATH, "5e-SRD-Monsters[DMTOOLS].json")
        self.invalid_json = os.path.join(definitions.JSON_RESOURCES_PATH, "InvalidJson.json")

    def test_file_not_found(self):
        """test get exception on file not found"""
        fileParser = JsonFileMonsterParser("/NoFileHere/nope.json")
        with self.assertRaises(FileNotFoundError):
            fileParser.get_monster_list()
