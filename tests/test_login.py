from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import Data
from conftest import driver
import time

class Testlogshapka:
    def test_login_shapka(self, driver):
        driver.find_element(*Locators.POLE_USER_NAME).send_keys(Data.EMAIL)  # Поле email
        time.sleep(2)
        driver.find_element(*Locators.POLE_PASSWORD).send_keys(Data.PASSWORD)  # Поле password
        time.sleep(2)
        driver.find_element(*Locators.VOITI_V_AKKAUNT).click()  # Кнопка войти после ввода емейла и пароля

        #button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.KNOPKA_OFORMIT_ZAKAZ))  # Кнопка оформить заказ на главной странице
        #assert button.is_displayed(), "Кнопка 'Оформить заказ' не отображается на странице"