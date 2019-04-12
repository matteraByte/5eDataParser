from os import listdir
from os.path import isfile, join, isdir
from Writer.FetBmdFileMonsterWriter import FetBmdFileMonsterWriter as FileWriter
from Parser.XmlMonsterFileParser import XmlMonsterFileParser as FileParser


class XmlToBmd(object):

    @staticmethod
    def convert(file_or_dir_path, output_directory):
        full_list_of_monsters = []

        if isfile(file_or_dir_path):
            file_parser = FileParser(file_or_dir_path)
            full_list_of_monsters = file_parser.get_monster_list_from_file(file_or_dir_path)
        else:
            print("Input option is not a file... checking if directory...", file_or_dir_path)
            if isdir(file_or_dir_path):
                print("Yeah... it's a directory. Gathering files in directory...")
                file_path_list = [f for f in listdir(file_or_dir_path) if isfile(join(file_or_dir_path, f))]

                for file_path in file_path_list:
                    print("Grabbing monsters for file: " + file_path)
                    full_file_path = join(file_or_dir_path, file_path)
                    file_parser = FileParser(full_file_path)
                    full_list_of_monsters.extend(file_parser.get_monster_list_from_file(full_file_path))
            else:
                print("Error: Input is not a file or a directory. Does directory exist?")

        if isdir(output_directory):
            if len(full_list_of_monsters) > 0:
                print("Writing " + str(len(full_list_of_monsters)) + " monsters to directory: " + output_directory)
                file_writer = FileWriter(output_directory, full_list_of_monsters)
                file_writer.write_monsters_to_files()
            else:
                print("No monsters found to write. Exiting.")
        else:
            print("Specified output path is not a directory: ", output_directory)
