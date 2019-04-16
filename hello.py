from flask import Flask, request, Response
import jsonpickle
import numpy as np
import cv2
import xml.etree.ElementTree as XML

i = 0
while i < 4:
    res = XML.parse('Resources.xml')
    count = res.find('count')
    name = res.find('name')
    file_name = count.text + name.text
    res.find('count').text = str(int(count.text) + 1)
    res.find('name').text = 'image'
    res.write('Resources.xml')
    print(file_name)
    i = i+1
