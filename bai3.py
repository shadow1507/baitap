import csv
import json
import pandas as pd
from pandas.io.json import json_normalize

import requests

r = requests.get("https://d4c424ddddace0fb56529ba55f999d46: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@customerrs.myshopify.com/admin/api/2020-10/customers.json",
                 'Authorization: Basic d4c424ddddace0fb56529ba55f999d46')
a=r.json()

b=a['customers']

for i in b:
    del i['addresses']
    del i['tax_exemptions']
    del i['default_address']
colum=[]
for col in b[0].keys():
    colum.append(col)

with open('customers.csv','w')as f:
 p=csv.DictWriter(f,fieldnames=colum)
 p.writeheader()
 p.writerows(b)