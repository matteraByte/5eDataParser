# 5eDataParser

## Description
Parsers, Writers, and Converters of 5e data to and from different formats (xml, json, markdown, ...)

## Summary
There is a lot of 5e data on the web. The SRD opened a new world of info to be utilized by developers, dungeon masters, and players. Content sourced from the community for various programs. Although some formats are more popular than others, there isn't a set standard. I wanted to be able to take data from various sources describing monsters, spells, items, etc. and be able to write them to other formats. This is an attempt at a parser with templates and converters for various formats.

It is my hope that these can be expanded upon by the community to add more formats and also allow developers to use the parsers to read in files and use the data in their own applications with miminal effort.

## Requirements
Python 3.5 or greater

## XML to Markdown Converter
The XML to Markdown converter usage is as follows:
```bash
python ConvertXmlToBestiaryMarkdown.py InputDirectoryOrFile OutputDirectory
```
Contents of Homebrew.xml:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<compendium version="5">
	<monster>
		<name>Gnome Chompski</name>
		<size>S</size>
		<type>humanoid (gnome), homebrew</type>
		<alignment>lawful good</alignment>
		<ac>10</ac>
		<hp>17 (5d6)</hp>
		<speed>30 ft.</speed>
		<str>10</str>
		<dex>10</dex>
		<con>10</con>
		<int>10</int>
		<wis>14</wis>
		<cha>11</cha>
		<skill>Medicine +4, Religion +2</skill>
		<passive>12</passive>
		<languages>Common, Draconic, Gnomish, Goblin</languages>
		<cr>1/4</cr>
		<trait>
			<name>Spellcasting</name>
			<text>Chompski is a 1st-level spellcaster. His spellcasting ability is Wisdom (spell save DC 12, +4 to hit with spell attacks). Chompski has following cleric spells prepared: </text>
			<text />
			<text>• Cantrips (at will): light, sacred flame, thaumaturgy</text>
			<text>• 1st level (3 slots): bless, cure wounds, sanctuary</text>
		</trait>
		<action>
			<name>Turn Undead (1/short rest)</name>
			<text>Chompski presents his holy Symbol and speaks a prayer censuring the Undead. Each Undead that can see or hear Chompski within 30 feet of you must make a DC 12 Wisdom saving throw. If the creature fails its saving throw, it is turned for 1 minute or until it takes any damage.</text>
			<text>A turned creature must spend its turns trying to move as far away from you as it can, and it can't willingly move to a space within 30 feet of you. It also can't take reactions. For its action, it can use only the Dash action or try to escape from an effect that prevents it from moving. If there's nowhere to move, the creature can use the Dodge action.</text>
		</action>
		<action>
			<name>Club</name>
			<text>Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 2 (1d4) bludgeoning damage.</text>
			<attack>Club|2|1d4</attack>
		</action>
		<spells>light, sacred flame, thaumaturgy, bless, cure wounds, sanctuary</spells>
		<slots>3,0,0,0,0,0,0,0,0</slots>
	</monster>
	<monster>
		<name>Phatrat</name>
		<size>M</size>
		<type>beast, homebrew</type>
		<alignment>unaligned</alignment>
		<ac>13</ac>
		<hp>16 (2d6+9)</hp>
		<speed>30 ft.</speed>
		<str>7</str>
		<dex>16</dex>
		<con>12</con>
		<int>2</int>
		<wis>10</wis>
		<cha>4</cha>
		<senses>darkvision 60 ft.</senses>
		<passive>10</passive>
		<cr>1/4</cr>
		<action>
			<name>Bite</name>
			<text>Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) piercing damage. If the target is a creature, it must succeed on a DC 10 Constitution saving throw or contract a disease. Until the disease is cured, the target can't regain hit points except by magical means, and the target's hit point maximum decreases by 3 (1d6) every 24 hours. If the target's hit point maximum drops to 0 as a result of this disease, the target dies.</text>
			<attack>Bite|5|1d4+2</attack>
		</action>
	</monster>
	<monster>
		<name>Goblin Commoner</name>
		<size>S</size>
		<type>humanoid (goblinoid), homebrew</type>
		<alignment>neutral evil</alignment>
		<ac>15 (leather armor, shield)</ac>
		<hp>3 (1d6)</hp>
		<speed>30 ft.</speed>
		<str>8</str>
		<dex>12</dex>
		<con>10</con>
		<int>10</int>
		<wis>8</wis>
		<cha>8</cha>
		<skill>Stealth +6</skill>
		<senses>darkvision 60 ft.</senses>
		<passive>9</passive>
		<languages>Common, Goblin</languages>
		<cr>1/4</cr>
		<trait>
			<name>Nimble Escape</name>
			<text>The goblin commoner can take the Disengage or Hide action as a bonus action on each of its turns.</text>
		</trait>
		<action>
			<name>Scimitar</name>
			<text>Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) slashing damage.</text>
			<attack>|4|1d6+2</attack>
		</action>
		<action>
			<name>Shortbow</name>
			<text>Ranged Weapon Attack: +3 to hit, range 80/320 ft., one target. Hit: 4 (1d6 + 1) piercing damage.</text>
			<attack>|4|1d6+2</attack>
		</action>
	</monster>
	<monster>
		<name>Sergeant Gobbypants</name>
		<size>M</size>
		<type>humanoid (goblinoid), homebrew</type>
		<alignment>lawful evil</alignment>
		<ac>19 (splint, shield)</ac>
		<hp>18 (3d8+4)</hp>
		<speed>30 ft.</speed>
		<str>15</str>
		<dex>12</dex>
		<con>12</con>
		<int>10</int>
		<wis>10</wis>
		<cha>9</cha>
		<senses>darkvision 60 ft.</senses>
		<passive>10</passive>
		<languages>Common, Goblin</languages>
		<cr>1</cr>
		<trait>
			<name>Special Equipment</name>
			<text>The Sergeant has a potion of healing and two vials of antitoxin</text>
		</trait>
		<trait>
			<name>Martial Advantage</name>
			<text>Once per turn, the Sergeant can deal an extra 7 (2d6) damage to a creature it hits with a weapon attack if that creature is within 5 ft. of an ally of the Sergeant that isn't incapacitated.</text>
			<attack>Martial Advantage||2d6</attack>
		</trait>
		<action>
			<name>Longsword</name>
			<text>Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) slashing damage, or 6 (1d10 + 1) slashing damage if used with two hands.</text>
			<attack>|4|1d8+2</attack>
		</action>
		<action>
			<name>Longbow</name>
			<text>Ranged Weapon Attack: +4 to hit, range 150/600 ft., one target. Hit: 6 (1d8 + 2) piercing damage.</text>
			<attack>|4|1d8+2</attack>
		</action>
	</monster>
</compendium>
```
You can specify an individual file or a directory that the converter will cycle through and grab all the files from.
```bash
python ConvertXmlToBestiaryMarkdown.py /DnD/Homebrew.xml /DnD/monstermarkdown
```
The resulting files in the monstermarkdown directory start with the date. This choice was made so they could be used with Jekyll:
```
2017-05-28-gnome-chompski.markdown
2017-05-28-goblin-commoner.markdown
2017-05-28-phatrat.markdown
2017-05-28-sergeant-gobbypants.markdown
```

And the contents of a markdown file
```markdown
---
layout: post
title: "Sergeant Gobbypants"
date: 2017-05-28
tags: [medium, humanoid, cr1, homebrew]
---

**Medium humanoid (goblinoid), lawful evil**

**Armor Class** 19 (splint, shield)

**Hit Points** 18 (3d8+4)

**Speed** 30 ft.

|   STR   |   DEX   |   CON   |   INT   |   WIS   |   CHA   |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| 15 (+2) | 12 (+1) | 12 (+1) | 10 (0) | 10 (0) | 9 (-1) |

**Senses** darkvision 60 ft.

**Languages** Common, Goblin

**Challenge** 1 (200 XP)

***Special Equipment.*** The Sergeant has a potion of healing and two vials of antitoxin

***Martial Advantage.*** Once per turn, the Sergeant can deal an extra 7 (2d6) damage to a creature it hits with a weapon attack if that creature is within 5 ft. of an ally of the Sergeant that isn't incapacitated.

**Actions**

***Longsword.*** Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) slashing damage, or 6 (1d10 + 1) slashing damage if used with two hands.

***Longbow.*** Ranged Weapon Attack: +4 to hit, range 150/600 ft., one target. Hit: 6 (1d8 + 2) piercing damage.
```
[Here](https://matterabyte.github.io/bestiary/creatures/sergeant-gobbypants) is what it looks like after a build with Jekyll in the Bestiary.

A Demo Bestiary with converted XML from the SRD and the example homebrew available is available [here](https://matterabyte.github.io/bestiary/)

## Known issues
- Could be errors on fields that arent ints or other conversion things `<int>l</int>`. Yeah that happened.
- Same name collisions - will overwrite previous entry

## Decisions
Changed formatting on code markdown - tabs are blockquote instead of code.

## To do:
- Generate Monster guid based on source and name
- Option to have spells in markdown link to spell grimoire
- Add tags to filter by source

## Project Status
### Converters
| Input Format  | Output Format | Data Type  | Status |
| ------------- |:-------------:|:-----:|--------:|
| xml | markdown | monster | done |
| xml | statblock | monster | not started |

### Parsers
| Format        | App           | Data Type  | Status |
| ------------- |:-------------:|:-----:|--------:|
| xml | Fight Club | monster | done |
| json | 5e API, DM Tools | monster | incomplete |

### Writers
| Format        | App           | Data Type  | Status |
| ------------- |:-------------:|:-----:|--------:|
| markdown | Bestiary | monster | done |
| json | 5e API, DM Tools Android 5e | monster | incomplete |
| statblock | 5e Statblock styling | monster | not started |
| xml | Fight Club | monster | not started |
