from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class NotesPage(BasePage):

    # Add Note button
    ADD_NOTE_BTN = (
        By.CSS_SELECTOR,
        "[data-testid='add-new-note']"
    )

    # Category dropdown
    CATEGORY_DROPDOWN = (
        By.CSS_SELECTOR,
        "[data-testid='note-category']"
    )

    # Title field
    TITLE_FIELD = (
        By.CSS_SELECTOR,
        "[data-testid='note-title']"
    )

    # Description field
    DESCRIPTION_FIELD = (
        By.CSS_SELECTOR,
        "[data-testid='note-description']"
    )

    # Create button
    CREATE_BTN = (
        By.XPATH,
        "//button[contains(text(),'Create')]"
    )

    # Notes list
    NOTES_LIST = (
        By.CSS_SELECTOR,
        "[data-testid='notes-list']"
    )

    # First note title
    FIRST_NOTE_TITLE = (
        By.CSS_SELECTOR,
        "[data-testid='note-card-title']"
    )

    def click_add_note(self):

        self.click(
            self.ADD_NOTE_BTN
        )

    def select_category(self, category):

        dropdown = WebDriverWait(
            self.driver,
            10
        ).until(

            EC.visibility_of_element_located(
                self.CATEGORY_DROPDOWN
            )
        )

        Select(dropdown).select_by_visible_text(
            category
        )

    def enter_title(self, title):

        self.enter_text(
            self.TITLE_FIELD,
            title
        )

    def enter_description(self, description):

        self.enter_text(
            self.DESCRIPTION_FIELD,
            description
        )

    def click_create(self):

        self.click(
            self.CREATE_BTN
        )

    def is_note_created(self, title):

        note_locator = (
            By.XPATH,
            f"//*[contains(text(),'{title}')]"
        )

        return WebDriverWait(
            self.driver,
            10
        ).until(

            EC.visibility_of_element_located(
                note_locator
            )
        )

    def get_first_note_title(self):

        note = WebDriverWait(
            self.driver,
            10
        ).until(

            EC.visibility_of_element_located(
                self.FIRST_NOTE_TITLE
            )
        )

        return note.text

    def is_note_present(self, title):
        """Checks if a note with the given title is present on the page."""
        note_locator = (
            By.XPATH,
            f"//div[@data-testid='note-card']//h2[contains(text(),'{title}')]"
        )
        try:
            # Short wait to see if it's still there
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(note_locator)
            )
            return True
        except:
            return False

    def refresh_page(self):
        self.driver.refresh()

        WebDriverWait(
            self.driver,
            15
        ).until(
            EC.visibility_of_element_located(
                self.ADD_NOTE_BTN
            )
        )