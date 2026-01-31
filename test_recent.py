import requests
import json

# Test retrieval of recent analysis
url = 'http://127.0.0.1:8000/api/recent-analysis/'

try:
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    
    data = response.json()
    if isinstance(data, list):
        print(f"Received list of {len(data)} records.")
        # Print first one as sample
        if len(data) > 0:
            print("Most recent record sample:")
            print(json.dumps(data[0], indent=2))
    else:
        print("Expected a list, got something else.")
        print(data)

except Exception as e:
    print(e)
