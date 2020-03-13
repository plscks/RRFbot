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

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

def dataGrab():
    now = datetime.datetime.utcnow()
    csvFormat = f'{now.month:02d}-{(now.day-1):02d}-{now.year}.csv'
    url = f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{csvFormat}'
    df = pd.read_csv(url,names=['Province', 'Country', 'Updated', 'Confirmed', 'Deaths', 'Recovered', 'Latitude', 'Longitude'], skiprows=1)
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

if __name__ == "__main__":
    data = dataGrab()
    worldData = parseData('world', data)
    usData = parseData('us', data)
    localData = parseData('local', data)
    output(worldData, usData, localData)
    i2cOut(worldData, usData, localData)
