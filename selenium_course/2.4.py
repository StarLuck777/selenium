from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет  кликабельной
    price_element = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    input_value_element = browser.find_element(By.ID, "input_value")
    browser.execute_script(
        "arguments[0].scrollIntoView(true);", input_value_element)

    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)

    res = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(res)

    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

finally:

    time.sleep(20)

    browser.quit()
