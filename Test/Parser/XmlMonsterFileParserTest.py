import unittest
import os
import definitions
import xml.etree.ElementTree as etree
from Parser.XmlMonsterFileParser import XmlMonsterFileParser


class XmlMonsterFileParserTest(unittest.TestCase):

    def setUp(self):
        self.monster_srd_xml = os.path.join(definitions.XML_RESOURCES_PATH, '5e-SRD-Monsters[FIGHTCLUB].xml')
        self.monster_xml = os.path.join(definitions.XML_RESOURCES_PATH, 'Aboleth.xml')
        self.invalid_xml = os.path.join(definitions.XML_RESOURCES_PATH, 'InvalidXml.xml')
        self.srd_file_parser = XmlMonsterFileParser(self.monster_srd_xml)
        self.monster_file_parser = XmlMonsterFileParser(self.monster_xml)

    def test_get_monster_list_from_file(self):
        empty_parser = XmlMonsterFileParser()
        monster_list = empty_parser.get_monster_list_from_file()
        self.assertEquals(len(monster_list), 0)

        monster_list = self.srd_file_parser.get_monster_list_from_file()
        self.assertEquals(len(monster_list), 6)

    def test_get_tree_from_file(self):
        self.assertNotEquals(self.srd_file_parser.get_tree_from_file(self.monster_srd_xml), None)

        with self.assertRaises(FileNotFoundError):
            self.srd_file_parser.get_tree_from_file("/I/Dont/Exist.xml")

        with self.assertRaises(etree.ParseError):
            self.srd_file_parser.get_tree_from_file(self.invalid_xml)

    def test_get_monster(self):
        monster_list = self.monster_file_parser.get_monster_list_from_file()

        self.assertEquals(len(monster_list), 1)
        monster = monster_list[0]

        self.assertEquals(monster.strength, 21)
        self.assertEquals(monster.dexterity, 9)
        self.assertEquals(monster.charisma, 18)
        self.assertEquals(monster.constitution, 15)
        self.assertEquals(monster.intelligence, 18)
        self.assertEquals(monster.wisdom, 15)

        self.assertEquals(monster.alignment, "lawful evil")
        self.assertEquals(monster.speed_with_description, "10 ft., swim 40 ft.")
        self.assertEquals(monster.type, "aberration")
        self.assertEquals(monster.subtype, "fish")
        self.assertEquals(monster.size, "large")
        self.assertEquals(monster.senses, "darkvision 120 ft.")
        self.assertEquals(monster.saving_throws, "Con +6, Int +8, Wis +6")
        self.assertEquals(monster.hit_points_with_hit_dice, "135 (18d10+36)")
        self.assertEquals(monster.challenge_rating, 10)
        self.assertEquals(monster.languages, "Deep Speech, telepathy 120 ft.")
        self.assertEquals(monster.skills, "History +12, Perception +10")
        self.assertEquals(monster.armor_class_with_description, "17 (natural armor)")
        self.assertEquals(len(monster.actions), 4)
        self.assertEquals(len(monster.special_abilities), 3)
        self.assertEquals(len(monster.legendary_actions), 3)

