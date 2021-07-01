from jira import JIRA
import requests
from requests.auth import HTTPBasicAuth
import json
token = 'MTg2NTgxMDI4Mzg5OnXd8RaxXO9i4waU5vxJvcE0M5xK'
username = r"bytex"
base_url = r"https://jira.fraglab.com"

#session = requests.session()
#resp = session.get(base_url + "/browse/LI-4240", auth=HTTPBasicAuth(username, token))
#nedded = requests.get(r"https://jira.fraglab.com", auth=('bytex', '3b7cbc8bbe0c7866ccd003c1ba21add68f6ddb31'))
#print(nedded.text)
response = requests.get("https://jira.fraglab.com//rest//api//latest//issue//LI-3981", auth=(username, token))
print(response.text)
