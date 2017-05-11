class MonsterFieldsSpecialAbilities(object):
    ROOT = 'trait'
    NAME = 'name'
    DESCRIPTION = 'text'

    def __init__(self):
        self.ROOT = 'trait'
        self.NAME = 'name'
        self.DESCRIPTION = 'text'


class MonsterFieldsActions(object):
    ROOT = 'action'
    NAME = 'name'
    DESCRIPTION = 'text'  # could be multiple nodes that need to be stitched together
    DAMAGE_DICE = 'attack'  # need to parse out this field
    DAMAGE_BONUS = 'attack'  # need to parse out this field
    ATTACK_BONUS = 'attack'  # need to parse out this field

    def __init__(self):
        self.ROOT = 'action'
        self.NAME = 'name'
        self.DESCRIPTION = 'text'  # could be multiple nodes that need to be stitched together
        self.DAMAGE_DICE = 'attack'  # need to parse out this field
        self.DAMAGE_BONUS = 'attack'  # need to parse out this field
        self.ATTACK_BONUS = 'attack'  # need to parse out this field


class MonsterLegendaryActions(object):
    ROOT = 'legendary'
    NAME = 'name'
    DESCRIPTION = 'text'  # could be multiple nodes that need to be stitched together
    DAMAGE_DICE = 'attack'  # need to parse out this field
    DAMAGE_BONUS = 'attack'  # need to parse out this field
    ATTACK_BONUS = 'attack'  # need to parse out this field

    def __init__(self):
        self.ROOT = 'legendary'
        self.NAME = 'name'
        self.DESCRIPTION = 'text'  # could be multiple nodes that need to be stitched together
        self.DAMAGE_DICE = 'attack'  # need to parse out this field
        self.DAMAGE_BONUS = 'attack'  # need to parse out this field
        self.ATTACK_BONUS = 'attack'  # need to parse out this field


class MonsterFieldsXml(object):
    MONSTER_TAG = "monster"
    ROOT_TAG = "compendium"

    """Basic Fields"""
    NAME = 'name'
    TYPE = 'type'
    SIZE = 'size'

    """Complex Fields"""
    SPECIAL_ABILITIES = MonsterFieldsSpecialAbilities()
    ACTIONS = MonsterFieldsActions()
    LEGENDARY_ACTIONS = MonsterLegendaryActions()

    def __init__(self):
        self.XML = "xml"
        self.JSON = "json"
        self.MONSTER_TAG = "monster"
        self.ROOT_TAG = "compendium"

        """Basic Fields"""
        self.NAME = 'name'
        self.TYPE = 'type'
        self.SIZE = 'size'

        """Complex Fields"""
        self.SPECIAL_ABILITIES = MonsterFieldsSpecialAbilities()
        self.ACTIONS = MonsterFieldsActions()
        self.LEGENDARY_ACTIONS = MonsterLegendaryActions()
