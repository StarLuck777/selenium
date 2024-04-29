from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Проверяем наличие обязательных полей
    required_fields_present = True
    try:
        browser.find_element(
            By.XPATH, "//input[@placeholder='Input your first name']")
        browser.find_element(
            By.XPATH, "//input[@placeholder='Input your last name']")
        browser.find_element(
            By.XPATH, "//input[@placeholder='Input your email']")
    except NoSuchElementException:
        required_fields_present = False

    if not required_fields_present:
        print("Required fields are missing on this page!")
    else:
        # Заполняем обязательные поля
        input1 = browser.find_element(
            By.XPATH, "//input[@placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(
            By.XPATH, "//input[@placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(
            By.XPATH, "//input[@placeholder='Input your email']")
        input3.send_keys("777@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # Проверяем, что нет сообщения об успешной регистрации (для второй страницы)
        success_message_present = True
        try:
            browser.find_element(By.TAG_NAME, "h1")
        except NoSuchElementException:
            success_message_present = False

        if success_message_present:
            print("Unexpected success message on this page!")
        else:
            print("Form submitted successfully on this page.")

finally:
    # Ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # Закрываем браузер после всех манипуляций
    browser.quit()
