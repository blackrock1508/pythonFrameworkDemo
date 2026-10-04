class AutomationPracticeForm:
    def __init__(self, page):
        self.page = page
        self.first_name_input = page.locator("#firstName")
        self.last_name_input = page.locator("#lastName")
        self.email_input = page.locator("#userEmail")
        self.gender_radio_male = page.locator("#gender-radio-1")
        self.hobbies_sports = page.get_by_label("Sports")
        self.hobbies_reading = page.get_by_label("Reading")
        self.state_combobox = page.get_by_role("combobox").last
        self.city_combobox = page.get_by_role("combobox").nth(2)

    def fill_first_name(self, name):
        self.first_name_input.fill(name)

    def fill_last_name(self, name):
        self.last_name_input.fill(name)

    def fill_email(self, email):
        self.email_input.fill(email)

    def select_gender(self):
        self.gender_radio_male.check()

    def check_hobbies(self):
        self.hobbies_sports.check()
        self.hobbies_reading.check()

    def select_state(self, state):
        self.state_combobox.scroll_into_view_if_needed()
        self.state_combobox.click()
        self.state_combobox.fill(state)
        self.page.wait_for_timeout(2000)
        self.page.get_by_text(state, exact=True).click()

    def select_city(self, city):
        self.city_combobox.scroll_into_view_if_needed()
        self.city_combobox.click()
        self.city_combobox.fill(city)
        self.page.wait_for_timeout(2000)
        self.page.get_by_text(city, exact=True).click()
