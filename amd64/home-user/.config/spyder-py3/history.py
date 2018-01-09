# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

##---(Sun Sep 24 23:23:10 2017)---
import csv
import xmltodict
from json import loads, dumps
from bs4 import BeautifulSoup
import json
from .. import goodreads
pwd
%cd scripts
%pwd
%cd /scripts
ls
%cd goodreads_sample/
pwd
from .. import goodreads
from . import goodreads
from ..goodreads import to_dict
from .goodreads import to_dict
import goodreads
import .goodreads
import ./goodreads
from ..goodreads import *
pwd
from .. import goodreads
from ..goodreads import *
from ..goodreads import to_dict
from .. import goodreads
%pwd
ls
from .. import goodreads
%cd ..
from .. import goodreads
from . import goodreads
import goodreads
from goodreads import to_dict
xml = open('/archive/Studies/DataScience/DSc_portfolio/bestsellers/scripts/goodreads_sample/sample.xml')
obj = to_dict(xmltodict.parse(xml.content))
with open('/archive/Studies/DataScience/DSc_portfolio/bestsellers/scripts/goodreads_sample/sample.xml') as f:
    obj = to_dict(xmltodict.parse(f))

with open('/archive/Studies/DataScience/DSc_portfolio/bestsellers/scripts/goodreads_sample/sample.xml', 'b') as f:
    obj = to_dict(xmltodict.parse(f))

obj = to_dict(xmltodict.parse('/archive/Studies/DataScience/DSc_portfolio/bestsellers/scripts/goodreads_sample/sample.xml'))
obj = to_dict(xmltodict.parse('/archive/Studies/DataScience/DSc_portfolio/bestsellers/scripts/goodreads_sample/sample.xml', encoding='utf-8'))
obj = to_dict(xmltodict.parse('sample.xml', encoding='utf-8'))
doc = ElementTree(file="sample.xml") 
from xml.etree.ElementTree import ElementTree
doc = ElementTree(file="sample.xml") 
doc = ElementTree(file="/sample.xml") 
doc = ElementTree(file='/archive/Studies/DataScience/DSc_portfolio/bestsellers/scripts/goodreads_sample/sample.xml') 
with open('/archive/Studies/DataScience/DSc_portfolio/bestsellers/scripts/goodreads_sample/sample.xml') as f:
    obj = to_dict(xmltodict.parse(f))

with open('/archive/Studies/DataScience/DSc_portfolio/bestsellers/scripts/goodreads_sample/sample.xml', 'rb') as f:
    obj = to_dict(xmltodict.parse(f))

obj['GoodreadsResponse'][type] 
print(obj['GoodreadsResponse'][type]) 
print(obj['GoodreadsResponse']['book']['id']) 
with open('/archive/Studies/DataScience/DSc_portfolio/bestsellers/scripts/goodreads_sample/sample.xml', 'rb') as f:
    obj = to_dict(xmltodict.parse(f))
    book = obj['GoodreadsResponse'][type]

with open('/archive/Studies/DataScience/DSc_portfolio/bestsellers/scripts/goodreads_sample/sample.xml', 'rb') as f:
    obj = to_dict(xmltodict.parse(f))
    book_obj = obj['GoodreadsResponse'][type]

book_obj['book']['popular_shelves']
with open('/archive/Studies/DataScience/DSc_portfolio/bestsellers/scripts/goodreads_sample/sample.xml', 'rb') as f:
    obj = to_dict(xmltodict.parse(f))
    book_obj = obj['GoodreadsResponse'][type]

book_obj['book']['popular_shelves']
book_obj
book_obj = obj['GoodreadsResponse'][type]
book_obj['book']
obj['book']
def get_object():     
    with open('/archive/Studies/DataScience/DSc_portfolio/bestsellers/scripts/goodreads_sample/sample.xml', 'rb') as f:
        obj = to_dict(xmltodict.parse(f))
    return obj['GoodreadsResponse'][type]

book_obj = get_object()
book_obj['book']
def get_object(type):     
    with open('/archive/Studies/DataScience/DSc_portfolio/bestsellers/scripts/goodreads_sample/sample.xml', 'rb') as f:
        obj = to_dict(xmltodict.parse(f))
    return obj['GoodreadsResponse'][type]


book_obj = get_object('book')
book_obj['book']
book_obj
book_obj['popular_shelves']
book_obj['popular_shelves']['shelf']
book_obj['popular_shelves']['shelf'][0]
book_obj['popular_shelves']['shelf'][0]['@name']
{i['@name'] for i in book_obj['popular_shelves']['shelf'] }
[i['@name'] for i in book_obj['popular_shelves']['shelf']]
keywords = ['animals', 'contemporary', 'fantasy', 'humor', 'adult', 'family', 'inspirational', 'pets', 'reincarnation', 'tear-jerker', 'made-me-cry', 'animal-behavior', 'adventure', 'life-lessons', 'humour', 'death']
[i['@name'] for i in book_obj['popular_shelves']['shelf'] if i['@name'] is in keywords]
[i['@name'] for i in book_obj['popular_shelves']['shelf'] if i['@name'] in keywords]
top5_genres = [i['@name'] for i in book_obj['popular_shelves']['shelf'] if i['@name'] in keywords][:5]
top5_genres

##---(Mon Sep 25 13:53:53 2017)---
import csv
import xmltodict
from json import loads, dumps
from bs4 import BeautifulSoup
import json

from goodreads import to_dict
keywords = ['animals', 'contemporary', 'fantasy', 'humor', 'adult', 'family', 'inspirational', 'pets', 'reincarnation', 'tear-jer lker', 'made-me-cry', 'animal-behavior', 'adventure', 'life-lessons', 'humour', 'death']


def get_object(type):     
    with open('/archive/Studies/DataScience/DSc_portfolio/bestsellers/scripts/goodreads_sample/sample.xml', 'rb') as f:
        obj = to_dict(xmltodict.parse(f))
    return obj['GoodreadsResponse'][type]


book_obj = get_object('book')
top5_genres = []

for i in book_obj['popular_shelves']['shelf']:
    if i['@name'] in keywords:
        top5_genres.append(i['@name'])
    if len(top5_genres) == 5: break



top5_genres