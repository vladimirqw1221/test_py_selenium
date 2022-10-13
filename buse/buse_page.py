import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


class Buse():
    def __init__(self , driver):
        self.driver = driver

    """Current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Corrent URL " + get_url)

    """Scroll page"""

    def get_scroll_pqge(self):
        self.driver.execute_script("window.scrollTo(0, 800)")
        print("Scroll done")

    def get_scroll_pqge_2(self):
        self.driver.execute_script("window.scrollTo(0, 500)")
        print("Scroll done")


    def get_scroll_pqge_3(self):
        self.driver.execute_script("window.scrollTo(0, 1700)")
        print("Scroll done")


    """Methosd chech box clcik is not DOM"""

    def get_clcik_check_box(self):
        self.driver.execute_script("document.querySelector('#cgv').click();")
        print("Toogle on click ")


    """Assert word """

    def assert_word(self, word , result):
        value_word = word.text
        assert value_word == result
        print("Good value word")


    """Method screenshot"""

    def get_screenshot(self):
        new_date = datetime.datetime.utcnow().strftime("%Y. %m. %d. %H.%M. %S")
        name_screenshot  = 'screenshot ' + new_date + '.png'
        self.driver.save_screenshot("/Users/user/Desktop/auto_test_selem777/scren/" + name_screenshot)
        print("Screenshot added")





















