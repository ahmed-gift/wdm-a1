# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 17:41:52 2020

@author: Ahmed
"""

import xmlschema
from pprint import pprint

xsd = xmlschema.XMLSchema('resume-xml-schema.xsd')
print(xsd.is_valid('resume.xml'))
if xsd.is_valid('resume.xml'):
    print ("Your Resume is Valid")
print(xsd.validate('resume.xml'))