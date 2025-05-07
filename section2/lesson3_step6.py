from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Инициализация браузера
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    
    # 1. Нажимаем на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    button.click()
    
    # 2. Переключаемся на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    # 3. Решаем капчу
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    # Вводим ответ
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)
    
    # Отправляем решение
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    
    # Получаем результат из alert
    alert = browser.switch_to.alert
    print("Код ответа:", alert.text.split()[-1])
    alert.accept()
    
finally:
    # Даем время для просмотра результата
    time.sleep(5)
    # Закрываем все вкладки и браузер
    browser.quit()