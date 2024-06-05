import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import secret


class Browser:
    browser, service = None, None

    # Initialize the webdriver with the path to chromedriver.exe
    def _init_(self,driver: str):
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)

    def open_page(self,url: str):
        self.browser.get(url)
    
    def close_browser(self):
        self.browser.close()

    #Linked In  Video No #2

    def add_input(self, by: By, value: str, text: str):
        field = self.browser.find_element(by=by, value=value)
        field.send_keys(text)
        time.sleep(1)

    def click_button(self,by: By, value: str):
        button = self.browser.find_element(by=by, value=value)
        button.click()
        time.sleep(1)
    
    def login_linkedin(self, username: str, password: str):
        self.add_input(by=By.ID, value='email-or-phone', text=username)
        self.add_input(by=By.ID, value='password', text=password)
        self.click_button(by=By.CLASS_NAME, value='join-form__form-body-submit-button')
     


if __name__ == '_main_':
    browser = Browser ('drivers\chromedriver.exe')
    #browser.open_page('https://www.google.com')
    #time.sleep(3)
    #browser.open_page('https://pycontent.org')
    #time.sleep(3)
    #browser.close_browser()
    browser.open_page('https://www.linkedin.com/signup/cold-join')
    time.sleep(10)


    browser.login_linkedin(secret.email, secret.password)
    time.sleep(100)
    browser.close_browser()