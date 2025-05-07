from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    # Инициализация браузера
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    
    # Заполняем текстовые поля
    browser.find_element(By.NAME, "firstname").send_keys("Иван")
    browser.find_element(By.NAME, "lastname").send_keys("Петров")
    browser.find_element(By.NAME, "email").send_keys("test@example.com")
    
    # Создаем временный файл в той же директории, где находится скрипт
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testfile.txt")
    with open(file_path, "w") as file:
        file.write("")  # Создаем пустой файл
    
    # Загружаем файл
    browser.find_element(By.ID, "file").send_keys(file_path)
    
    # Нажимаем кнопку Submit
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
finally:
    # Даем время для копирования результата
    time.sleep(30)
    # Закрываем браузер
    browser.quit()
    
    # Удаляем временный файл, если он был создан
    if os.path.exists(file_path):
        os.remove(file_path)