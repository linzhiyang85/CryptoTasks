import requests
from datetime import datetime, timedelta

def test_relative_humidity():
    api_url = 'https://pda.weather.gov.hk/locspc/android_data/fnd_uc.xml'
    resp = requests.get(api_url)
    assert resp.status_code == 200, "API request failed"

    jObj = resp.json()
    day_after_tomorrow = datetime.now() + timedelta(days=2)
    date_str = day_after_tomorrow.strftime('%Y%m%d')

    for item in jObj['forecast_detail']:
        if item['forecast_date'] == date_str:
            print(item['forecast_date'], item['min_rh'], item['max_rh'])