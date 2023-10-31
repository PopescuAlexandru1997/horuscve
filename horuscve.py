import requests
import json
import time
from datetime import datetime #for ISO8601  datetimeformat
import sys

def print_log(string):
    if(logging == '1'):
        print(string)

logging = sys.argv[1]
pubStartDate = sys.argv[2]
pubEndDate = sys.argv[3]
argument_start_lib = 4

print_log(time.ctime())
print_log("HORUSCVE APP STARTED")
print_log(pubStartDate)
print_log(pubEndDate)

today_date = datetime.now().replace(microsecond=0)
string_api_horus = 'http://www.horuscve.org/api/vulnerabilities/date-range?startDate='+pubStartDate+'&endDate='+pubEndDate
print_log(string_api_horus)

response_horus = requests.get(string_api_horus)
print_log(response_horus)

libraries=list()
for i in range(argument_start_lib,len(sys.argv)):
    print_log(str(sys.argv[i]))
    libraries.append(str(sys.argv[i]))

if (response_horus.status_code == 200):
    print_log("Response 200")
    with open('output/horuscve.json','wb') as f:
        f.write(response_horus.content)
else:
    print_log("Response not OK")



json_dict = response_horus.json()
vuln = json_dict['vulnerabilities']
print_log("--------------------------------")
for i in range(0, len(vuln)-1):
    temp=vuln[i]
    temp_cve=temp['description'].lower()
    for lib in libraries:
        if lib in temp_cve:
            print(str(temp['cve_id'])," for the component ",lib)
print_log("--------------------------------")


print(time.ctime())
print_log("HORUSCVE APP FINISHED")