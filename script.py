#!/usr/bin/python

import sys
import requests
import collections

def downloadwalker(tiledata):
    
    iteratorvar = enumerate(tiledata) if isinstance(tiledata, list) else tiledata.iteritems()
    for (k, v) in iteratorvar:
        if(isinstance(v, collections.Mapping) or isinstance(v, list)):
            downloadwalker(v)
        else:
            if k == "uri":
                #Download function goes here
                print(v)

if len(sys.argv) < 3:
    print("Error! At least 2 arguments required")
    exit()

asset_number = sys.argv[1]
access_token = sys.argv[2]
response = requests.get("https://api.cesium.com/v1/assets/{}/endpoint?access_token={}".format(asset_number, access_token))
if response.json().get("accessToken"):
    accessToken = response.json().get("accessToken")
    tileset = requests.get(" https://assets.cesium.com/{}/tileset.json?access_token={}".format(asset_number, accessToken))
    fo = open("tileset.json", "wb")
    fo.write(tileset.text)
    fo.close()
    downloadwalker(tileset.json())
else:
    print("An Error Occured")
    exit()
