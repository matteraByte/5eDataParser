import unittest
import time
from Parser.Monster import Monster, \
    MonsterSpecialAbility as SpecialAbility, \
    MonsterAction as Action,\
    MonsterLegendaryAction as LegendaryAction
from Writer.BMDFileMonsterWriter import BMDFileMonsterWriter as FileWriter, BMDBlobMonsterBuilder as BlobBuilder


class BMDFileMonsterWriterTest(unittest.TestCase):

    def setUp(self):
        self.monster = Monster("Testermon")
        self.monster.size = "Large"
        self.monster.type = "Aborigonize"
        self.monster.challenge_rating = 9

        self.special_ability_1 = SpecialAbility()
        self.special_ability_1.name = "Evil Snot"
        self.special_ability_1.description = "When a description is not a description, it is a test."

        self.special_ability_2 = SpecialAbility()
        self.special_ability_2.name = "Hideous Collar Bones"
        self.special_ability_2.description = "Creatures within 20 feet of the Testermon that can see its many " \
                                             "collar bones must succeed a DC 16 Wisdom saving throw or be paralyzed " \
                                             "for 1 minute. Creatures can repeat this saving throw only by speaking " \
                                             "in baby voice."

        self.monster.special_abilities.append(self.special_ability_1)
        self.monster.special_abilities.append(self.special_ability_2)

        self.action_1 = Action()
        self.action_1.name = "Action Jackson"
        self.action_1.description = "He needs no description, Son."
        self.action_2 = Action()
        self.action_2.name = "Some Action Attack"
        self.action_2.description = "So good and attacky. Test attack 1d6+4 slashing damage."

        self.monster.actions.append(self.action_1)
        self.monster.actions.append(self.action_2)

        self.legendary_action_1 = LegendaryAction()
        self.legendary_action_1.name = "Legendary One"
        self.legendary_action_1.description = "Like oh so special."
        self.legendary_action_2 = LegendaryAction()
        self.legendary_action_2.name = "Another Special Thing I Can Do (Costs 2 Actions)"
        self.legendary_action_2.description = "So Cool."

        self.monster.legendary_actions.append(self.legendary_action_1)
        self.monster.legendary_actions.append(self.legendary_action_2)

        self.monster.alignment = "Lawful Good"
        self.monster.armor_class_with_description = "17 (natural armor)"
        self.monster.speed_with_description = "10 ft., swim 40 ft."

        self.monster.strength = 21
        self.monster.dexterity = 9
        self.monster.constitution = 15
        self.monster.intelligence = 18
        self.monster.wisdom = 15
        self.monster.charisma = 18

        self.blob_builder = BlobBuilder(self.monster)

    def test_build_post_info(self):
        expected = "---\n" \
                   "layout: post\n" \
                   "title: \"Testermon\"\n" \
                   "date: " + time.strftime("%Y-%m-%d") + "\n" \
                   "tags: [large, aborigonize, cr9]\n" \
                   "---\n"
        post_info = self.blob_builder.build_post_info()
        self.assertEquals(post_info, expected)

    def test_build_special_abilities(self):
        expected =  "***" + self.special_ability_1.name + ".*** " + self.special_ability_1.description + "\n\n"
        expected += "***" + self.special_ability_2.name + ".*** " + self.special_ability_2.description + "\n\n"
        result = self.blob_builder.build_special_abilities()
        self.assertEquals(result, expected)

    def test_build_actions(self):
        expected = "**Actions**" \
                   "\n\n"
        expected += "***" + self.action_1.name + ".*** " + self.action_1.description + "\n\n"
        expected += "***" + self.action_2.name + ".*** " + self.action_2.description + "\n\n"
        result = self.blob_builder.build_actions()
        self.assertEquals(result, expected)

    def test_build_legendary_actions(self):
        expected =  "**Legendary Actions**"
        expected += "The testermon may use 3 legendary actions, choosing from the options below. Only one legendary " \
                    "action option can be used at a time and only at the end of another creature’s turn. " \
                    "The testermon regains spent legendary actions at the start of its turn." \
                    "\n\n"

        expected += "***" + self.legendary_action_1.name + ".*** " + self.legendary_action_1.description + "\n\n"
        expected += "***" + self.legendary_action_2.name + ".*** " + self.legendary_action_2.description + "\n\n"
        result = self.blob_builder.build_legendary_actions()
        self.assertEquals(result, expected)

    def test_build_type_string(self):
        expected = "**Large aborigonize, lawful good**"
        result = self.blob_builder.build_type_string()
        self.assertEquals(result, expected)

    def test_build_armor_class_string(self):
        expected = "**Armor Class** 17 (natural armor)"
        result = self.blob_builder.build_armor_class_string()
        self.assertEquals(result, expected)

    def test_build_speed_string(self):
        expected = "**Speed** 10 ft., swim 40 ft."
        result = self.blob_builder.build_speed_string()
        self.assertEquals(result, expected)

    def test_build_stat_scores(self):
        expected = "|   STR   |   DEX   |   CON   |   INT   |   WIS   |   CHA   |\n" \
                   "|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|\n" \
                   "| 21 (+5) | 9 (−1) | 15 (+2) | 18 (+4) | 15 (+2) | 18 (+4) |"
        result = self.blob_builder.build_stat_scores_string()
        self.assertEquals(result, expected)
