# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 20:58:03 2017

@author: alexb
"""

import requests
import json
import prettytable
import pandas as pd

headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid": ['CUUR0000SA0','SUUR0000SA0'],"startyear":"2011", "endyear":"2014"})
p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)
for series in json_data['Results']['series']:
    x = pd.DataFrame(["series id","year","period","value","footnotes"])
    seriesId = series['seriesID']
    for item in series['data']:
        year = item['year']
        period = item['period']
        value = item['value']
        footnotes=""
        for footnote in item['footnotes']:
            if footnote:
                footnotes = footnotes + footnote['text'] + ',' 'if 'M01' <= period <= 'M12':' x.add_row([seriesId,year,period,value,footnotes[0:-1]])
    output = open(seriesId + '.txt','w')
    output.write (x.get_string())
    output.close()

# Alternative and Core Financial Markets Data
# https://www.quandl.com/

# Not sure but seems to have employement and salary data
# https://developer.adzuna.com/overview

# https://www.data.gov/

# San Francisco specific datasets:
    # https://catalog.data.gov/dataset?groups=local&organization=city-of-san-francisco&_organization_limit=0
    # https://catalog.data.gov/dataset/employee-compensation-53987/resource/0cb14075-b998-4397-b677-b49fdec0f1ab?inner_span=True

# May 2016 Metropolitan and Nonmetropolitan Area Occupational Employment and Wage Estimates
# San Francisco-Oakland-Hayward, CA    
# https://www.bls.gov/oes/current/oes_41860.htm#00-0000
# https://www.bls.gov/developers/api_signature_v2.htm

# Great San Francisco dataset
# https://catalog.data.gov/dataset/employee-compensation-53987/resource/9bc4ffed-0869-4b9e-bfb8-18ce92cb8645
# https://data.sfgov.org/api/views/88g8-5mnd/rows.json?accessType=DOWNLOAD

# https://dev.socrata.com/
# https://dev.socrata.com/docs/endpoints.html
# https://dev.socrata.com/docs/app-tokens.html
# https://github.com/xmun0x/sodapy#getdataset_identifier-content_typejson-kwargs


https://data.sfgov.org/resource/wwmu-gmzc.json

from sodapy import Socrata
import urllib3

client = Socrata("https://data.seattle.gov/resource/3k2p-39jp.json?$$app_token=X-App-Token",None)

client.get("wwmu-gmzc", "$select=*")
client.get("wwmu-gmzc")

https://data.sfgov.org/resource/wwmu-gmzc.json

GET /resource/3k2p-39jp.json HTTP/1.1

a1 = urllib3.connection_from_url('https://data.sfgov.org/resource/wwmu-gmzc.json')
a1.urlopen()
print(a1)