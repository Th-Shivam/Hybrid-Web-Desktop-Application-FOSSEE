import requests
import pandas as pd
import io

# Define the URL
url = 'http://127.0.0.1:8000/api/upload-csv/'

# Prepare the file for upload
# Opening the actual file from the root directory
with open('sample_equipment_data.csv', 'rb') as f:
    files = {'file': f}
    try:
        response = requests.post(url, files=files)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")
