import pytesseract
from random_words import RandomWords
from PIL import Image, ImageDraw, ImageFont
import random
import time
import pytesseract
import easyocr
import parsel
import numpy as np
import pandas as pd
import difflib
import sys
import json

tsa_start_time = 0
tsa_end_time = 0
tsa_time_used = 0


def parse_xml(xml):
    """
    parse xml text to be accessed through xpath
    :param xml: xml text
    :type xml: str
    :return: parsel.selector.Selector
    :rtype: object
    """
    # setup xml parser
    parsel.Selector.__str__ = parsel.Selector.extract
    parsel.Selector.__repr__ = parsel.Selector.__str__
    parsel.SelectorList.__repr__ = lambda x: '[{}]'.format(
        '\n '.join("({}) {!r}".format(i, repr(s))
                   for i, s in enumerate(x, start=1))
    ).replace(r'\n', '\n')

    doc = parsel.Selector(text=xml)
    return doc


def tesseract_read(file: str):
    """
    extract text from the image using Tesseract
    :param file: path to the image
    :type file: str
    :return: text
    :rtype: str
    """
    hocr = pytesseract.image_to_pdf_or_hocr(file, extension='hocr')
    xml = hocr.decode('utf-8')
    doc = parse_xml(xml)
    tsa_output = []

    # get text
    for tag in doc.xpath('/html/body/div/div/p/span/span'):
        tsa_output.append(str(tag.xpath('text()')[0]))

    tsa_output = " ".join(tsa_output).lower()  # lowercase the output to be better compared with easyocr
    tsa_output = tsa_output.replace('-', ' ')  # replace '-' to be better compared with easyocr

    return tsa_output
tsa_start_time = time.time()

result_list = []
result_dict = {}

for i in range(1, 15):
    name = '../img/test' + str(i) + '.jpg'

    
    tsa_result = tesseract_read(name)
    tsa_time_used = tsa_time_used + (tsa_end_time-tsa_start_time)/60
    result_list.append(tsa_result)
    result_dict[str(i)] = result_list[i-1]
    #result = tesseract_read(name)
    print('test' + str(i) + ': \n')
    print(tsa_result)
    print('\n')

tsa_end_time = time.time()
tsa_time_used = tsa_time_used + (tsa_end_time-tsa_start_time)
print(tsa_time_used)

with open('tesse.json', 'w') as f:
    json.dump(result_dict, f, indent=1)
