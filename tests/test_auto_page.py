import time

from pages.autorezation import Autorezation
from selenium import webdriver

from pages.cart_page import Cart
from pages.detals_page import Detal_page
from pages.select_product import Select_product
import allure

@allure.description("Test 1")
def test_on_start():
    driver = webdriver.Chrome(executable_path='/Users/user/Desktop/resourse/chromedriver')


    print("start test ")


    a = Autorezation(driver)
    a.start_loggin()

    sp = Select_product(driver)
    sp.select_product()

    c = Cart(driver)
    c.cart_path()

    dp = Detal_page(driver)
    dp.detals_ofer()


    time.sleep(8)


    print("Finish test")




