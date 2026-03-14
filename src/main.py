import requests

# TFL API endpoint
url = "https://api.tfl.gov.uk/Line/Mode/tube/Status"

# send request to TFL API
response = requests.get(url)

# check if the request was successful
if response.status_code == 200:
    data = response.json()
    for line in data:
        print(f"Line: {line['name']}")
        print(f"Status: {line['lineStatuses'][0]['statusSeverityDescription']}")

