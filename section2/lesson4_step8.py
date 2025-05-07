from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Инициализация браузера
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    # Ожидаем, когда цена станет $100 (ждём не менее 12 секунд)
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    
    # Нажимаем кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()
    
    # Решаем математическую задачу
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    # Вводим ответ
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)
    
    # Отправляем решение
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()
    
finally:
    # Даём время для копирования результата
    time.sleep(10)
    # Закрываем браузер
    browser.quit()