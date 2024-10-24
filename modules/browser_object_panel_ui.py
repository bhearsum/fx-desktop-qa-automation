from pypom import Region
from selenium.webdriver.support import expected_conditions as EC

from modules.page_base import BasePage
from modules.util import PomUtils


class PanelUi(BasePage):
    """Page Object Model for nav panel UI menu (hamburger menu, application menu)"""

    URL_TEMPLATE = "about:blank"

    class Menu(Region):
        def __init__(self, page, **kwargs):
            super().__init__(page, **kwargs)
            self.utils = PomUtils(self.driver)

        @property
        def loaded(self):
            targeted = [
                el
                for el in self.page.elements.values()
                if "requiredForPage" in el["groups"] and "menuItem" in el["groups"]
            ]
            return all([EC.presence_of_element_located(el) for el in targeted])

    def open_panel_menu(self) -> BasePage:
        with self.driver.context(self.driver.CONTEXT_CHROME):
            panel_root = self.get_element("panel-ui-button")
            panel_root.click()
            self.menu = self.Menu(self, root=panel_root)
        return self

    def select_panel_setting(self, name, *labels):
        with self.driver.context(self.driver.CONTEXT_CHROME):
            panel_option = self.get_element(name, labels=labels)
            panel_option.click()

    def navigate_to_about_addons(self):
        """
        On the hamburger menu > More Tools > Customize Toolbar > Manage Themes
        """
        self.select_panel_setting("more-tools")
        self.select_panel_setting("customize-toolbar")
        with self.driver.context(self.driver.CONTEXT_CHROME):
            self.get_element("manage-themes").click()
