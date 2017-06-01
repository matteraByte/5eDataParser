#!/usr/bin/python

import sys
from Converter.XmlToBmd import XmlToBmd as Converter

numArgs = len(sys.argv)
if numArgs < 3:
    print("Invalid number of arguments. "
          "Usage: python ConvertXmlToBestiaryMarkdown.py InputFileOrDirectory OutputDirectory")
else:
    inFileOrDirectory = sys.argv[1]
    outDirectory = sys.argv[2]
    Converter.convert(inFileOrDirectory, outDirectory)

