from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Инициализация браузера
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    browser.find_element("xpath","//*[@type='submit']").click()
    confirm = browser.switch_to.alert
    confirm.accept()

    browser.get("https://suninjuly.github.io/alert_redirect.html?")
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)    
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(y)
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()




finally:
    # Даем время для копирования результата
    time.sleep(30)
    # Закрываем браузер
    browser.quit()
