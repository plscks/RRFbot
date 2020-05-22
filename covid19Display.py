# COVID-19 Data pull class
# version 0.1
# written by plscks
# [X]  Pull data from https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data in .csv format
# [X]  Parse data
# [X]  Output data
# [X]  Format data for input to I2C screen output
# []   Need to put in function for getting the correct date as the first day of a month always rolls back to 00 instead of the last day last month
# sudo pip3 install adafruit-blinka pandas sqlite3 adafruit-circuitpython-ssd1306 Pillow
import datetime
from datetime import timedelta
import pandas as pd
import time
import subprocess
import sqlite3

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

def dataGrab():
    ## need to include an if that will roll the month back and set to the last day of previous if it is the first.
    now = datetime.datetime.utcnow()
    dateChange = timedelta(days = 1)
    fileDate = now - dateChange
    csvFormat = f'{fileDate.month:02d}-{(fileDate.day):02d}-{fileDate.year}.csv'
    url = f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{csvFormat}'
    # Legacy format
    # df = pd.read_csv(url,names=['Province', 'Country', 'Updated', 'Confirmed', 'Deaths', 'Recovered', 'Latitude', 'Longitude'], skiprows=1)
    # New format as of 2020-03-24
    print(f'URL: {url}')
    # Legacy format - rolled back 2020-04-14
    df = pd.read_csv(url,names=['FIPS', 'County', 'Province', 'Country', 'Updated', 'Latitude', 'Longitude', 'Confirmed', 'Deaths', 'Recovered', 'Active', 'CombinedKeys'], skiprows=1)
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
    print(f'Available COVID-19 Data as of {now.month:02d}-{(now.day):02d}-{now.year} 00:00 UTC')
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

def databaseGrab():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~Getting data from COVID19 Database~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    worldData = []
    usData = []
    localData = []
    conn = sqlite3.connect('COVID-19')
    c = conn.cursor()

    print('~Grabbing world data.')
    wwQuery = 'SELECT a.date, SUM(a.confirmed) AS confirmed, SUM(a.deaths) AS deaths, SUM(a.recovered) AS recovered FROM all_data AS a INNER JOIN (SELECT MAX(date) AS MaxDate FROM all_data) AS md WHERE a.date = md.MaxDate'
    c.execute(wwQuery)
    worldRows = c.fetchall()
    worldData[0] = worldRows[0][1]
    worldData[1] = worldRows[0][2]

    print('~Grabbing US data.')
    usQuery = 'SELECT COUNT() AS count, a.date, SUM(a.confirmed) AS confirmed, SUM(a.deaths) AS deaths, SUM(a.recovered) AS recovered, last_updated, a.country AS country FROM all_data AS a INNER JOIN (SELECT MAX(date) AS MaxDate FROM all_data) AS md WHERE a.date = md.MaxDate AND (country like "US" OR province like "US")'
    c.execute(usQuery)
    usRows = c.fetchall()
    usData[0] = usRows[0][2]
    usData[1] = usRows[0][3]

    print('~Grabbing local data.')
    localQuery = 'SELECT COUNT() AS count, a.date, SUM(a.confirmed) AS confirmed, SUM(a.deaths) AS deaths, SUM(a.recovered) AS recovered, last_updated, a.country AS country FROM all_data AS a INNER JOIN (SELECT MAX(date) AS MaxDate FROM all_data) AS md WHERE a.date = md.MaxDate AND (country like "Illinois" OR province like "Illinois")'
    c.execute(localQuery)
    localRows = c.fetchall()
    localData[0] = localRows[0][2]
    localData[1] = localRows[0][3]

    conn.close()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~Pushing data to display~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    i2cOut(worldData, usData, localData)

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
        wwQuery = 'INSERT INTO all_data (province, country, last_updated, confirmed, deaths, recovered, fips, county, active, combined_keys) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        wwParams = (row['Province'], row['Country'], row['Updated'], row['Confirmed'], row['Deaths'], row['Recovered'], row['FIPS'], row['County'], row['Active'], row['CombinedKeys'])
        c.execute(wwQuery, wwParams)

    print('~Loading data into US database.')
    for index, row in us.iterrows():
        # format change from 2020-04-13
        # usQuery = 'INSERT INTO us_data (state, last_updated, confirmed, deaths, recovered, county, active, combined_keys, incident_rate, number_tested, number_hospitalized, uid) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        # usParams = (row['Province'], row['Updated'], row['Confirmed'], row['Deaths'], row['Recovered'], row['County'], row['Active'], row['CombinedKeys'], row['IncidentRate'], row['NumberTested'], row['NumberHospitalized'], row['UID'])
        usQuery = 'INSERT INTO us_data (state, last_updated, confirmed, deaths, recovered, county, active, combined_keys) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
        usParams = (row['Province'], row['Updated'], row['Confirmed'], row['Deaths'], row['Recovered'], row['County'], row['Active'], row['CombinedKeys'])
        c.execute(usQuery, usParams)

    print('~Loading data into local database.')
    for index, row in local.iterrows():
        # format change from 2020-04-13
        # localQuery = 'INSERT INTO il_data (last_updated, confirmed, deaths, recovered, county, active, combined_keys, incident_rate, number_tested, number_hospitalized, uid) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        # localParams = (row['Updated'], row['Confirmed'], row['Deaths'], row['Recovered'], row['County'], row['Active'], row['CombinedKeys'], row['IncidentRate'], row['NumberTested'], row['NumberHospitalized'], row['UID'])
        localQuery = 'INSERT INTO il_data (last_updated, confirmed, deaths, recovered, county, active, combined_keys) VALUES (?, ?, ?, ?, ?, ?, ?)'
        localParams = (row['Updated'], row['Confirmed'], row['Deaths'], row['Recovered'], row['County'], row['Active'], row['CombinedKeys'])
        c.execute(localQuery, localParams)

    conn.commit()
    conn.close()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~Finished database operations~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

if __name__ == "__main__":
    # data = dataGrab()
    # worldData = parseData('world', data)
    # usData = parseData('us', data)
    # localData = parseData('local', data)
    # output(worldData, usData, localData)
    # i2cOut(worldData, usData, localData)
    # databasePush(data)
    databaseGrab()