from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    # Инициализация браузера
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")
    
    # Находим числа и вычисляем их сумму
    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)
    sum_result = str(num1 + num2)
    
    # Выбираем значение из выпадающего списка
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum_result)  # Ищем вариант с вычисленной суммой
    
    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    
finally:
    # Даём время для копирования результата (30 секунд)
    time.sleep(30)
    # Закрываем браузер
    browser.quit()