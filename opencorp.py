import httplib
import urllib
import sys
import json

conn = httplib.HTTPConnection('api.opencorporates.com')
params = urllib.urlencode({'q': 'Nokia Oyj'})
conn.request('GET', '/v0.4.3/companies/search' + '?' + params)
response = conn.getresponse()
print response.status, response.reason

data = json.loads(response.read())
print 'Number of results:', data['results']['total_count']

comps = data['results']['companies']
names = [ c['company']['name'] for c in comps ]
for name in names:
    print name

#recent = data['results']['company']['data']['most_recent']
#for d in recent:
#    print d['datum']['title']

def suspicious(company):
    return True
