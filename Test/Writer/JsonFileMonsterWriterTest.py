from Parser.JsonFileMonsterParser import JsonFileMonsterParser
from Writer.JsonFileMonsterWriter import JsonFileMonsterWriter, JsonBlobMonsterBuilder

fileLocation = "../../Resources/DMTools/5e-SRD-Monsters[DMTOOLS].json"
decoded = []

file_parser = JsonFileMonsterParser(fileLocation)
monster_list = file_parser.get_monster_list()

json_builder = JsonBlobMonsterBuilder(monster_list)

print(json_builder.build_json_blob())