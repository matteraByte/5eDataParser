class MonsterFieldsSpecialAbilities(object):
    ROOT = 'trait'
    NAME = 'name'
    DESCRIPTION = 'text'


class MonsterFieldsActions(object):
    ROOT = 'action'
    NAME = 'name'
    DESCRIPTION = 'text'  # could be multiple nodes that need to be stitched together
    DAMAGE_DICE = 'attack'
    DAMAGE_BONUS = 'attack'
    ATTACK_BONUS = 'attack'


class MonsterFieldsReactions(object):
    ROOT = 'reaction'
    NAME = 'name'
    DESCRIPTION = 'text'  # could be multiple nodes that need to be stitched together

class MonsterLegendaryActions(object):
    ROOT = 'legendary'
    NAME = 'name'
    DESCRIPTION = 'text'  # could be multiple nodes that need to be stitched together
    DAMAGE_DICE = 'attack'
    DAMAGE_BONUS = 'attack'
    ATTACK_BONUS = 'attack'


class MonsterFieldsXml(object):
    MONSTER_TAG = "monster"
    ROOT_TAG = "compendium"

    SOURCE = "type"

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
    SPEED = "speed"
    ARMOR_CLASS = "ac"
    ALIGNMENT = "alignment"
    DAMAGE_VULNERABILITIES = "vulnerable"
    DAMAGE_RESISTANCES = "resist"
    DAMAGE_IMMUNITIES = "immune"
    CONDITION_IMMUNITIES = "conditionImmune"

    STRENGTH = "str"
    WISDOM = "wis"
    CONSTITUTION = "con"
    INTELLIGENCE = "int"
    DEXTERITY = "dex"
    CHARISMA = "cha"

    """Complex Fields"""
    SPECIAL_ABILITIES = MonsterFieldsSpecialAbilities()
    ACTIONS = MonsterFieldsActions()
    REACTIONS = MonsterFieldsReactions()
    LEGENDARY_ACTIONS = MonsterLegendaryActions()
