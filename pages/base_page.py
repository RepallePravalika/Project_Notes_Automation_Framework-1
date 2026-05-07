from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):

        self.driver = driver

    def click(self, locator):

        element = WebDriverWait(
            self.driver,
            15
        ).until(

            EC.presence_of_element_located(locator)
        )

        # Scroll element into view
        self.driver.execute_script(

            "arguments[0].scrollIntoView({block: 'center'});",

            element
        )

        try:

            # Wait until clickable
            WebDriverWait(
                self.driver,
                10
            ).until(

                EC.element_to_be_clickable(locator)
            )

            # Normal click
            element.click()

        except Exception:

            # JavaScript fallback click
            self.driver.execute_script(
                "arguments[0].click();",
                element
            )

    def enter_text(self, locator, text):

        element = WebDriverWait(
            self.driver,
            10
        ).until(

            EC.visibility_of_element_located(locator)
        )

        element.clear()

        element.send_keys(text)