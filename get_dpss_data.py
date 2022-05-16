import pandas as pd 
import numpy as np 
import requests
from datetime import date, datetime, timedelta

def get_crime_stats(start_date, end_date):
    '''
    Takes in start date and end date 
    and gets data from DPSS Crime Log
    Database

    Date Format: YYYY-MM-DD
    '''
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date,  "%Y-%m-%d")
    date_range = [start_date + timedelta(days = x) for x in range((end_date - start_date).days)]
    data = []
    for dt in date_range:
        year = dt.year
        month = dt.month
        day = dt.day
        url = f"https://dpss.umich.edu/api/GetCrimeLogCache?date={month}/{day}/{year}" 
        resp =  requests.get(url)
        data.append(resp.json())
    return data
        



def main():
    start_date = '2022-04-12'
    end_date = '2022-04-15'
    print(get_crime_stats(start_date, end_date))

if __name__ == "__main__":
    main()