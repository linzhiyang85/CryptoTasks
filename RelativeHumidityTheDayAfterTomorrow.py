import requests
from datetime import datetime, timedelta

def get_relative_humidity_of_the_day_after_tomorrow():
    day_after_tomorrow = datetime.now() + timedelta(days=2)
    date_str = day_after_tomorrow.strftime('%Y%m%d')
    api_url = 'https://pda.weather.gov.hk/locspc/android_data/fnd_uc.xml'
    resp = requests.get(api_url)
    if resp.status_code == 200:
        jObj = resp.json()
        for item in jObj['forecast_detail']:
            if item['forecast_date'] == date_str:
                return (item['forecast_date'], item['min_rh'], item['max_rh'])

if __name__ == '__main__':
    datestr, min_rh, max_rh = get_relative_humidity_of_the_day_after_tomorrow()
    print(f"Relative Humidity for {datestr[:4]}/{datestr[4:6]}/{datestr[-2:]} is {min_rh}%-{max_rh}%")