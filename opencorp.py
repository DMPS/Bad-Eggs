import httplib
import urllib
import sys
import json
from datetime import datetime,timedelta

def parse_date(string):
    if string is None:
        return None
    else:
        return datetime.strptime(string, "%Y-%m-%d")

today = datetime.today()

def suspicious(company):
    ret_val = {}
    inc_date = parse_date(company['incorporation_date'])
    if inc_date is None or today - inc_date < timedelta(1000):
        ret_val['inc_date'] = inc_date
    if company['dissolution_date'] is not None:
        ret_val['dissolution_date'] = company['dissolution_date']
    return ret_val

def fetch_companies(search_term):
    conn = httplib.HTTPConnection('api.opencorporates.com')
    params = urllib.urlencode({'q': search_term})
    conn.request('GET', '/v0.4.3/companies/search' + '?' + params)
    response = conn.getresponse()
    #print response.status, response.reason

    data = json.loads(response.read())
    print 'Number of results:', data['results']['total_count']
    return [ c['company'] for c in data['results']['companies'] ]

name = 'Nokia Oyj'
if len(sys.argv) > 1:
    name = sys.argv[1]

comps = fetch_companies(name)
for co in comps:
    print co['name'], suspicious(co)

