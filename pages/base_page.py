import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.settings import TIMEOUT

logger = logging.getLogger(__name__)


class BasePage:
    """
    所有 Page Object 的基类。
    封装 WebDriver 的通用等待和操作，子类不直接调用 driver。
    """

    def __init__(self, driver) -> None:
        self._driver = driver
        self._wait   = WebDriverWait(driver, TIMEOUT)

    def _find(self, locator: tuple):
        try:
            element = self._wait.until(EC.visibility_of_element_located(locator))
            logger.debug("_find OK | locator=%s", locator)
            return element
        except TimeoutException:
            logger.debug("_find TIMEOUT | locator=%s", locator)  # ERROR 改 DEBUG
            raise

    def _click(self, locator: tuple) -> None:
        try:
            self._wait.until(EC.element_to_be_clickable(locator)).click()
            logger.debug("_click OK | locator=%s", locator)
        except TimeoutException:
            logger.debug("_click TIMEOUT | locator=%s", locator)  # ERROR 改 DEBUG
            raise

    def _input(self, locator: tuple, text: str) -> None:
        element = self._find(locator)
        element.clear()
        element.send_keys(text)
        logger.debug("_input OK | locator=%s | text=%s", locator, text)

    def _get_text(self, locator: tuple) -> str:
        return self._find(locator).text

    def get_current_url(self) -> str:
        return self._driver.current_url