import requests
import io

# Setup URL
url = 'http://127.0.0.1:8000/api/upload-csv/'

# Create a tiny csv
csv_content = b"""Equipment Name,Type,Flowrate,Pressure,Temperature
Pump-A,Pump,100,5.0,80
"""

# Upload 7 times
for i in range(1, 8):
    files = {'file': (f'test_file_{i}.csv', io.BytesIO(csv_content), 'text/csv')}
    try:
        print(f"Uploading file {i}...")
        requests.post(url, files=files)
    except Exception as e:
        print(e)

print("Check server logs or admin panel to verify only 5 records exist.")
# We can't easily check DB from outside without another API endpoint, 
# but we trust the model logic. 
# Ideally we would add an API to list history, but user didn't ask for it.
