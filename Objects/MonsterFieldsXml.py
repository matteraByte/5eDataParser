class MonsterFieldsSpecialAbilities(object):
    ROOT = 'trait'
    NAME = 'name'
    DESCRIPTION = 'text'


class MonsterFieldsActions(object):
    ROOT = 'action'
    NAME = 'name'
    DESCRIPTION = 'text'  # could be multiple nodes that need to be stitched together
    DAMAGE_DICE = 'attack'  # need to parse out this field
    DAMAGE_BONUS = 'attack'  # need to parse out this field
    ATTACK_BONUS = 'attack'  # need to parse out this field


class MonsterLegendaryActions(object):
    ROOT = 'legendary'
    NAME = 'name'
    DESCRIPTION = 'text'  # could be multiple nodes that need to be stitched together
    DAMAGE_DICE = 'attack'  # need to parse out this field
    DAMAGE_BONUS = 'attack'  # need to parse out this field
    ATTACK_BONUS = 'attack'  # need to parse out this field


class MonsterFieldsXml(object):
    MONSTER_TAG = "monster"
    ROOT_TAG = "compendium"

    """Basic Fields"""
    NAME = "name"
    TYPE = "type"
    SIZE = "size"
    HIT_POINTS = "hp"
    CHALLENGE_RATING = "cr"
    LANGUAGES = "languages"
    SENSES = "senses"
    SKILLS = "skill"
    SAVING_THROWS = "save"

    """Complex Fields"""
    SPECIAL_ABILITIES = MonsterFieldsSpecialAbilities()
    ACTIONS = MonsterFieldsActions()
    LEGENDARY_ACTIONS = MonsterLegendaryActions()
