from selenium.webdriver import Keys

from buse.buse_page import Buse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilites.logs_file import Logger
import allure



class Detal_page(Buse):



    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # Lacation

    detals_btn = "//tr[contains(@class,'first_item')]//a[@class='btn btn-default button button-small']"
    select_rew = "//select[@name='id_product']"
    tesxt_masage = "//textarea[@name='msgText']"
    home_btn = "//span[normalize-space()='Home']"



    # Geters


    def get_tesxt_masage(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.tesxt_masage )))

    def get_detals_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.detals_btn )))


    def get_select_rew(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.select_rew )))

    def get_home_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.home_btn)))






    # ACTIONS


    def find_tesxt_masage(self ,tesxt_masage ):
        self.get_tesxt_masage().send_keys(tesxt_masage)
        print("Input 'Test' text")


    def clcik_detals_btn(self):
        self.get_detals_btn().click()
        print("Click details button")



    def clcik_select_rew(self):
        self.get_select_rew().click()
        print("Click Review ")


    def clcik_select_rew_2(self):
        self.get_select_rew().send_keys(Keys.ARROW_DOWN)
        print("Click arrow down")

    def clcik_select_rew_3(self):
        self.get_select_rew().send_keys(Keys.RETURN)
        print("Click Enter")

    def click_home_btn(self):
        self.get_home_btn().click()
        print("Click go to Home button")








    # Method

    def detals_ofer(self):
        with allure.step("detals_ofer"):
            Logger.add_start_step(method="detals_ofer")
            self.get_current_url()
            self.clcik_detals_btn()
            self.get_scroll_pqge_3()
            self.find_tesxt_masage("test test tes ")
            self.clcik_select_rew()
            self.clcik_select_rew_2()
            self.clcik_select_rew_3()
            self.click_home_btn()
            self.get_screenshot()
            Logger.add_end_step(url=self.get_current_url(),method="detals_ofer")










