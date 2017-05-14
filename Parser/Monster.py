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


class Monster(object):
    """
    :type name: str
    :type legendary_nickname: str
    :type special_abilities: list of MonsterSpecialAbility
    :type actions: list of MonsterAction
    :type armor_class_with_description: str
    :type legendary_actions: list of MonsterLegendaryAction
    """
    def __init__(self, name):
        self.SIZE_LIST = ["tiny", "small", "medium", "large", "huge", "gargantuan"]
        self.name = name
        self.legendary_nickname = ""
        self.size = ""
        self.type = ""
        self.subtype = ""
        self.alignment = ""
        self.armor_class_with_description = ""
        self.speed_with_description = ""
        self.hit_points_with_hit_dice = ""
        self.saving_throws = ""
        self.skills = ""
        self.senses = ""
        self.languages = ""
        self.challenge_rating = -1
        self.special_abilities = []
        self.actions = []
        self.legendary_actions = []

        self.strength = 10
        self.dexterity = 10
        self.wisdom = 10
        self.intelligence = 10
        self.charisma = 10
        self.constitution = 10
