#!/usr/bin/env python3

import xml.etree.ElementTree as ET

tree = ET.parse('issue_mapping.xml')

print('Issue Mapping')
print('---------------------')


for mapping in tree.getroot():
    print('mapping: ')
    for node in mapping:
        print('    ' + node.tag + ': ' + node.text)
        print(type(node))
    print()


print('---------------------')
