import unittest
import os
import definitions
import xml.etree.ElementTree as etree
from Parser.XmlMonsterFileParser import XmlMonsterFileParser


class XmlMonsterFileParserTest(unittest.TestCase):

    def setUp(self):
        self.monster_xml = os.path.join(definitions.XML_RESOURCES_PATH, '5e-SRD-Monsters[FIGHTCLUB].xml')
        self.invalid_xml = os.path.join(definitions.XML_RESOURCES_PATH, 'InvalidXml.xml')
        self.file_parser = XmlMonsterFileParser(self.monster_xml)

    def test_get_monster_list_from_file(self):
        empty_parser = XmlMonsterFileParser()
        monster_list = empty_parser.get_monster_list_from_file()
        self.assertEquals(len(monster_list), 0)

        monster_list = self.file_parser.get_monster_list_from_file()
        self.assertEquals(len(monster_list), 6)

    def test_get_tree_from_file(self):
        self.assertNotEquals(self.file_parser.get_tree_from_file(self.monster_xml), None)

        with self.assertRaises(FileNotFoundError):
            self.file_parser.get_tree_from_file("/I/Dont/Exist.xml")

        with self.assertRaises(etree.ParseError):
            self.file_parser.get_tree_from_file(self.invalid_xml)
