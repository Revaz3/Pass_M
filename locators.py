from selenium.webdriver.common.by import By


class Locators:
    VOITI_V_AKKAUNT = (By.XPATH, '//*[@id="lgnDiv"]/div[9]/div/span') #Кнопка Войти в аккаунт на главной странице
    POLE_USER_NAME = (By.XPATH, '//*[@id="username"]') #Поле email
    POLE_PASSWORD = (By.XPATH, '//*[@id="password"]') #Поле password






