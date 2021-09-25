# Task 1 Crypto Web UI Automation
- Install environment
1. Download and install python3.9, allure2.15.0
2. Install dependencies: pip install -r requirements.txt
- Run tests:  pytest --env prod --browser chrome --alluredir report .
- View report: allure serve .\report
# Task 2 MyObservatory API Request
- Capture API
1. Download and install Fiddler
2. Open fiddler, the default proxy port is 8888
3. In tools->options, enable remote computes to connect, restart fiddler
4. In cell phone, set proxy to computer's IP, and port is 8888
5. Download and install cert in cell phone
6. In cell phone, VirtualXposed
7. In VirtualXposed install JustTrustMe.apk and install APP MyObservatory
8. Open MyObservatory, when app initially loaded, Fiddler will capture API requests
9. In Fiddler search some keywords displayed in the 9 day forecast view, you can find the API retuning that content
10. Captured API is: https://pda.weather.gov.hk/locspc/android_data/fnd_uc.xml
- Request relative humidity for the day after tomorrow:
python RelativeHumidityTheDayAfterTomorrow.py
