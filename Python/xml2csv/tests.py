#!/usr/bin/env python3

import unittest as ut
import xml.etree.ElementTree as ET
from xmlReader import DataMappingReader
from dataMapping import DataMapping

class DataMappingReaderTest(ut.TestCase):
    def testInstance(self):
        self.assertIsInstance(
            DataMappingReader(), 
            DataMappingReader
        )

    def testCanCreateTreeFromFileIssueMapping(self):
        self.assertIsInstance(
            DataMappingReader().readFile('./issue_mapping.xml'),
            ET.ElementTree
        )

    def testCreateIssueMapping(self):
        dmr = DataMappingReader()
        dmr.createXmlTree('./issue_mapping.xml', 'issue_id')

        self.assertEqual(
            dmr.get('issue_id').tag,
            'issue_id'
        )

class DataMappingTest(ut.TestCase):
    def testGetNode(self):
        mapping = DataMapping('./economicaDataMappings.xml')
        node = mapping.getNode('issue_id')

        self.assertIsInstance(
            node,
            ET.Element
        )

    def testCreateMapping(self):
        mapping = DataMapping('./economicaDataMappings.xml').getMapping(
            'issue_id'
        )

        self.assertIsInstance(
            mapping,
            list
        )

    def testArticleMapping(self):
        articleMapping = DataMapping('./economicaDataMappings.xml').getMapping(
            'article_id'
        )

        self.assertTrue(len(articleMapping) > 100)

if (__name__ == '__main__'):
    ut.main()
