import httplib
import sys
import json

conn = httplib.HTTPConnection('api.opencorporates.com')
conn.request('GET', '/companies/nl/17087985')
response = conn.getresponse()
print response.status, response.reason

data = json.loads(response.read())
recent = data['results']['company']['data']['most_recent']
for d in recent:
    print d['datum']['title']
