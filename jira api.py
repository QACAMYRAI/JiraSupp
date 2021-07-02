from jira import JIRA

token = 'MTg2NTgxMDI4Mzg5OnXd8RaxXO9i4waU5vxJvcE0M5xK'
username = r"bytex"
base_url = r"https://jira.fraglab.com"

jira_options = {'server': 'https://jira.fraglab.com'}
jira = JIRA(options=jira_options, basic_auth=(r'bytex', 'MTg2NTgxMDI4Mzg5OnXd8RaxXO9i4waU5vxJvcE0M5xK'))
#jql = 'project = ' + "lI-3891"
#issues_list = jira.search_issues(jql)
issue = jira.issue("LI-3891")
