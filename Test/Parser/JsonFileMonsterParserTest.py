import unittest
from Parser.JsonFileMonsterParser import JsonFileMonsterParser


class JsonFileMonsterParserTest(unittest.TestCase):

    def setUp(self):
        self.srd_monsters_json = "../../Resources/DMTools/5e-SRD-Monsters[DMTOOLS].json"
        self.invalid_json = "../../Resources/InvalidJson.json"

    def test_file_not_found(self):
        """test get exception on file not found"""
        fileParser = JsonFileMonsterParser("/NoFileHere/nope.json")
        with self.assertRaises(FileNotFoundError):
            fileParser.get_monster_list()
