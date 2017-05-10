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

    def test_get_actions(self):
        actions = self.parser.get_actions()
        self.assertNotEquals(len(actions), 0)
        action1 = actions[0]
        action2 = actions[1]
        self.assertEquals(action1.name, "Multiattack")
        self.assertEquals(action1.description, "Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 12 (2d6 + 5) bludgeoning damage. If the target is a creature, it must succeed on a DC 14 Constitution saving throw or become diseased. The disease has no effect for 1 minute and can be removed by any magic that cures disease. After 1 minute, the diseased creature's skin becomes translucent and slimy, the creature can't regain hit points unless it is underwater, and the disease can be removed only by heal or another disease-curing spell of 6th level or higher. When the creature is outside a body of water, it takes 6 (1d12) acid damage every 10 minutes unless moisture is applied to the skin before 10 minutes have passed.")
        self.assertEquals(action1.damage_dice, "2d6")
        self.assertEquals(action1.attack_bonus, 9)
        self.assertEquals(action2.name, "Tail")
        self.assertEquals(action1.damage_dice, "3d6")
        self.assertEquals(action1.attack_bonus, 9)
