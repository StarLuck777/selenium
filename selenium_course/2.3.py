from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    # Инициализация драйвера браузера (Chrome)
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)

    res = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(res)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Ждем немного перед закрытием браузера, чтобы увидеть результат
    time.sleep(10)
    # Закрываем браузер после всех операций
    browser.quit()
