import requests
import pandas as pd
import io

# Create a dummy CSV
csv_content = """col1,col2
1,a
2,b
3,c
"""
dummy_file = io.StringIO(csv_content)

# Define the URL
url = 'http://127.0.0.1:8000/api/upload-csv/'

# Prepare the file for upload
files = {'file': ('test.csv', dummy_file, 'text/csv')}

try:
    response = requests.post(url, files=files)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {e}")
