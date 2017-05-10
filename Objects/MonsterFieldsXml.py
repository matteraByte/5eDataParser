
class MonsterFieldsXml(object):
    def __init__(self):
        """Types"""
        self.XML = "xml"
        self.JSON = "json"

        """Basic Fields"""
        self.NAME = 'name'
        self.TYPE = 'type'
        self.SIZE = 'size'
        self.SPECIAL_ABILITIES = MonsterFieldsSpecialAbilities()
        self.ACTIONS = MonsterFieldsActions()


class MonsterFieldsSpecialAbilities(object):
    def __init__(self):
        """Special Abilities"""
        self.ROOT = 'trait'
        self.NAME = 'name'
        self.DESCRIPTION = 'text'
        # TODO: don't think traits need these
        # self.ATTACK_BONUS = 'attack_bonus'

class MonsterFieldsActions(object):
    def __init__(self):
        self.ROOT = 'action'
        self.NAME = 'name'
        self.DESCRIPTION = 'text'  # TODO: could have multiple <text> nodes
        self.DAMAGE_DICE = 'attack'  # TODO: need to parse out of this field
        self.ATTACK_BONUS = 'attack'  # TODO: need to parse out of this field
