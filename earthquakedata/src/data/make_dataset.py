import requests
import json
import pandas as pd
from datetime import datetime
import os

def fetch_earthquake_data():
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
        'format': 'geojson',
        'starttime': '2024-01-01',  # Change this to desired start date
        'endtime': '2024-12-31',  # Change this to desired end date
        'minmagnitude': 4.0  # Filter earthquakes greater than magnitude 4
    }
    
    response = requests.get(url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error fetching data from USGS API")

def save_data(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)
        
# Example usage
if __name__ == "__main__":
    data = fetch_earthquake_data()
    filename=os.path.dirname( os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+ "/data/raw/earthquake_data.json"
    print(filename)
    save_data(data,filename)
