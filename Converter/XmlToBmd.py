import os
from Writer.BMDFileMonsterWriter import BMDFileMonsterWriter as FileWriter
from Parser.XmlMonsterFileParser import XmlMonsterFileParser as FileParser


class XmlToBmd(object):

    @staticmethod
    def convert(file_path, output_directory):
        file_parser = FileParser(file_path)
        list_of_monsters = []

        if os.path.isfile(file_path):
            list_of_monsters = file_parser.get_monster_list_from_file()
        else:
            """TODO: iterate through xml files in directory"""

        file_writer = FileWriter(output_directory, list_of_monsters)
        file_writer.write_monsters_to_files()
