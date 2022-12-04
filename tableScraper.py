# Simple program scraping a wikepedia table for largest law firms in the world
# needed this to speed up data collection for ENTR 3400 assignment 3 marketing report

import requests
from bs4 import BeautifulSoup
import numpy as np

URL = "https://en.wikipedia.org/wiki/List_of_largest_law_firms_by_revenue"

strUs = 'United States'
strCan = 'Canada'
strChina = 'China'
strGB = 'United Kingdom'

US = 0
USrev = 0
CANADA = 0
CANrev = 0
CHINA = 0
CHINArev = 0
GB = 0
GBrev = 0

moneyIn = 0

res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')
print()
for items in soup.find('table', class_='wikitable').find_all('tr')[1::1]:
    data = items.find_all(['th','td'])
    try:
        firmName = data[1].a.text
        firmRevenue = data[2].text.strip('$,\n,')
        firmRevenue = firmRevenue.replace(',', '')
        moneyIn = int(firmRevenue)
        firmCountry = data[6].text.strip()
    except IndexError:pass
    if firmCountry == strUs.strip():
        US += 1
        USrev += moneyIn
    elif firmCountry == strCan.strip():
        CANADA += 1
        CANrev += moneyIn
    elif firmCountry == strChina.strip():
        CHINA += 1
        CHINArev += moneyIn
    elif firmCountry == strGB.strip():
        GB += 1
        GBrev += moneyIn

    print("{} MAKES {} is located in {}".format(firmName, firmRevenue, firmCountry))

print("\nUS = {} CANADA = {} CHINA = {}\n".format(US, CANADA, CHINA))

firmsList = [[US, USrev, strUs], [CANADA, CANrev, strCan], [CHINA, CHINArev, strChina], [GB, GBrev, str]]
sorted(firmsList, key = lambda l:l[0])



print("The country with the most grossing law firms is {} with a total of {} firms bringing in ${}".format(firmsList[0][2], firmsList[0][0], firmsList[0][1]))