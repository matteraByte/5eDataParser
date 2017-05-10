
class MonsterFieldsJson(object):
    def __init__(self):
        """Types"""
        self.XML = "xml"
        self.JSON = "json"

        """Basic Fields"""
        self.NAME = 'name'
        self.TYPE = 'type'
        self.SIZE = 'size'
        self.SPECIAL_ABILITIES = MonsterFieldsSpecialAbilities()


class MonsterFieldsSpecialAbilities(object):
    def __init__(self):
        """Special Abilities"""
        self.ROOT = 'special_abilities'
        self.NAME = 'name'
        self.DESCRIPTION = 'desc'
        self.ATTACK_BONUS = 'attack_bonus'
