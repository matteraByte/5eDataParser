from Parser.Monster import Monster, MonsterSpecialAbility, MonsterAction, MonsterLegendaryAction
from Objects.MonsterFieldsXml import *


class XmlMonsterAttributeParser(object):
    """A 5e Monster with the following properties:

            <name>: String, The monster's name.
            <size>: String, Text description of the monster's size (tiny, small, medium, large, huge, gargantuan)
            <type>: String, Monster's type (humanoid, undead, fiend)
        """

    def __init__(self, entry):
        self.entry = entry
        self.MONSTER_FIELDS = MonsterFieldsXml()

    @staticmethod
    def get_attribute_from_entry(xml_root, node_name):
        result = []
        try:
            result = xml_root.findall(node_name)
        except KeyError:
            """No key - return blank"""
        return result

    def get_attribute_text_from_entry(self, xml_root, node_name):
        nodes = self.get_attribute_from_entry(xml_root, node_name)
        try:
            result = nodes[0].text
        except:
            result = ""
        return result

    def get_attribute(self, attribute_name):
        return self.get_attribute_text_from_entry(self.entry, attribute_name)

    def get_name(self):
        """Gets the name of the monster from xml node"""
        return self.get_attribute(self.MONSTER_FIELDS.NAME)

    # def get_size(self):
    #     return self.get_attribute("size")
    #
    # def get_subtype(self):
    #     return self.get_attribute("subtype")
    #

    def get_special_abilities(self):
        """
        :rtype: list of MonsterSpecialAbility
        """
        monster_abilities = self.get_attribute_from_entry(self.entry, self.MONSTER_FIELDS.SPECIAL_ABILITIES.ROOT)
        result = []
        for entry in monster_abilities:
            ability = MonsterSpecialAbility()
            # ability.attack_bonus = self.get_attribute_from_entry(entry, "attack_bonus")
            ability.attack_bonus = 0
            ability.name = self.get_attribute_text_from_entry(entry, self.MONSTER_FIELDS.SPECIAL_ABILITIES.NAME)
            ability.description = self.get_attribute_text_from_entry(entry, self.MONSTER_FIELDS.SPECIAL_ABILITIES.DESCRIPTION)
            result.append(ability)
        return result

    def get_actions(self):
        """
        :rtype: list of MonsterAction
        """
        monster_actions = self.get_attribute_from_entry(self.entry, self.MONSTER_FIELDS.ACTIONS.ROOT)
        result = []
        for entry in monster_actions:
            action = MonsterAction()
            action.name = self.get_attribute_text_from_entry(entry, self.MONSTER_FIELDS.ACTIONS.NAME)
            """could have multiple text lines"""
            action.description = self.getAppendedDescription(self.get_attribute_from_entry(entry, self.MONSTER_FIELDS.ACTIONS.NAME))
            result.append(action)

        return result

    """
    :rtype: str
    """
    def getAppendedDescription(self, descriptions_list):
        result = ""
        # TODO: impliment
        # for text_node in descriptions_list:
        #     result += self.get_attribute_text_from_entry(text_node, )
        #     result
        return result

    def get_legendary_actions(self):
        """
        :rtype: list of MonsterLegendaryAction
        """
        result = []
        return result

    #     monster_actions = self.get_attribute("actions")
    #     result = []
    #     if monster_actions != "":
    #         for entry in monster_actions:
    #             action = MonsterAction()
    #             action.attack_bonus = self.get_attribute_from_json_entry(entry, "attack_bonus")
    #             action.name = self.get_attribute_from_json_entry(entry, "name")
    #             action.description = self.get_attribute_from_json_entry(entry, "desc")
    #             action.damage_dice = self.get_attribute_from_json_entry(entry, "damage_dice")
    #             action.damage_bonus = self.get_attribute_from_json_entry(entry, "damage_bonus")
    #             result.append(action)
    #     return result
    #
    # def get_legendary_actions(self):
    #     monster_legendary_actions = self.get_attribute("legendary_actions")
    #     result = []
    #     if monster_legendary_actions != "":
    #         for entry in monster_legendary_actions:
    #             legendaryAction = MonsterLegendaryAction()
    #             legendaryAction.attack_bonus = self.get_attribute_from_json_entry(entry, "attack_bonus")
    #             legendaryAction.name = self.get_attribute_from_json_entry(entry, "name")
    #             legendaryAction.description = self.get_attribute_from_json_entry(entry, "desc")
    #             legendaryAction.damage_dice = self.get_attribute_from_json_entry(entry, "damage_dice")
    #             legendaryAction.damage_bonus = self.get_attribute_from_json_entry(entry, "damage_bonus")
    #             result.append(legendaryAction)
    #     return result
