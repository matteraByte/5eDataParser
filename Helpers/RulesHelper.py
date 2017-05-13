import math


class RulesHelper(object):
    @staticmethod
    def get_bonus_from_score(stat_score):
        """:rtype: int"""
        return math.floor((stat_score - 10) / 2)

    @staticmethod
    def get_bonus_description_from_score(stat_score):
        """:rtype: str"""
        stat_score = RulesHelper.get_bonus_from_score(stat_score)
        if stat_score > 0:
            return "+" + str(stat_score)
        else:
            return "" + str(stat_score)

    @staticmethod
    def get_xp_for_challenge_rating(challenge_rating):
        """:type challenge_rating int"""
        xp = ""
        # TODO: Implement
        return xp
