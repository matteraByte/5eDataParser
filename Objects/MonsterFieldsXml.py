
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
        self.LEGENDARY_ACTIONS = MonsterLegendaryActions()


class MonsterFieldsSpecialAbilities(object):
    def __init__(self):
        """Special Abilities"""
        self.ROOT = 'trait'
        self.NAME = 'name'
        self.DESCRIPTION = 'text'


class MonsterFieldsActions(object):
    def __init__(self):
        self.ROOT = 'action'
        self.NAME = 'name'
        self.DESCRIPTION = 'text'  # could be multiple nodes that need to be stitched together
        self.DAMAGE_DICE = 'attack'  # need to parse out this field
        self.DAMAGE_BONUS = 'attack'  # need to parse out this field
        self.ATTACK_BONUS = 'attack'  # need to parse out this field


class MonsterLegendaryActions(object):
    def __init__(self):
        self.ROOT = 'legendary'
        self.NAME = 'name'
        self.DESCRIPTION = 'text'  # could be multiple nodes that need to be stitched together
        self.DAMAGE_DICE = 'attack'  # need to parse out this field
        self.DAMAGE_BONUS = 'attack'  # need to parse out this field
        self.ATTACK_BONUS = 'attack'  # need to parse out this field

