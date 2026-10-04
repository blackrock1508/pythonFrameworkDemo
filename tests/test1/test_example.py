from playwright.sync_api import Page, expect
import pytest

@pytest.mark.readonly
def test_playwright_example(page: Page):
    # Navigate to the example page
    page.goto("https://demoqa.com/automation-practice-form")
    page.get_by_role("textbox", name="First Name").click()
    page.get_by_role("textbox", name="First Name").fill("ashsdas")
    page.get_by_role("textbox", name="First Name").press("Tab")
    page.get_by_role("textbox", name="Last Name").fill("sdjhf")
    page.get_by_role("textbox", name="name@example.com").fill("fejejf@hddfh")
    page.locator("div").filter(has_text=re.compile(r"^Male$")).click()
    page.get_by_role("textbox", name="Mobile Number").fill("343739343")
    page.locator("#dateOfBirthInput").click()
    page.get_by_role("gridcell", name="Choose Tuesday, October 20th,").click()
    page.locator(".subjects-auto-complete__input-container").click()
    page.locator("#subjectsInput").fill("dj")
    page.get_by_role("checkbox", name="Sports").check()
    page.locator(".subjects-auto-complete__input-container").click()
    page.locator("#subjectsInput").fill("efhehf")       
    page.locator("#currentAddress-wrapper").click()
    page.locator(".css-8mmkcg").first.click()
    page.get_by_role("option", name="NCR").click()
    page.locator("#city > .css-13cymwt-control > .css-hlgwow > .css-19bb58m").click()
    page.get_by_role("option", name="Delhi").click()
