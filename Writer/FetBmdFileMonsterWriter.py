import time
import os
from Helpers.RulesHelper import RulesHelper
from Parser.Monster import Monster, MonsterSpecialAbility

"""
5etools BMD
"""


class FetBmdBlobMonsterBuilder(object):
    """
    :type monster: Monster
    """
    def __init__(self, monster):
        self.post_date = time.strftime("%Y-%m-%d")
        self.monster = monster

    @staticmethod
    def get_line_break():
        return ">___\n"

    def build_post_info(self):
        # ___
        # >## Lich
        # >*Medium undead, any evil alignment*
        # >___
        post_info =  '___\n'
        post_info += f'>## {self.monster.name}\n'
        post_info += f'>{self.build_type_string()}\n'

        # TODO: remove
        # if self.monster.source != "":
        #     monster_source = self.monster.source.replace(" ", "-").lower()
        #     monster_source = monster_source.replace("'", "")
        #     monster_source = monster_source.replace(":", "")
        #     monster_source = monster_source.replace(",", "")
        #     post_info += ", " + monster_source

        post_info += '>___\n'

        return post_info

    @staticmethod
    def normalize_description(desc):
        description = desc

        #TODO: is this needed?
        # Double new line is the minimum for markup to display newlines on their own line
        description = description.replace("\n\n", "\n")
        description = description.replace("\n", "\n\n")

        # Indents result in a code block for markup. Instead use blockquote.
        description = description.replace("	", ">")

        # Sometimes there is a bullet that isn't actually a markup bullet - usually this happens in spell lists
        # make sure they have a space after them
        description = description.replace("• ", "* ")
        description = description.replace("•", "* ")

        return description

    def build_special_abilities(self):
        special_abilities_string = ""

        for monster_special_ability in self.monster.special_abilities:
            description = self.normalize_description(monster_special_ability.description)

            special_abilities_string += ">***" + \
                                        monster_special_ability.name + \
                                        ".*** " + \
                                        description + \
                                        "\n>\n"
        return special_abilities_string

    def build_actions(self):
        actions_string = ""
        for monster_action in self.monster.actions:
            if actions_string == "":
                actions_string += ">### Actions\n"
            #  end if

            description = self.normalize_description(monster_action.description)
            actions_string += ">***" +\
                              monster_action.name + \
                              ".*** " + \
                              description + \
                              "\n>\n"
            #  end for each
        return actions_string

    def build_reactions(self):
        reactions_string = ""
        for monster_reaction in self.monster.reactions:
            if reactions_string == "":
                reactions_string += ">### Reactions\n"
            # end if

            description = self.normalize_description(monster_reaction.description)
            reactions_string += ">***" + \
                                monster_reaction.name + \
                                ".*** " + \
                                description + \
                                "\n>\n"
            #  end for each
        return reactions_string

    def build_legendary_actions(self):
        if len(self.monster.legendary_actions) > 0:
            legendary_actions_string = ">### Legendary Actions\n"
            legendary_actions_string += ">" + self.monster.legendary_summary + "\n>\n"

            for monster_legendary_action in self.monster.legendary_actions:
                description = self.normalize_description(monster_legendary_action.description)
                legendary_actions_string += ">***" + \
                                            monster_legendary_action.name + \
                                            ".*** " + \
                                            description + \
                                            "\n>\n"

            return legendary_actions_string
        else:
            return ""

    def build_type_string(self):
        type_string = "*" + \
                      self.monster.size.capitalize() + \
                      " " + \
                      self.monster.type.lower()

        if self.monster.subtype != "":
            type_string += " (" + self.monster.subtype.lower() + ")"

        type_string += ", " + \
            self.monster.alignment.lower() + \
            "*"

        return type_string

    def build_armor_class_string(self):
        armor_class_string = ">- **Armor Class** " + self.monster.armor_class_with_description + "\n"
        return armor_class_string

    def build_speed_string(self):
        speed_string = ">- **Speed** " + self.monster.speed_with_description + "\n"
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

        stat_scores_string = ">___\n" \
                             ">|STR|DEX|CON|INT|WIS|CHA|\n" + \
                             ">|:---:|:---:|:---:|:---:|:---:|:---:|\n" + \
                             ">|" + str(strength_score) + " (" + strength_bonus_desc + ")" + \
                             "|" + str(dexterity_score) + " (" + dexterity_bonus_desc + ")" + \
                             "|" + str(constitution_score) + " (" + constitution_bonus_desc + ")" + \
                             "|" + str(intelligence_score) + " (" + intelligence_bonus_desc + ")" + \
                             "|" + str(wisdom_score) + " (" + wisdom_bonus_desc + ")" + \
                             "|" + str(charisma_score) + " (" + charisma_bonus_desc + ")" + \
                             "|" + "\n>___\n"
        return stat_scores_string

    def build_saving_throws_string(self):
        saving_throws_string = ""
        if self.monster.saving_throws != "":
            saving_throws_string += ">- **Saving Throws** "
            saving_throws_string += self.monster.saving_throws + "\n"
        return saving_throws_string

    def build_skills_string(self):
        skills_string = ""
        if self.monster.skills != "":
            skills_string += ">- **Skills** "
            skills_string += self.monster.skills + "\n"
        return skills_string

    def build_senses_string(self):
        senses_string = ""
        if self.monster.senses != "":
            senses_string += ">- **Senses** "
            senses_string += self.monster.senses + "\n"
        return senses_string

    def build_languages_string(self):
        languages_string = ""
        if self.monster.languages != "":
            languages_string += ">- **Languages** "
            languages_string += self.monster.languages + "\n"
        return languages_string

    def build_challenge_rating_string(self):
        xp = RulesHelper.get_xp_for_challenge_rating(self.monster.challenge_rating)
        challenge_rating_string = ">- **Challenge** " + \
                                  self.monster.challenge_rating
        if xp != "":
            challenge_rating_string += " (" + xp + " XP)"

        challenge_rating_string += "\n"
        return challenge_rating_string

    def build_hit_points_string(self):
        hit_points_string = ">- **Hit Points** " + self.monster.hit_points_with_hit_dice + "\n"
        return hit_points_string

    def build_condition_immunities_string(self):
        condition_immunities_string = ""
        if self.monster.condition_immunities != "":
            condition_immunities_string = ">- **Condition Immunities** " + self.monster.condition_immunities + "\n"
        return condition_immunities_string

    def build_damage_immunities_string(self):
        damage_immunities_string = ""
        if self.monster.damage_immunities != "":
            damage_immunities_string = ">- **Damage Immunities** " + self.monster.damage_immunities + "\n"
        return damage_immunities_string

    def build_damage_resistances_string(self):
        damage_resistances_string = ""
        if self.monster.damage_resistances != "":
            damage_resistances_string = ">- **Damage Resistances** " + self.monster.damage_resistances + "\n"
        return damage_resistances_string

    def build_damage_vulnerabilities_string(self):
        damage_vulnerabilities_string = ""
        if self.monster.damage_vulnerabilities != "":
            damage_vulnerabilities_string = ">- **Damage Vulnerabilities** " + \
                                            self.monster.damage_vulnerabilities + "\n"
        return damage_vulnerabilities_string

    def build_all_post(self):
        post_all = ""
        post_all += self.build_post_info()
        post_all += self.build_armor_class_string()
        post_all += self.build_hit_points_string()
        post_all += self.build_speed_string()
        post_all += self.build_stat_scores_string()
        post_all += self.build_saving_throws_string()
        post_all += self.build_skills_string()
        post_all += self.build_damage_vulnerabilities_string()
        post_all += self.build_damage_resistances_string()
        post_all += self.build_damage_immunities_string()
        post_all += self.build_condition_immunities_string()
        post_all += self.build_senses_string()
        post_all += self.build_languages_string()
        post_all += self.build_challenge_rating_string()
        post_all += self.get_line_break()
        post_all += self.build_special_abilities()  # traits
        post_all += self.build_actions()
        post_all += self.build_reactions()
        post_all += self.build_legendary_actions()

        return post_all


class FetBmdFileMonsterWriter(object):
    def __init__(self, directory_path, list_of_monsters):
        """
        :type list_of_monsters: list of Monster
        """
        self.directory_path = directory_path
        self.list_of_monsters = list_of_monsters

    def write_monsters_to_files(self):
        for monster in self.list_of_monsters:
            blob_builder = FetBmdBlobMonsterBuilder(monster)
            monster_name = blob_builder.monster.name.lower()
            post_date = blob_builder.post_date
            file_name = post_date + "-" + monster_name.replace(" ", "-") + ".markdown"
            file_name = file_name.replace("/", "-")
            file_name = file_name.replace("'", "")
            file_name = file_name.replace(",", "")
            full_file_path = os.path.join(self.directory_path, file_name)
            file = open(full_file_path, "w+")
            file.write(blob_builder.build_all_post())
            file.close()
