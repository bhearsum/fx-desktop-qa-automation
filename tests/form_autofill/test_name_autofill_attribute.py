import pytest
from selenium.webdriver import Firefox

from modules.browser_object import Navigation
from modules.browser_object_autofill_popup import AutofillPopup
from modules.page_object import AddressFill
from modules.util import Utilities

countries = ["CA", "US"]


@pytest.mark.parametrize("country_code", countries)
def test_address_attribute_selection(driver: Firefox, country_code: str):
    """
    C122356 - This test verifies that after filling the autofill fields and saving the data, hovering over the first
    item in the dropdown ensures that the actual value matches the expected value.
    """
    # Instantiate objects and open the navigation page
    Navigation(driver).open()
    address_form_fields = AddressFill(driver).open()
    autofill_popup_panel = AutofillPopup(driver)
    util = Utilities()

    # Create fake data, fill in the form, and press submit and save on the doorhanger
    autofill_sample_data = util.fake_autofill_data(country_code)
    address_form_fields.save_information_basic(autofill_sample_data)
    autofill_popup_panel.press_doorhanger_save()

    # Double-click on the name field to trigger the autocomplete dropdown
    address_form_fields.double_click("form-field", labels=["name"])

    # Get the first element from the autocomplete dropdown
    first_item = autofill_popup_panel.get_nth_element(1)
    actual_value = autofill_popup_panel.hover_over_element(
        first_item, chrome=True
    ).get_primary_value(first_item)

    # Get the primary value (street address) from the first item in the dropdown and assert that the actual value
    # matches the expected value
    expected_name = autofill_sample_data.name
    assert (
        expected_name == actual_value
    ), f"Expected {expected_name}, but got {actual_value}"
