import pandas as pd
import json
from datetime import datetime
import os

def process_earthquake_data(input_file='earthquake_data.json'):
    with open(input_file, 'r') as f:
        data = json.load(f)
        
    # Extract relevant fields
    earthquakes = []
    for feature in data['features']:
        earthquake = {
            'id': feature['id'],
            'magnitude': feature['properties']['mag'],
            'place': feature['properties']['place'],
            'timestamp': datetime.utcfromtimestamp(feature['properties']['time'] / 1000),
            'latitude': feature['geometry']['coordinates'][1],
            'longitude': feature['geometry']['coordinates'][0],
            'depth': feature['geometry']['coordinates'][2]
        }
        earthquakes.append(earthquake)
    
    # Create a DataFrame
    df = pd.DataFrame(earthquakes)
    
    # Optional: Handle missing data
    df.dropna(inplace=True)
    
    # Optional: Filter based on magnitude
    df = df[df['magnitude'] > 4.0]
    
    return df

def save_processed_data(df, output_file):
    df.to_csv(output_file, index=False)

#  usage
if __name__ == "__main__":
    inputFile=os.path.dirname( os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+ "/data/raw/earthquake_data.json"
    df = process_earthquake_data(inputFile)
    outputFile=os.path.dirname( os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+ "/data/processed/processed_earthquake_data.csv"
    save_processed_data(df,outputFile)
