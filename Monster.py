class Monster(object):
    """A 5e Monster with the following properties:

            name: String, The monster's name.
            size: String, Text description of the monster's size (tiny, small, medium, large, huge, gargantuan)
            type: String, Monster's type (humanoid, undead, fiend)
        """
    def __init__(self, name):
        """Return a Monster object whose name is *name*"""
        self.name = name
        self.size = ""
        self.type = ""
        self.subtype = ""
        self.special_abilities = []
        self.actions = []
        self.legendary_actions = []


class MonsterSpecialAbility(object):
    def __init__(self):
        self.name = ""
        self.description = ""
        """attack_bonus int"""
        self.attack_bonus = 0


class MonsterAction(object):
    def __init__(self):
        self.name = ""
        self.description = ""
        """attack_bonus int"""
        self.attack_bonus = 0
        self.damage_dice = ""
        """damage_bonus int"""
        self.damage_bonus = 0


class MonsterLegendaryAction(object):
    def __init__(self):
        self.name = ""
        self.description = ""
        """attack_bonus int"""
        self.attack_bonus = 0
        """damage_bonus int"""
        self.damage_bonus = 0


class JsonMonsterParser(object):
    """A 5e Monster with the following properties:

            name: String, The monster's name.
            size: String, Text description of the monster's size (tiny, small, medium, large, huge, gargantuan)
            type: String, Monster's type (humanoid, undead, fiend)
        """

    def __init__(self, entry):
        self.entry = entry
        """Return a JsonMonsterParser"""

    @staticmethod
    def get_attribute_from_json_entry(json_entry, attribute_name):
        attribute = ""
        try:
            attribute = json_entry[attribute_name]
        except KeyError:
            """No key - return blank"""
        return attribute

    def get_attribute(self, attribute_name):
        return self.get_attribute_from_json_entry(self.entry, attribute_name)

    def get_name(self):
        """Gets the name of the monster from json entry"""
        return self.get_attribute("name")

    def get_size(self):
        return self.get_attribute("size")

    def get_subtype(self):
        return self.get_attribute("subtype")

    def get_special_abilities(self):
        monster_abilities = self.get_attribute("special_abilities")
        result = []
        if monster_abilities != "":
            for entry in monster_abilities:
                ability = MonsterSpecialAbility()
                ability.attack_bonus = self.get_attribute_from_json_entry(entry, "attack_bonus")
                ability.name = self.get_attribute_from_json_entry(entry, "name")
                ability.description = self.get_attribute_from_json_entry(entry, "desc")
                """TODO: Since using generic method for grabbing int too, need to set default to 0"""
                result.append(ability)
        return result

    def get_actions(self):
        monster_actions = self.get_attribute("actions")
        result = []
        if monster_actions != "":
            for entry in monster_actions:
                action = MonsterAction()
                """TODO: Since using generic method for grabbing int too, need to set default to 0"""
                action.attack_bonus = self.get_attribute_from_json_entry(entry, "attack_bonus")
                action.name = self.get_attribute_from_json_entry(entry, "name")
                action.description = self.get_attribute_from_json_entry(entry, "desc")
                action.damage_dice = self.get_attribute_from_json_entry(entry, "damage_dice")
                action.damage_bonus = self.get_attribute_from_json_entry(entry, "damage_bonus")
                result.append(action)
        return result

    def get_legendary_actions(self):
        monster_legendary_actions = self.get_attribute("legendary_actions")
        result = []
        if monster_legendary_actions != "":
            for entry in monster_legendary_actions:
                legendaryAction = MonsterLegendaryAction()
                """TODO: Since using generic method for grabbing int too, need to set default to 0"""
                legendaryAction.attack_bonus = self.get_attribute_from_json_entry(entry, "attack_bonus")
                legendaryAction.name = self.get_attribute_from_json_entry(entry, "name")
                legendaryAction.description = self.get_attribute_from_json_entry(entry, "desc")
                legendaryAction.damage_dice = self.get_attribute_from_json_entry(entry, "damage_dice")
                legendaryAction.damage_bonus = self.get_attribute_from_json_entry(entry, "damage_bonus")
                result.append(legendaryAction)
        return result
