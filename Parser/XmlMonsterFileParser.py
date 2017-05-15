import logging
import logging.config
import definitions
import xml.etree.ElementTree as etree
from Objects.MonsterFieldsXml import MonsterFieldsXml as XML_FIELDS
from Parser.Monster import Monster
from Parser.XmlMonsterAttributeParser import XmlMonsterAttributeParser as AttributeParser

logging.config.fileConfig(definitions.LOGGING_CONFIG_PATH)
logger = logging.getLogger('basicLog')


class XmlMonsterFileParser(object):
    def __init__(self, file_path=""):
        self.file_path = file_path
        self.blob_parser = None

    def get_monster_list_from_file(self, file_path=""):
        if file_path != "":
            self.file_path = file_path
        if self.file_path == "":
            logger.error("Context=" + __class__.__name__ +
                         "|Message=" + "Must define file path.")
            return []

        monster_list = XmlMonsterFileParser.get_monster_list(
            XmlMonsterFileParser.get_tree_from_file(self.file_path))

        if monster_list:
            return monster_list
        else:
            return []

    @staticmethod
    def get_monster(monster_element):
        attribute_parser = AttributeParser(monster_element)
        monster = Monster(attribute_parser.get_name())
        monster.actions = attribute_parser.get_actions()
        monster.special_abilities = attribute_parser.get_special_abilities()
        monster.legendary_actions = attribute_parser.get_legendary_actions()

        monster.strength = attribute_parser.get_strength()
        monster.dexterity = attribute_parser.get_dexterity()
        monster.intelligence = attribute_parser.get_intelligence()
        monster.constitution = attribute_parser.get_constitution()
        monster.wisdom = attribute_parser.get_wisdom()
        monster.charisma = attribute_parser.get_charisma()

        monster.speed_with_description = attribute_parser.get_speed_with_description()
        monster.skills = attribute_parser.get_skills()
        monster.languages = attribute_parser.get_languages()
        monster.saving_throws = attribute_parser.get_saving_throws()
        monster.senses = attribute_parser.get_senses()
        monster.challenge_rating = attribute_parser.get_challenge_rating()
        monster.hit_points_with_hit_dice = attribute_parser.get_hit_points_with_hit_dice()
        monster.size = attribute_parser.get_size()
        monster.type = attribute_parser.get_type()
        monster.subtype = attribute_parser.get_subtype()
        monster.alignment = attribute_parser.get_alignment()
        monster.armor_class_with_description = attribute_parser.get_armor_class_with_description()

        return monster

    @staticmethod
    def get_monster_list(tree):
        monster_list = []
        root_node = tree.getroot()
        monster_element_list = root_node.findall(XML_FIELDS.MONSTER_TAG)

        for monster_element in monster_element_list:
            monster_list.append(XmlMonsterFileParser.get_monster(monster_element))
        return monster_list

    @staticmethod
    def get_tree_from_file(file_path):
        try:
            tree = etree.parse(file_path)
        except FileNotFoundError:
            logger.error("Context=" + __class__.__name__ +
                         "|Message=" + "File not found." + "|Path=" + file_path)
            raise
        except etree.ParseError:
            logger.error("Context=" + __class__.__name__ +
                         "|Message=" + "Xml Parse error. Invalid XML." + "|Path=" + file_path)
            raise
        return tree
