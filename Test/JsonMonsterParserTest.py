import json

from Parser.Monster import Monster
from Parser.JsonMonsterAttributeParser import JsonMonsterAttributeParser
from Parser.JsonFileMonsterParser import JsonFileMonsterParser


class JsonMonsterParserTest(object):

    srd_monsters_json = "../Resources/5e-SRD-Monsters[DMTOOLS].json"
    invalid_json = "../Resources/InvalidJson.json"

    @staticmethod
    def invalid_json_test():
        """test get exception on invalid_json"""