import time

import pytest
from playwright.sync_api import Page,expect
from  pages.automation_practice_form import AutomationPracticeForm 
from pathlib import Path
import json

# Load registration data from JSON file
with open(Path("testdata/registration_data.json")) as f:
    registration_data = json.load(f)

class TestLogin:

    @pytest.mark.smoke 
    @pytest.mark.parametrize("data", registration_data)
    def test_login_smoke(self, page: Page, data):
        page.goto("https://demoqa.com/automation-practice-form")
        time.sleep(2)  # Wait for the page to load completely
        page.goto("https://demoqa.com/elements")
        time.sleep(2)  # Wait for the page to load completely
        page.go_back()    
        time.sleep(5)  # Wait for the page to load completely
        page.wait_for_load_state("load")  # Wait for network requests to finish
        form = AutomationPracticeForm(page)
        form.fill_first_name(data["first_name"])    
        form.fill_last_name(data["last_name"])
        form.fill_email(data["email"])
        form.select_gender()
        form.check_hobbies()        
        form.select_state(data["state"])    
        form.select_city(data["city"])
        form.page.wait_for_timeout(2000)
        form.page.screenshot(path=f"screenshots/test_login_smoke_{data['first_name']}_{data['last_name']}.png")
        form.page.wait_for_timeout(2000)
    
      