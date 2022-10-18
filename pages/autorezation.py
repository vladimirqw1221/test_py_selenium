from buse.buse_page import Buse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilites.logs_file import Logger
import allure


class Autorezation(Buse):

    url = "http://automationpractice.com/index.php"

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # Lacation


    sign_in_btn = ".header_user_info "
    find_email = "//input[@id='email']"
    find_password = "//input[@id='passwd']"
    btn_sign_in = "//button[@id='SubmitLogin']"



    # Geters

    def get_sign_in_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,self.sign_in_btn )))


    def get_find_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.find_email )))


    def get_find_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.find_password )))


    def get_btn_sign_in(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.btn_sign_in )))



    # ACTIONS


    def click_sign_in_btn(self):
        self.get_sign_in_btn().click()
        print("Click button Login")

    def input_find_email(self,find_email ):
        self.get_find_email().send_keys(find_email)
        print("Enter Email")


    def input_find_password(self,find_password ):
        self.get_find_password().send_keys(find_password)
        print("Enter Password")


    def click_btn_sign_in(self):
        self.get_btn_sign_in().click()
        print("Click button Sign In ")



    # Method
    def start_loggin(self):
        with allure.step("start_loggin"):
            Logger.add_start_step(method="start_loggin")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_sign_in_btn()
            self.input_find_email("njknkjn@gmail.com")
            self.input_find_password("1733392qwe@")
            self.click_btn_sign_in()
            Logger.add_end_step(url=self.get_current_url(),method="start_loggin")




