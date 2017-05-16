import math


class RulesHelper(object):
    XP_BY_CR = {
        "0": "10",
        "1/8": "25",
        "1/4": "50",
        "1/2": "100",
        "1": "200",
        "2": "450",
        "3": "700",
        "4": "1,100",
        "5": "1,800",
        "6": "2,300",
        "7": "2,900",
        "8": "3,900",
        "9": "5,000",
        "10": "5,900",
        "11": "7,200",
        "12": "8,400",
        "13": "10,000",
        "14": "11,500",
        "15": "13,000",
        "16": "15,000",
        "17": "18,000",
        "18": "20,000",
        "19": "22,000",
        "20": "25,000",
        "21": "33,000",
        "22": "41,000",
        "23": "50,000",
        "24": "62,000",
        "25": "75,000",
        "26": "90,000",
        "27": "105,000",
        "28": "120,000",
        "29": "135,000",
        "30": "155,000",
    }

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
        """:type challenge_rating str"""
        try:
            xp = RulesHelper.XP_BY_CR[challenge_rating]
        except KeyError:
            xp = ""
        return xp
