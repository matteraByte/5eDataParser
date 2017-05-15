from Parser.Monster import Monster, MonsterSpecialAbility, MonsterAction, MonsterLegendaryAction
from Objects.MonsterFieldsXml import MonsterFieldsXml as XML_FIELDS


class XmlMonsterAttributeParser(object):
    """A 5e Monster with the following properties:

            <name>: String, The monster's name.
            <size>: String, Text description of the monster's size (tiny, small, medium, large, huge, gargantuan)
            <type>: String, Monster's type (humanoid, undead, fiend)
        """

    def __init__(self, entry):
        self.entry = entry

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
        return self.get_attribute(XML_FIELDS.NAME)

    def get_type(self):
        raw_type = self.get_attribute(XML_FIELDS.TYPE)

        return raw_type.split(",")[0].split(" ")[0]

    def get_subtype(self):
        subtype = ""
        raw_type_and_subtype = self.get_attribute(XML_FIELDS.TYPE)
        raw_type_list = raw_type_and_subtype.split(",")[0].split("(")
        if len(raw_type_list) > 1:
            subtype = ''.join(c for c in raw_type_list[1] if c not in '()')
        return subtype

    def get_size(self):
        raw_size = self.get_attribute(XML_FIELDS.SIZE)
        if raw_size != "":
            for allowed_size in Monster.ALLOWED_SIZE_LIST:
                if allowed_size[0].lower() == raw_size[0].lower():
                    return allowed_size
        return ""

    def get_hit_points_with_hit_dice(self):
        hit_points_with_hit_dice = self.get_attribute(XML_FIELDS.HIT_POINTS)
        return hit_points_with_hit_dice

    def get_challenge_rating(self):
        challenge_rating = self.get_attribute(XML_FIELDS.CHALLENGE_RATING)
        try:
            return int(challenge_rating)
        except:
            return 0

    def get_languages(self):
        languages = self.get_attribute(XML_FIELDS.LANGUAGES)
        return languages

    def get_senses(self):
        senses = self.get_attribute(XML_FIELDS.SENSES)
        return senses

    def get_skills(self):
        skills = self.get_attribute(XML_FIELDS.SKILLS)
        return skills

    def get_saving_throws(self):
        saving_throws = self.get_attribute(XML_FIELDS.SAVING_THROWS)
        return saving_throws

    def get_special_abilities(self):
        """
        :rtype: list of MonsterSpecialAbility
        """
        ability_list = self.get_attribute_from_entry(self.entry, XML_FIELDS.SPECIAL_ABILITIES.ROOT)
        result = []
        for monster_ability in ability_list:
            ability = MonsterSpecialAbility()
            ability.name = self.get_attribute_text_from_entry(
                monster_ability, XML_FIELDS.SPECIAL_ABILITIES.NAME)
            ability.description = self.get_description(
                monster_ability, XML_FIELDS.SPECIAL_ABILITIES.DESCRIPTION)
            result.append(ability)
        return result

    def get_actions(self):
        """
        :rtype: list of MonsterAction
        """
        action_list = self.get_attribute_from_entry(self.entry, XML_FIELDS.ACTIONS.ROOT)
        result = []
        for monster_action in action_list:
            action = MonsterAction()
            action.name = self.get_attribute_text_from_entry(monster_action, XML_FIELDS.ACTIONS.NAME)
            """description could have multiple text lines"""
            action.description = self.get_description(monster_action, XML_FIELDS.ACTIONS.DESCRIPTION)
            action.attack_bonus = self.get_attack_bonus(monster_action, XML_FIELDS.ACTIONS.ATTACK_BONUS)
            action.damage_dice = self.get_damage_dice(monster_action, XML_FIELDS.ACTIONS.DAMAGE_DICE)
            action.damage_bonus = self.get_damage_bonus(monster_action, XML_FIELDS.ACTIONS.DAMAGE_BONUS)
            result.append(action)

        return result

    def get_damage_bonus(self, entry, field_name):
        return self.get_damage_bonus_from_attack_string(
            self.get_attribute_text_from_entry(entry, field_name))

    def get_damage_dice(self, entry, field_name):
        return self.get_damage_dice_from_attack_string(
            self.get_attribute_text_from_entry(entry, field_name))

    def get_attack_bonus(self, entry, field_name):
        return self.get_attack_bonus_from_attack_string(
            self.get_attribute_text_from_entry(entry, field_name))

    def get_description(self, entry, field_name):
        return self.get_appended_nodes(
            self.get_attribute_from_entry(entry, field_name))

    @staticmethod
    def get_attack_bonus_from_attack_string(attack_string):
        """
        :type: attack_string str
        :rtype: int
        """
        result = 0
        attack_array = attack_string.split('|')
        if len(attack_array) > 1:
            try:
                result = int(attack_array[1])
            except:
                """just return zero"""
                result = 0
        return result

    @staticmethod
    def get_damage_dice_from_attack_string(attack_string):
        """
        :type: attack_string str
        :rtype: str
        """
        result = ""
        attack_array = attack_string.split('|')
        if len(attack_array) > 2:
            damage_array = attack_array[2].split('+')
            if len(damage_array) > 0:
                result = damage_array[0]

        return result

    @staticmethod
    def get_damage_bonus_from_attack_string(attack_string):
        """
        :type: attack_string str
        :rtype: int
        """
        result = 0
        attack_array = attack_string.split('|')
        if len(attack_array) > 2:
            damage_array = attack_array[2].split('+')
            if len(damage_array) > 1:
                try:
                    result = int(damage_array[1])
                except:
                    result = 0

        return result

    @staticmethod
    def get_appended_nodes(same_node_list):
        """
        :rtype: str
        """
        result = ""

        for text_node in same_node_list:
            if result != "" or text_node.text is None:  # treat empty node as a newline
                result += " \n"  # add a space and a newline between each text node
            if text_node.text:
                result += text_node.text
        return result

    def get_legendary_actions(self):
        """
        :rtype: list of MonsterLegendaryAction
        """
        monster_legendary_action_list = self.get_attribute_from_entry(self.entry, XML_FIELDS.LEGENDARY_ACTIONS.ROOT)
        result = []
        for monster_legendary_action in monster_legendary_action_list:
            legendary_action = MonsterLegendaryAction()
            legendary_action.name = self.get_attribute_text_from_entry(
                monster_legendary_action, XML_FIELDS.LEGENDARY_ACTIONS.NAME)
            """description could have multiple text lines"""
            legendary_action.description = self.get_description(
                monster_legendary_action, XML_FIELDS.LEGENDARY_ACTIONS.DESCRIPTION)
            legendary_action.attack_bonus = self.get_attack_bonus(
                monster_legendary_action, XML_FIELDS.LEGENDARY_ACTIONS.ATTACK_BONUS)
            legendary_action.damage_dice = self.get_damage_dice(
                monster_legendary_action, XML_FIELDS.LEGENDARY_ACTIONS.DAMAGE_DICE)
            legendary_action.damage_bonus = self.get_damage_bonus(
                monster_legendary_action, XML_FIELDS.LEGENDARY_ACTIONS.DAMAGE_BONUS)
            result.append(legendary_action)

        return result

