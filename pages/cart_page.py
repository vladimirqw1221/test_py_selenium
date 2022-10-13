from buse.buse_page import Buse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilites.logs_file import Logger
import allure



class Cart(Buse):



    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # Lacation

    progress_checkout = "//a[@class='button btn btn-default standard-checkout button-medium']"
    progress_addres = "//button[@name='processAddress']//span[contains(text(),'Proceed to checkout')]"
    # check_box_service = "#cgv"
    progress_shipping = "//button[@name='processCarrier']//span[contains(text(),'Proceed to checkout')]"
    pay_bank_btn = "//a[@title='Pay by bank wire']"
    aseert_word = "//h1[normalize-space()='Order summary']"
    button_conf_my_order = "//span[normalize-space()='I confirm my order']"
    link_back_order = "//a[normalize-space()='Back to orders']"


    # Geters

    def get_progress_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.progress_checkout )))

    def get_progress_addres(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.progress_addres )))


    def get_progress_shipping(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.progress_shipping )))

    def get_pay_bank_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.pay_bank_btn )))

    def get_aseert_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.aseert_word)))

    def get_button_conf_my_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_conf_my_order)))

    def get_link_back_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_back_order)))



    # ACTIONS

    def click_progress_checkout(self):
        self.get_progress_checkout().click()
        print("Click Progress order 1")


    def click_progress_addres(self):
        self.get_progress_addres().click()
        print("Click Progress order 2 ")


    def click_progress_shipping(self):
        self.get_progress_shipping().click()
        print("Click Progress order 3")

    def click_pay_bank_btn(self):
        self.get_pay_bank_btn().click()
        print("Choose Payment Method")

    def click_button_conf_my_order(self):
        self.get_button_conf_my_order().click()
        print("Click button 'I confirm my order'")

    def click_link_back_order(self):
        self.get_link_back_order().click()
        print("Click on button my order")



    # Method
    def cart_path(self):
        with allure.step("cart_path"):
            Logger.add_start_step(method="cart_path")
            self.get_current_url()
            self.get_scroll_pqge_2()
            self.click_progress_checkout()
            self.click_progress_addres()
            self.get_scroll_pqge_2()
            self.get_clcik_check_box()
            self.click_progress_shipping()
            self.click_pay_bank_btn()
            self.assert_word(self.get_aseert_word(),"ORDER SUMMARY")
            self.click_button_conf_my_order()
            self.get_screenshot()
            self.click_link_back_order()
            Logger.add_end_step(url=self.get_current_url(),method="cart_path")









