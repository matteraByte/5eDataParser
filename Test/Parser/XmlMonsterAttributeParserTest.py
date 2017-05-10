import unittest
import xml.etree.ElementTree as etree
from Parser.XmlMonsterAttributeParser import XmlMonsterAttributeParser as AttributeParser
from Objects.MonsterFieldsXml import MonsterFieldsXml as MonsterFields
from Parser.Monster import Monster, MonsterSpecialAbility


class XmlMonsterAttributeParserTest(unittest.TestCase):

    def setUp(self):
        self.MONSTER_FIELDS = MonsterFields()

        self.monster_entry = "../../Resources/FightClub/Aboleth.xml"
        tree = etree.parse(self.monster_entry)
        self.root = tree.getroot().find("monster")
        self.parser = AttributeParser(self.root)

        self.monster_missing_fields = "../../Resources/FightClub/MissingFields.xml"
        tree = etree.parse(self.monster_missing_fields)
        self.root_missing_fields = tree.getroot().find("monster")
        self.parser_missing_fields = AttributeParser(self.root_missing_fields)

    def test_get_attribute_from_entry(self):

        result = self.parser.get_attribute_from_entry(self.root, self.MONSTER_FIELDS.NAME)
        self.assertEquals(len(result), 1)

        result = self.parser.get_attribute_from_entry(self.root, "invalid")
        self.assertEquals(len(result), 0)

    def test_get_name(self):
        expected = "Aboleth"
        result = self.parser.get_name()
        self.assertEquals(result, expected)

        expected = ""
        result = self.parser_missing_fields.get_name()
        self.assertEquals(result, expected)

    def test_get_special_abilities(self):
        special_abilities = self.parser.get_special_abilities()
        self.assertNotEquals(len(special_abilities), 0)
        ability1 = special_abilities[0]
        ability2 = special_abilities[1]
        self.assertEquals(ability1.name, "Amphibious")
        self.assertEquals(ability1.description, "The aboleth can breathe air and water.")
        self.assertEquals(ability1.attack_bonus, 0)
        self.assertEquals(ability2.name, "Mucous Cloud")
        missing_special_abilities = self.parser_missing_fields.get_special_abilities()
        self.assertEquals(len(missing_special_abilities), 0)

    def test_get_attack_bonus_from_attack_string(self):
        attack_string_normal = "Tail|9|3d6+5"
        expected_normal = 9
        attack_string_weird = "Tail||3d6"
        expected_weird = 0
        attack_string_empty = ""
        expected_empty = 0
        self.assertEquals(self.parser.get_attack_bonus_from_attack_string(attack_string_empty), expected_empty)
        self.assertEquals(self.parser.get_attack_bonus_from_attack_string(attack_string_weird), expected_weird)
        self.assertEquals(self.parser.get_attack_bonus_from_attack_string(attack_string_normal), expected_normal)

    def test_get_damage_bonus_from_attack_string(self):
        attack_string_normal = "Tail|9|3d6+5"
        expected_normal = 5
        attack_string_no_bonus = "Tail|9|3d6"
        expected_no_bonus = 0
        attack_string_weird = "Tail||"
        expected_weird = 0
        attack_string_empty = ""
        expected_empty = 0
        self.assertEquals(self.parser.get_damage_bonus_from_attack_string(attack_string_empty), expected_empty)
        self.assertEquals(self.parser.get_damage_bonus_from_attack_string(attack_string_weird), expected_weird)
        self.assertEquals(self.parser.get_damage_bonus_from_attack_string(attack_string_normal), expected_normal)
        self.assertEquals(self.parser.get_damage_bonus_from_attack_string(attack_string_no_bonus), expected_no_bonus)

    def test_get_damage_dice_from_attack_string(self):
        attack_string_normal = "Tail|9|3d6+5"
        expected_normal = "3d6"
        attack_string_no_bonus = "Tail|9|3d6"
        expected_no_bonus = "3d6"
        attack_string_weird = "Tail||"
        expected_weird = ""
        attack_string_empty = ""
        expected_empty = ""
        self.assertEquals(self.parser.get_damage_dice_from_attack_string(attack_string_empty), expected_empty)
        self.assertEquals(self.parser.get_damage_dice_from_attack_string(attack_string_weird), expected_weird)
        self.assertEquals(self.parser.get_damage_dice_from_attack_string(attack_string_normal), expected_normal)
        self.assertEquals(self.parser.get_damage_dice_from_attack_string(attack_string_no_bonus), expected_no_bonus)

    def test_get_actions(self):
        actions = self.parser.get_actions()
        self.assertNotEquals(len(actions), 0)
        action1 = actions[0]
        action2 = actions[1]
        # action3 = actions[2]
        action4 = actions[3]
        self.assertEquals(action1.name, "Multiattack")
        self.assertEquals(action1.description, "The aboleth makes three tentacle attacks.")
        self.assertEquals(action1.damage_dice, "")
        self.assertEquals(action1.attack_bonus, 0)
        self.assertEquals(action1.damage_bonus, 0)
        self.assertEquals(action4.name, "Enslave (3/day)")
        self.assertEquals(action4.description, "The aboleth targets one creature it can see within 30 ft. of it. "
                                               "The target must succeed on a DC 14 Wisdom saving throw or be magically "
                                               "charmed by the aboleth until the aboleth dies or until it is on a "
                                               "different plane of existence from the target. The charmed target is "
                                               "under the aboleth's control and can't take reactions, and the aboleth "
                                               "and the target can communicate telepathically with each other over any "
                                               "distance. \nWhenever the charmed target takes damage, the target can "
                                               "repeat the saving throw. On a success, the effect ends. No more than "
                                               "once every 24 hours, the target can also repeat the saving throw when "
                                               "it is at least 1 mile away from the aboleth.")
        self.assertEquals(action2.name, "Tentacle")
        self.assertEquals(action2.attack_bonus, 9)
        self.assertEquals(action2.damage_bonus, 5)
        self.assertEquals(action2.damage_dice, "2d6")

