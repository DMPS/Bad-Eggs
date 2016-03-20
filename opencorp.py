import httplib
import httplib2
import sys
import json
from datetime import datetime,timedelta
import urllib

def parse_date(string):
    if string is None:
        return None
    else:
        return datetime.strptime(string, "%Y-%m-%d")

today = datetime.today()

def suspicious(company):
    company = company['company']
    ret_val = {}
    inc_date = parse_date(company['incorporation_date'])
    if inc_date is None or today - inc_date < timedelta(300):
        ret_val['inc_date'] = inc_date
    if company['dissolution_date'] is not None:
        ret_val['dissolution_date'] = company['dissolution_date']
#    if company['jurisdiction_code'] in [ 'im', 'ie', 'us_de' ]:
#        ret_val['jurisdiction_code'] = company['jurisdiction_code']
    return ret_val

def fetch_companies(search_term):
    conn = httplib.HTTPConnection('api.opencorporates.com')
    params = urllib.urlencode({'q': search_term})
    conn.request('GET', '/v0.4.3/companies/search' + '?' + params)
    response = conn.getresponse()
    print response.status, response.reason

    data = json.loads(response.read())
    print 'Number of results:', data['results']['total_count']
    return data['results']['companies']

def fetch_sanctions(search_term):
    url = 'https://uksanctionslist.apispark.net:443/v1/entities/'+urllib.quote_plus(search_term)
    h = httplib2.Http()
    h.add_credentials('badeggs', 'qwerty1234') # Basic authentication
    resp, content = h.request(url, "GET")
    return content

if __name__ == "__main__":
    name = 'Nokia Oyj'
    if len(sys.argv) > 1:
        name = sys.argv[1]

    comps = fetch_companies(name)
    for co in comps:
        print co['company']['name'], suspicious(co)

