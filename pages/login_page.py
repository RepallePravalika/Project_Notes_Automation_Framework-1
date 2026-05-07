# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# from pages.base_page import BasePage


# class LoginPage(BasePage):

#     # Home page login button
#     HOME_LOGIN_BTN = (
#         By.CSS_SELECTOR,
#         "a[href='/notes/app/login']"
#     )

#     # Login form fields
#     EMAIL = (
#         By.ID,
#         "email"
#     )

#     PASSWORD = (
#         By.ID,
#         "password"
#     )

#     LOGIN_SUBMIT_BTN = (
#         By.CSS_SELECTOR,
#         "[data-testid='login-submit']"
#     )

#     # Dashboard validation
#     ADD_NOTE_BTN = (
#         By.CSS_SELECTOR,
#         "[data-testid='add-new-note']"
#     )

#     def load(self, url):

#         self.driver.get(url)

#     def open_login_page(self):

#         WebDriverWait(self.driver, 10).until(
#             EC.element_to_be_clickable(
#                 self.HOME_LOGIN_BTN
#             )
#         ).click()

#     def login(self, email, password):

#         self.enter_text(
#             self.EMAIL,
#             email
#         )

#         self.enter_text(
#             self.PASSWORD,
#             password
#         )

#         self.click(
#             self.LOGIN_SUBMIT_BTN
#         )

#     def is_dashboard_loaded(self):

#         return WebDriverWait(self.driver, 10).until(
#             EC.visibility_of_element_located(
#                 self.ADD_NOTE_BTN
#             )
#         )


from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class LoginPage(BasePage):

    # Home page login button
    HOME_LOGIN_BTN = (
        By.CSS_SELECTOR,
        "a[href='/notes/app/login']"
    )

    # Login form fields
    EMAIL = (
        By.ID,
        "email"
    )

    PASSWORD = (
        By.ID,
        "password"
    )

    LOGIN_SUBMIT_BTN = (
        By.CSS_SELECTOR,
        "[data-testid='login-submit']"
    )

    # Dashboard validation
    ADD_NOTE_BTN = (
        By.CSS_SELECTOR,
        "[data-testid='add-new-note']"
    )

    def load(self, url):

        self.driver.get(url)

    def open_login_page(self):
        self.click(
            self.HOME_LOGIN_BTN
        )

        
    def login(self, email, password, wait_for_dashboard=True):
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.PASSWORD, password)
        self.click(self.LOGIN_SUBMIT_BTN)
        
        if wait_for_dashboard:
            # Wait for dashboard to load after login
            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(self.ADD_NOTE_BTN)
            )

    def is_dashboard_loaded(self):

        return WebDriverWait(
            self.driver,
            10
        ).until(

            EC.visibility_of_element_located(
                self.ADD_NOTE_BTN
            )
        )