# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 12:32:05 2020

@author: Ahmed
"""


from lxml import etree

parser = etree.XMLParser(dtd_validation = True)

tree = etree.parse("resume.xml",parser)
