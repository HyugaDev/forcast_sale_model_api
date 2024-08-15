import pandas as pd
from datetime import datetime

def preprocess_input(input_data):
    # Parse the input date string into a datetime object
    date_obj = datetime.strptime(input_data.date, '%Y-%m-%d')
    
    # Extract the year, month, and day from the date object
    year = date_obj.year
    month = date_obj.month
    day = date_obj.day
    
    # Create a DataFrame with the required columns
    data = {
        'store': [input_data.store],
        'item': [input_data.item],
        'month': [month],
        'day': [day],
        'year': [year]
    }
    df = pd.DataFrame(data)
    return df
