from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

class ReservationBot():
    def __init__(self, browser_url, username, password):
        self.browser_url = browser_url  # url of the initial browser site
        self.username = username
        self.password = password

    def choose_day(self, day, day_number, time_number):
        browser.get(self.browser_url)
        # self.get_browser().get(self.browser_url)   # initialzie the browser site
        day_tabCSS = f"#pills-tab > li:nth-child({day_number}) > a" # day_number must be a digit from 1-7, corresponding to days of week (Sunday = 1)
        day_moreINFO = f"#{day} > div:nth-child({time_number}) > div > p.orderContainer > a"    # day = day of week, time_number = corresponding number of list of ordered time (3, 5, 7, 9, ...)
        browser.find_element_by_css_selector(day_tabCSS).click()
        browser.find_element_by_css_selector(day_moreINFO).click()
        url = browser.current_url
        return url

    def login(self, day, day_number, time_number):
        url = self.choose_day(day, day_number, time_number)
        browser.get(url)
        register_button = "orderNow"
        browser.find_element_by_class_name(register_button).click()
        username_box = browser.find_element_by_css_selector("#username")
        username_box.click()
        username_box.send_keys(self.username)
        password_box = browser.find_element_by_css_selector("#password")
        password_box.click()
        password_box.send_keys(self.password)
        password_box.submit()
        url = browser.current_url
        return url

    def sign_waivers(self, day, day_number, time_number):
        url = self.login(day, day_number, time_number)
        browser.get(url)
        css_selectorSignwaivers = '#mainContent > div:nth-child(5) > div.small-4.columns.right.end.text-right > a'
        css_termsNagreement = '#mainContent > div > div > form > div:nth-child(10) > input:nth-child(2)'
        css_Liability = '#mainContent > div > div > form > div:nth-child(11) > input:nth-child(2)'
        css_covid = '#mainContent > div > div > form > div:nth-child(9) > input:nth-child(2)'
        css_checkout = '#mainContent > div:nth-child(5) > div.small-5.columns.right.end.text-right > form > input.button.small'
        browser.find_element_by_css_selector(css_selectorSignwaivers).click()
        browser.find_element_by_css_selector(css_termsNagreement).click()
        browser.find_element_by_css_selector(css_Liability).click()
        browser.find_element_by_css_selector(css_covid).click()
        browser.find_element_by_css_selector(css_checkout).click()
