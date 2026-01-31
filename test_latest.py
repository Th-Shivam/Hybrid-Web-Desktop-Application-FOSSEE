import requests

# Test retrieval of latest analysis
url = 'http://127.0.0.1:8000/api/latest-analysis/'

try:
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    print("Latest Analysis Data:")
    print(response.json())
except Exception as e:
    print(e)
