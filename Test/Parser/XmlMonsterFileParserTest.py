import unittest
import os
import definitions
from Parser.XmlMonsterFileParser import XmlMonsterFileParser


class XmlMonsterFileParserTest(unittest.TestCase):

    def setUp(self):
        self.monster_xml = os.path.join(definitions.XML_RESOURCES_PATH, '5e-SRD-Monsters[FIGHTCLUB].xml')
        print(self.monster_xml)
        self.file_parser = XmlMonsterFileParser(self.monster_xml)

    def test_get_monster_list_from_file(self):
        result = self.file_parser.get_monster_list_from_file()
        self.assertEquals(len(result), 325)

