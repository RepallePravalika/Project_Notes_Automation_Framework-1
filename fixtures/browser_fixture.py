# # import pytest

# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service

# # from webdriver_manager.chrome import ChromeDriverManager


# # @pytest.fixture
# # def driver():

# #     service = Service(
# #         ChromeDriverManager().install()
# #     )

# #     driver = webdriver.Chrome(service=service)

# #     driver.maximize_window()

# #     yield driver

# #     driver.quit()

# import pytest

# from selenium import webdriver

# from webdriver_manager.chrome import ChromeDriverManager

# from selenium.webdriver.chrome.service import Service


# @pytest.fixture

# def driver():

#     driver = webdriver.Chrome(

#         service=Service(
#             ChromeDriverManager().install()
#         )
#     )

#     # Maximize browser
#     driver.maximize_window()

#     yield driver

#     driver.quit()


import pytest

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options

from selenium.webdriver import Remote


@pytest.fixture()

def driver():

    use_grid = True

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    if use_grid:

        driver = Remote(

            command_executor=
            "http://localhost:4444/wd/hub",

            options=chrome_options
        )

    else:

        driver = webdriver.Chrome(

            service=Service(
                ChromeDriverManager().install()
            ),

            options=chrome_options
        )

    # Maximize browser
    driver.maximize_window()

    yield driver

    driver.quit()