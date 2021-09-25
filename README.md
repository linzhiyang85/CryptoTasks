# Task 1 Crypto Web UI Automation
- Install environment
  1. Download and install python3.9, allure2.15.0
  2. Install dependencies: **pip install -r requirements.txt**
- Run tests:  **pytest --env prod --browser chrome --alluredir report .**
- View report: **allure serve .\report**
- Case design:
  + Data driven and reuse the same code logic, case paths:
    + case/exchange/trade/test_navigation.py::TestTrade::test_navigate_to_trade_page[CRO-USDC]
    + case/exchange/trade/test_navigation.py::TestTrade::test_navigate_to_trade_page[ATOM-CRO]
  + Steps:
    1. Initialize chrome driver, create instances of page objects
    2. Maximize window
    3. Load from config file to get the start url and open it
    4. Wait for "Accept Cookie" button and accept it
    5. Find and click target menu tab, find and click "source/target" row and click, find the "Trade" button in the row (actually can directly click "source/target" element in instrument column, i.e. the first column
    6. Wait for switching to trading page
    7. Check points are:
      * The url has changed
      * The toggle button at top-left corner of the page is showing the correct "source/target" name
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
  10. Captured API is: **https://pda.weather.gov.hk/locspc/android_data/fnd_uc.xml**
- Request relative humidity for the day after tomorrow:
  **python RelativeHumidityTheDayAfterTomorrow.py**
- Or run as a test case:
  **pytest case\test_myobservatory.py**
  + Case checkpoints:
    + Response status code is 200
    + Able to extract fields min_rh and max_rh
