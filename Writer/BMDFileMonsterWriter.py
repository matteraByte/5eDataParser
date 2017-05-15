import time
import os
from Helpers.RulesHelper import RulesHelper
from Parser.Monster import Monster, MonsterSpecialAbility


class BMDBlobMonsterBuilder(object):
    """
    :type monster: Monster
    """
    def __init__(self, monster):
        self.post_date = time.strftime("%Y-%m-%d")
        self.monster = monster

    def build_post_info(self):
        # ---
        # layout: post
        # title: "Aboleth"
        # date: 2016-02-29
        # tags: [large, aberration, cr10, monster-manual]
        # ---
        post_info =  "---\n" \
                     "layout: post\n"
        post_info += "title: \"" + self.monster.name + "\"\n"
        post_info += "date: " + self.post_date + "\n"
        post_info += "tags: [" + self.monster.size.lower() + ", " + \
                     self.monster.type.lower() + ", " +\
                     "cr" + str(self.monster.challenge_rating)
        if self.monster.source != "":
            monster_source = self.monster.source.replace(" ", "-").lower()
            monster_source = monster_source.replace("'", "")
            monster_source = monster_source.replace(":", "")
            monster_source = monster_source.replace(",", "")
            post_info += ", " + monster_source

        post_info += "]\n"
        post_info += "---\n\n"

        return post_info

    def build_special_abilities(self):
        special_abilities_string = ""

        for monster_special_ability in self.monster.special_abilities:
            description = monster_special_ability.description
            # TODO: Fix this hokey replace with some regex
            description = description.replace("\n\n", "\n")
            description = description.replace("\n", "\n\n")

            special_abilities_string += "***" + \
                                        monster_special_ability.name + \
                                        ".*** " + \
                                        description + \
                                        "\n\n"
        return special_abilities_string

    def build_actions(self):
        actions_string = ""
        for monster_action in self.monster.actions:
            if actions_string == "":
                actions_string += "**Actions**\n\n"
            #  end if
            description = monster_action.description
            # TODO: Fix this hokey replace with some regex
            description = description.replace("\n\n", "\n")
            description = description.replace("\n", "\n\n")
            actions_string += "***" +\
                              monster_action.name + \
                              ".*** " + \
                              description + \
                              "\n\n"
            #  end for each
        return actions_string

    def build_legendary_actions(self):
        legendary_actions_string = ""
        for monster_legendary_action in self.monster.legendary_actions:
            if legendary_actions_string == "":
                legendary_actions_string += "**Legendary Actions**"
                #  TODO: Include the creature's name in the legendary actions string like "the vampire" or "Strahd"
                legendary_nickname = self.monster.legendary_nickname
                if legendary_nickname == "":
                    legendary_nickname = "The " + self.monster.name.lower()
                legendary_actions_string += legendary_nickname + \
                                            " may use 3 legendary actions, choosing from the options below. Only "\
                                            "one legendary action option can be used at a time and only at the end " \
                                            "of another creature’s turn. " + \
                                            legendary_nickname + " regains spent legendary actions " \
                                            "at the start of its turn." \
                                            "\n\n"
            #  end if
            description = monster_legendary_action.description
            # TODO: Fix this hokey replace with some regex
            description = description.replace("\n\n", "\n")
            description = description.replace("\n", "\n\n")
            legendary_actions_string += "***" + \
                                        monster_legendary_action.name + \
                                        ".*** " + \
                                        description + \
                                        "\n\n"
            #  end for each
        return legendary_actions_string

    def build_type_string(self):
        type_string = "**" + \
                      self.monster.size.capitalize() + \
                      " " + \
                      self.monster.type.lower()

        if self.monster.subtype != "":
            type_string += " (" + self.monster.subtype.lower() + ")"

        type_string += ", " + \
            self.monster.alignment.lower() + \
            "**" + "\n\n"

        return type_string

    def build_armor_class_string(self):
        armor_class_string = "**Armor Class** " + self.monster.armor_class_with_description + "\n\n"
        return armor_class_string

    def build_speed_string(self):
        speed_string = "**Speed** " + self.monster.speed_with_description + "\n\n"
        return speed_string

    def build_stat_scores_string(self):
        strength_score = self.monster.strength
        dexterity_score = self.monster.dexterity
        wisdom_score = self.monster.wisdom
        intelligence_score = self.monster.intelligence
        constitution_score = self.monster.constitution
        charisma_score = self.monster.charisma

        strength_bonus_desc = RulesHelper.get_bonus_description_from_score(strength_score)
        dexterity_bonus_desc = RulesHelper.get_bonus_description_from_score(dexterity_score)
        wisdom_bonus_desc = RulesHelper.get_bonus_description_from_score(wisdom_score)
        charisma_bonus_desc = RulesHelper.get_bonus_description_from_score(charisma_score)
        constitution_bonus_desc = RulesHelper.get_bonus_description_from_score(constitution_score)
        intelligence_bonus_desc = RulesHelper.get_bonus_description_from_score(intelligence_score)

        stat_scores_string = "|   STR   |   DEX   |   CON   |   INT   |   WIS   |   CHA   |\n" + \
                             "|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|\n" + \
                             "| " + str(strength_score) + " (" + strength_bonus_desc + ") " + \
                             "| " + str(dexterity_score) + " (" + dexterity_bonus_desc + ") " + \
                             "| " + str(constitution_score) + " (" + constitution_bonus_desc + ") " + \
                             "| " + str(intelligence_score) + " (" + intelligence_bonus_desc + ") " + \
                             "| " + str(wisdom_score) + " (" + wisdom_bonus_desc + ") " + \
                             "| " + str(charisma_score) + " (" + charisma_bonus_desc + ") " + \
                             "|" + "\n\n"
        return stat_scores_string

    def build_saving_throws_string(self):
        saving_throws_string = ""
        if self.monster.saving_throws != "":
            saving_throws_string += "**Saving Throws** "
            saving_throws_string += self.monster.saving_throws + "\n\n"
        return saving_throws_string

    def build_skills_string(self):
        skills_string = ""
        if self.monster.skills != "":
            skills_string += "**Skills** "
            skills_string += self.monster.skills + "\n\n"
        return skills_string

    def build_senses_string(self):
        senses_string = ""
        if self.monster.senses != "":
            senses_string += "**Senses** "
            senses_string += self.monster.senses + "\n\n"
        return senses_string

    def build_languages_string(self):
        languages_string = ""
        if self.monster.languages != "":
            languages_string += "**Languages** "
            languages_string += self.monster.languages + "\n\n"
        return languages_string

    def build_challenge_rating_string(self):
        challenge_rating_string = "**Challenge** " + \
                                  str(self.monster.challenge_rating) + \
                                  " " + \
                                  RulesHelper.get_xp_for_challenge_rating(self.monster.challenge_rating) + "\n\n"
        return challenge_rating_string

    def build_hit_points_string(self):
        hit_points_string = "**Hit Points** " + self.monster.hit_points_with_hit_dice + "\n\n"
        return hit_points_string

    def build_all_post(self):
        post_all = ""
        post_all += self.build_post_info()
        post_all += self.build_type_string()
        post_all += self.build_armor_class_string()
        post_all += self.build_hit_points_string()
        post_all += self.build_speed_string()
        post_all += self.build_stat_scores_string()
        post_all += self.build_saving_throws_string()
        post_all += self.build_skills_string()
        post_all += self.build_senses_string()
        post_all += self.build_languages_string()
        post_all += self.build_challenge_rating_string()
        post_all += self.build_special_abilities()  # traits
        post_all += self.build_actions()
        post_all += self.build_legendary_actions()

        return post_all


class BMDFileMonsterWriter(object):
    def __init__(self, directory_path, list_of_monsters):
        """
        :type list_of_monsters: list of Monster
        """
        self.directory_path = directory_path
        self.list_of_monsters = list_of_monsters

    def write_monsters_to_files(self):
        for monster in self.list_of_monsters:
            blob_builder = BMDBlobMonsterBuilder(monster)
            monster_name = blob_builder.monster.name.lower()
            post_date = blob_builder.post_date
            file_name = post_date + "-" + monster_name.replace(" ", "-") + ".markdown"
            file_name = file_name.replace("/", "-")
            full_file_path = os.path.join(self.directory_path, file_name)
            file = open(full_file_path, "w+")
            file.write(blob_builder.build_all_post())
            file.close()