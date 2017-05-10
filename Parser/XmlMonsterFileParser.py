import json
import logging
import logging.config
import definitions
from Parser.Monster import Monster
from Parser.XmlMonsterAttributeParser import XmlMonsterAttributeParser

logging.config.fileConfig(definitions.LOGGING_CONFIG_PATH)
logger = logging.getLogger('basicLog')


class XmlMonsterFileParser(object):
    def __init__(self, file_path=""):
        self.file_path = file_path
        self.blob_parser = None

    def get_monster_list_from_file(self, file_path=""):
        if file_path != "":
            self.file_path = file_path
        if file_path == "":
            logger.error("Context=" + __class__.__name__ +
                         "|Message=" + "Must define file path.")
            return []

    @staticmethod
    def get_monster(entry):
        return None

    @staticmethod
    def get_monster_list(root_node):
        return []

    @staticmethod
    def get_root_node(xml_input):
        return ""
