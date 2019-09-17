#!/usr/bin/env python3

import xml.etree.ElementTree as ET
from xmlReader import DataMappingReader

class DataMapping:
    def __init__(self, value):
        if (isinstance(value, ET.ElementTree)):
            self.__data = node
        elif(isinstance(value, str)):
            self.__data = DataMappingReader().readFile(value).getroot()

    def __hasNode(self, nodename, tree, depth=1):
        found = False
        
        for child in tree:
            if (found):
                break
            elif (child.tag == nodename):
                found = True
            elif (depth > 1):
                found = self.__hasNode(nodename, child, depth - 1)

        return found

    def __getNodeRecur(self, nodename, tree, depth=10):
        node = None
        
        for child in tree:
            if (node != None):
                break
            elif (child.tag == nodename):
                node = child
            elif (depth > 1):
                node = self.__getNodeRecur(nodename, child, depth - 1)

        return node

    def getNode(self, nodename):
        return self.__getNodeRecur(nodename, self.__data)

    def getMapping(self, nodename):
        mappingList = []
        elementMappings = self.getNode(nodename)
        for mapping in elementMappings:
            mappingList.append({ 
                'old': mapping.find('old').text,
                'new': mapping.find('new').text 
            })
        return mappingList

