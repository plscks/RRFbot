#!/usr/bin/python3
# Nexus Clash search rates utility v0.5
# Written by plscks
# Utilizes WikiMedia built in api
# API documentation : https://wiki.nexuscla.sh/wiki/api.php
#
################
## TO DO LIST ##
################
# [X] get location page IDs in json format
# [X] sort page IDs into [locations: pageids]
# [X] get wikitext from pages by ID in json format
# [X] clean wiki text of useless information store in pageInfo =  [itemName: findWeight]
# [X] calculate search rate from findWeight totals
# [X] store in dictionary as locationRates = [itemName: searchRate]
# [X] store in dictionary within dictionary masterRates = [itemName: [locationName: searchRate]]
# [] sort itemName by searchRate descending
# [x] output as json to be imported in RRFBot
# [] Tea House (pageid:5886) lists as outside even though page shows only inside
#
# Is this a test?
# It has to be.....
import json
import re
import requests
import time

def getRawLocations():
    """Gets json data of all current breath locations wiki page ids"""
    response = requests.get('https://wiki.nexuscla.sh/wiki/api.php?action=query&list=categorymembers&cmtitle=Category:Current%20Locations&cmlimit=max&format=json')
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def getCleanLocations():
    """Sorts current breath locations into single dictionary {'Tile name': 'pageid'}"""
    locations = getRawLocations()
    masterLocation = {}
    for i in locations['query']['categorymembers']:
        masterLocation[i['title']] = i['pageid']
    return masterLocation

def getItemRates(location, pageid):
    """Gets item find weight from locations pages"""
    items = {}
    ## setup as {locationName: {itemName: findWeight}}
    response = requests.get('https://wiki.nexuscla.sh/wiki/api.php?action=parse&format=json&prop=wikitext&pageid=' + str(pageid))
    if response.status_code == 200:
        wikitext = json.loads(response.content.decode('utf-8'))
    else:
        print('Bad page ID, canceling request.')
    wikitext = wikitext['parse']['wikitext']['*']
    if 'Items found inside:' in wikitext:
        shortWikitext = wikitext[wikitext.find('|+ Items found inside:'):]
        insideFinds = shortWikitext.split('background-color:#f0f8ff;"', 1)[0]
        if 'Items found outside' in wikitext:
            outsideFinds = wikitext[wikitext.find('|+ Items found outside:'):]
            outsideFinds = outsideFinds.split('|}', 1)[0]
        else:
            insideFinds = insideFinds.split('|}', 1)[0]
            outsideFinds = None
    else:
        shortWikitext = wikitext[wikitext.find('|+ Items found outside:'):]
        outsideFinds = shortWikitext.split('|}', 1)[0]
        insideFinds = None
    if insideFinds == None:
        output = {}
        outsideItemNameList = textParse(outsideFinds)[0]
        outsideItemPercentList = textParse(outsideFinds)[1]
        number = -1
        #print(outsideItemNameList)
        for i in outsideItemNameList:
            number += 1
            output[i] = {'Outside ' + location: outsideItemPercentList[number]}
        return output
    else:
        if outsideFinds == None:
            output = {}
            insideItemNameList = textParse(insideFinds)[0]
            insideItemPercentList = textParse(insideFinds)[1]
            number = -1
            #print(insideItemNameList)
            for i in insideItemNameList:
                number += 1
                output[i] = {'Inside ' + location: insideItemPercentList[number]}
            return output
        else:
            totalItemNameList = []
            totalItemPercentList = []
            output = {}
            #print(f'Text: {insideFinds}')
            insideItemNameList = textParse(insideFinds)[0]
            insideItemPercentList = textParse(insideFinds)[1]
            outsideItemNameList = textParse(outsideFinds)[0]
            outsideItemPercentList = textParse(outsideFinds)[1]
            number = -1
            #print(insideItemNameList)
            for i in insideItemNameList:
                number += 1
                #print(f'Number: {number}    Location: {location}    Item: {i}')
                #print(f'Percent List: {insideItemPercentList}')
                output[i] = {'Inside ' + location: insideItemPercentList[number]}
            number = -1
            #print(outsideItemNameList)
            for i in outsideItemNameList:
                number += 1
                #print(f'Number: {number}    Location: {location}    Item: {i}')
                if i in output:
                    output[i].update({'Outside ' + location: outsideItemPercentList[number]})
                else:
                    output[i] = {'Outside ' + location: outsideItemPercentList[number]}
            return output

def textParse(text):
    """Pulls item names and correcsponding weights from input wiki text"""
    itemNames = re.finditer(r'(?<=\[\[).+?(?=\])', text)
    itemNameList = []
    itemRateList = []
    for m in itemNames:
        itemNameList.append(m[0])
    itemRates = re.finditer(r'(?<=\| )\d', text)
    for m in itemRates:
        itemRateList.append(int(m[0]))
    itemRatePercent = weight2Rate(itemRateList)
    return itemNameList, itemRatePercent

def weight2Rate(inputWeights):
    """converts item find weight to search rates by percentage"""
    weightSum = sum(inputWeights)
    percentRates = []
    for i in inputWeights:
        percentRates.append((i / weightSum) * 100)
    return percentRates

def masterOutput():
    masterLocations = getCleanLocations()
    findRates = {}
    locationData = {}
    masterList = {}
    for k, v in masterLocations.items():
        locationData[k] = getItemRates(k, v)
        #print(locationData[k])
        for key, value in locationData[k].items():
            #print(f'Key: {key}    Value: {value}')
            if key in masterList:
                #print(f'Master List before: {masterList}')
                masterList[key].update(value)
                #print(f'Master List after: {masterList}')
            else:
                #print(f'Master List before: {masterList}')
                masterList[key] = value
                #print(f'Master List after: {masterList}')
        time.sleep(2)
    return masterList

if __name__ == "__main__":
    #jsonOut = json.dumps(masterOutput())
    #print(jsonOut)
    with open('searchRates.json', 'w') as json_file:
        json.dump(masterOutput(), json_file)
