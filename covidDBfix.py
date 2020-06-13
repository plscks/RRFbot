# COVID-19 Data pull class
# version 0.1
# written by plscks
# [X]  Pull data from https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data in .csv format
# [X]  Parse data
# [X]  Output data
# []  Format data for input to I2C screen output
#
import datetime
import pandas as pd
import time
import subprocess
import sqlite3

#from board import SCL, SDA
#import busio
#from PIL import Image, ImageDraw, ImageFont
#import adafruit_ssd1306

date = '2020-06-13'
urlDate = '06-12-2020'

def dataGrab():
    ## need to include an if that will roll the month back and set to the last day of previous if it is the first.
    now = datetime.datetime.utcnow()
    csvFormat = f'{now.month:02d}-{(now.day-1):02d}-{now.year}.csv'
    #url = f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{csvFormat}'
    # Legacy format
    # df = pd.read_csv(url,names=['Province', 'Country', 'Updated', 'Confirmed', 'Deaths', 'Recovered', 'Latitude', 'Longitude'], skiprows=1)
    # New format as of 2020-03-24
    url = f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{urlDate}.csv'
    print(f'URL: {url}')
    # Legacy format - rolled back 2020-04-14
    df = pd.read_csv(url,names=['FIPS', 'County', 'Province', 'Country', 'Updated', 'Latitude', 'Longitude', 'Confirmed', 'Deaths', 'Recovered', 'Active', 'CombinedKeys', 'IncidentRate', 'CaseFacilityRatio'], skiprows=1)
    # New format as of 2020-04-13
    # Province_State	Country_Region	Last_Update	Lat	Long_	Confirmed	Deaths	Recovered	Active	Admin2	FIPS	Combined_Key	Incident_Rate	People_Tested	People_Hospitalized	UID	ISO3
    # df = pd.read_csv(url,names=['Province', 'Country', 'Updated', 'Latitude', 'Longitude', 'Confirmed', 'Deaths', 'Recovered', 'Active', 'County', 'FIPS', 'CombinedKeys', 'IncidentRate', 'NumberTested', 'NumberHospitalized', 'UID', 'ISO3'], skiprows=1)
    return df

def parseData(region, df):
    if region == 'world':
        worldTotals = []
        worldTotals.append(df.Confirmed.sum())
        worldTotals.append(df.Deaths.sum())
        return worldTotals
    elif region == 'us':
        usTotals = []
        usTotals.append(df[df.Country == 'US'].Confirmed.sum())
        usTotals.append(df[df.Country == 'US'].Deaths.sum())
        return usTotals
    else:
        localTotals = []
        localTotals.append(df[df.Province == 'Illinois'].Confirmed.sum())
        localTotals.append(df[df.Province == 'Illinois'].Deaths.sum())
        return localTotals

def output(world, us, local):
    now = datetime.datetime.utcnow()
    print(f'Available COVID-19 Data as of {date} 00:00 UTC')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'Worldwide confirmed cases:   {world[0]}')
    print(f'Worldwide confirmaed deaths: {world[1]}')
    print('')
    print(f'US confirmed cases:  {us[0]}')
    print(f'US confirmed deaths: {us[1]}')
    print('')
    print(f'Illinois confirmed cases:  {local[0]}')
    print(f'Illinois confirmed deaths: {local[1]}')

def i2cOut(world, us, local):
    i2c = busio.I2C(SCL, SDA)
    disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
    disp.fill(0)
    disp.show()
    width = disp.width
    height = disp.height
    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    padding = -2
    top = padding
    bottom = height-padding
    x = 0
    font = ImageFont.load_default()
    #font = ImageFont.truetype('/home/plscks/FiraCode-Regular.ttf', 9)
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((x, top+0), '   COVID-19 DATA', font=font, fill=255)
    draw.text((x, top+8), '~~~~~~~~~~~~~~~~~~~~', font=font, fill=255)
    draw.text((x, top+16), f'World cases:  {world[0]}', font=font, fill=255)
    draw.text((x, top+24), f'World deaths: {world[1]}', font=font, fill=255)
    draw.text((x, top+32), f'US cases:  {us[0]}', font = font, fill = 255)
    draw.text((x, top+40), f'US deaths: {us[1]}', font = font, fill = 255)
    draw.text((x, top+48), f'Il cases:  {local[0]}', font = font, fill = 255)
    draw.text((x, top+56), f'Il deaths: {local[1]}', font = font, fill = 255)

    # Display image.
    disp.image(image)
    disp.show()

def databasePush(data):
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~Performing database operations~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    us = data[data.Country == 'US']
    local = data[data.Province == 'Illinois']
    conn = sqlite3.connect('COVID-19')
    c = conn.cursor()

    print('~Loading data to worldwide database.')
    for index, row in data.iterrows():
        # format change from 2020-04-13
        # wwQuery = 'INSERT INTO all_data (province, country, last_updated, confirmed, deaths, recovered, fips, county, active, combined_keys, incident_rate, number_tested, number_hospitalized, uid, iso3) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        # wwParams = (row['Province'], row['Country'], row['Updated'], row['Confirmed'], row['Deaths'], row['Recovered'], row['FIPS'], row['County'], row['Active'], row['CombinedKeys'], row['IncidentRate'], row['NumberTested'], row['NumberHospitalized'], row['UID'], row['ISO3'])
        wwQuery = 'INSERT INTO all_data (date, province, country, last_updated, confirmed, deaths, recovered, fips, county, active, combined_keys) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        wwParams = (f'{date}', row['Province'], row['Country'], row['Updated'], row['Confirmed'], row['Deaths'], row['Recovered'], row['FIPS'], row['County'], row['Active'], row['CombinedKeys'])
        c.execute(wwQuery, wwParams)

    print('~Loading data into US database.')
    for index, row in us.iterrows():
        # format change from 2020-04-13
        # usQuery = 'INSERT INTO us_data (state, last_updated, confirmed, deaths, recovered, county, active, combined_keys, incident_rate, number_tested, number_hospitalized, uid) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        # usParams = (row['Province'], row['Updated'], row['Confirmed'], row['Deaths'], row['Recovered'], row['County'], row['Active'], row['CombinedKeys'], row['IncidentRate'], row['NumberTested'], row['NumberHospitalized'], row['UID'])
        usQuery = 'INSERT INTO us_data (date, state, last_updated, confirmed, deaths, recovered, county, active, combined_keys) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'
        usParams = (f'{date}', row['Province'], row['Updated'], row['Confirmed'], row['Deaths'], row['Recovered'], row['County'], row['Active'], row['CombinedKeys'])
        c.execute(usQuery, usParams)

    print('~Loading data into local database.')
    for index, row in local.iterrows():
        # format change from 2020-04-13
        # localQuery = 'INSERT INTO il_data (last_updated, confirmed, deaths, recovered, county, active, combined_keys, incident_rate, number_tested, number_hospitalized, uid) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        # localParams = (row['Updated'], row['Confirmed'], row['Deaths'], row['Recovered'], row['County'], row['Active'], row['CombinedKeys'], row['IncidentRate'], row['NumberTested'], row['NumberHospitalized'], row['UID'])
        localQuery = 'INSERT INTO il_data (date, last_updated, confirmed, deaths, recovered, county, active, combined_keys) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
        localParams = (f'{date}', row['Updated'], row['Confirmed'], row['Deaths'], row['Recovered'], row['County'], row['Active'], row['CombinedKeys'])
        c.execute(localQuery, localParams)

    conn.commit()
    conn.close()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~Finished database operations~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

if __name__ == "__main__":
    data = dataGrab()
    worldData = parseData('world', data)
    usData = parseData('us', data)
    localData = parseData('local', data)
    output(worldData, usData, localData)
    #i2cOut(worldData, usData, localData)
    databasePush(data)
