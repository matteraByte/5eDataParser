class Monster(object):
    """A 5e Monster with the following properties:

            name: String, The monster's name.
            size: String, Text description of the monster's size (tiny, small, medium, large, huge, gargantuan)
            type: String, Monster's type (humanoid, undead, fiend)
    """
    def __init__(self, name):
        """Return a Monster object whose name is *name*"""

        self.SIZE_LIST = ["tiny", "small", "medium", "large", "huge", "gargantuan"]
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


class MonsterAction(object):
    def __init__(self):
        self.name = ""
        self.description = ""
        self.damage_dice = ""
        """attack_bonus int"""
        self.attack_bonus = 0
        """damage_bonus int"""
        self.damage_bonus = 0


class MonsterLegendaryAction(object):
    def __init__(self):
        self.name = ""
        self.description = ""
        self.damage_dice = ""
        """attack_bonus int"""
        self.attack_bonus = 0
        """damage_bonus int"""
        self.damage_bonus = 0
