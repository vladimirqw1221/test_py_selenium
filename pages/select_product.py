import allure

from buse.buse_page import Buse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilites.logs_file import Logger


# njknkjn@gmail.com
# 1733392qwe@
class Select_product(Buse):



    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # Lacation

    women_li = "//a[@title='Women']"
    tops_select = "//a[@title='Faded Short Sleeve T-shirts']"
    add_to_cart = "//button[@name='Submit']"
    inform_win = "//iframe[@id='fancybox-frame1665549148525']"
    button_checkount ="//a[@title='Proceed to checkout']"


    # Geters

    def get_women_li(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.women_li )))


    def get_tops_select(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH,self.tops_select )))


    def get_inform_win(self):
        return WebDriverWait(self.driver, 30).until(EC.frame_to_be_available_and_switch_to_it((0)))


    def get_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.add_to_cart )))


    def get_button_checkount(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.button_checkount )))


    # ACTIONS

    def clcik_women_li(self):
        self.get_women_li().click()
        print("Click section")


    def clcik_tops_select(self):
        self.get_tops_select().click()
        print("Click PDP Tops")


    def open_inform_win(self):
        self.get_inform_win()
        print("Iframe opens")


    def clcik_add_to_cart(self):
        self.get_add_to_cart().click()
        print(" Click button 'Add to cart'")

    def click_button_checkount(self):
        self.get_button_checkount().click()
        print("Click on button Checkout")


    # Method

    def select_product(self):
        with allure.step("select_product"):
            Logger.add_start_step(method="select_product")
            self.get_current_url()
            self.clcik_women_li()
            self.get_scroll_pqge()
            self.clcik_tops_select()
            self.open_inform_win()
            self.clcik_add_to_cart()
            self.click_button_checkount()
            Logger.add_end_step(url=self.get_current_url(),method="select_product")








