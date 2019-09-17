#!/usr/bin/env python3

import xml.etree.ElementTree as ET

class DataMappingReader:
    def __init__(self):
        self.__trees = dict()

    def get(self, name):
        if (name in self.__trees.keys()):
            return self.__trees[name]

    def set(self, name, value):
        self.__trees[name] = value
        
    def readFile(self, filename):
        return ET.parse(filename)

    def createXmlTree(self, filename, nodename):
        self.set(nodename, self.readFile(filename).getroot())
