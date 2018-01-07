# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 18:33:17 2017

@author: Ignacio Iglesias
"""
#Next proyect get points and info from google places

import urllib.request, json, urllib
import requests
import os
from bs4 import BeautifulSoup
import pandas as pd

def GoogPlac(lat,lng,radius,types,key,keyword): #construyendo la url
  #making the url
  AUTH_KEY = key
  LOCATION = str(lat) + "," + str(lng)
  RADIUS = radius
  TYPES = types
  KEYWORD = keyword
  MyUrl = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
           '?location=%s'
           '&radius=%s'
           '&types=%s'
           '&keyword=%s'
           '&sensor=false&key=%s') % (LOCATION, RADIUS, TYPES, KEYWORD, AUTH_KEY)
  #grabbing the JSON result
  request = requests.get(MyUrl)
  return request
  
  
resp = GoogPlac(40.546285,-3.6277594,1000,'bank&atm',   #set lat, lng y radius and type. Set de GOOGLE API KEY
               'Put_Here_Your_Google_Api_Places_Key',
               '')

print(resp.text[:500])

resp_json = BeautifulSoup(resp.content, 'html.parser') #json solo para control
print(resp_json)
resp_dic =resp.json()
results = resp_dic['results']

for result in resp_dic['results']:      #recorriendo el resultado para comparar
    result['lat'] = result['geometry']['location']['lat']
    result['lng'] = result['geometry']['location']['lng']
    del result['geometry']
    print(result)

results_frm = pd.DataFrame(resp_dic['results'])

results_frm.to_csv('Zone.csv', sep=';',index=False, encoding='cp1252')

print(results_frm)
