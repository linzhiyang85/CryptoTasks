import pytest
import time
from page.exchange import ExchangePage
from page.trade import TradePage

class TestTrade:
    @pytest.mark.parametrize('source, target', [('CRO', 'USDC'), ('ATOM', 'CRO')])
    def test_navigate_to_trade_page(self, source, target, driver, settings):
        # initialize page object
        exchange_page = ExchangePage(driver)
        trade_page = TradePage(driver)

        # maximize
        exchange_page.maximize_window()

        # open initial page, accept cookie
        exchange_page.open(settings.get_start_url('exchange'))
        exchange_page.accept_cookie()

        # find target instrument
        exchange_page.click_market_menu(target)
        instrument = exchange_page.get_instrument(source, target)
        assert instrument is not None, f'Failed to find instrument for {source}/{target}'

        # click to open trade page
        exchange_page.open_instrument(instrument)
        exchange_page.wait_for_url_change(driver.current_url)

        # verification
        assert '/trade/' in driver.current_url and f'{source}_{target}' in driver.current_url, f"Failed to open trade page for {source}/{target}"
        assert f'{source}/{target}' == trade_page.get_instrument_name(), "Instrument name in trade page is not correct"


