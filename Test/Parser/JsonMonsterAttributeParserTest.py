import unittest, json
from Parser.JsonMonsterAttributeParser import JsonMonsterAttributeParser as AttributeParser
from Objects.MonsterFieldsJson import MonsterFieldsJson as MonsterFields


class JsonMonsterAttributeParserTest(unittest.TestCase):

    def setUp(self):
        self.monster_entry = "../../Resources/DMTools/Aboleth.json"

        with open(self.monster_entry, 'r') as inputFile:
            self.json_input = inputFile.read().replace('\n', '')

        self.decoded_json = json.loads(self.json_input)
        self.MONSTER_FIELDS = MonsterFields()
        self.parser = AttributeParser(self.decoded_json)

    def test_get_attribute(self):
        expected = "Aboleth"
        result = None

        result = self.parser.get_attribute_from_entry(self.decoded_json, self.MONSTER_FIELDS.NAME)
        self.assertEquals(result, expected)
        result = self.parser.get_attribute(self.MONSTER_FIELDS.NAME)
        self.assertEquals(result, expected)
        result = self.parser.get_attribute(self.MONSTER_FIELDS.SPECIAL_ABILITIES.ROOT)
        self.assertNotEquals(result, None)
