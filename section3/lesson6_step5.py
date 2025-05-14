import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.mark.parametrize('link', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
])
def test_alien_message(browser, link):
    # Открываем страницу
    browser.get(link)
    
    # Авторизация
    login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.navbar__auth_login")))
    login_button.click()
    
    email_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "id_login_email")))
    email_input.send_keys("*")
    
    password_input = browser.find_element(By.ID, "id_login_password")
    password_input.send_keys("*")
    
    submit_button = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn")
    submit_button.click()
    
    # Ждем загрузки страницы после авторизации
    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "textarea")))
    
    
    # Вводим ответ
    answer_field = browser.find_element(By.CSS_SELECTOR, "textarea")
    answer = str(math.log(int(time.time())))
    answer_field.clear()
    answer_field.send_keys(answer)
    
    
    # Нажимаем кнопку "Отправить"
    submit_button = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable(("xpath", "button[type='button']")))
    submit_button.click()
    
    
    # Ожидаем перезагрузки страницы и появления фидбека
    # После нажатия кнопки страница может перезагрузиться, поэтому:
    # 1. Ждем исчезновения кнопки отправки (старой)
    WebDriverWait(browser, 30).until(
        EC.staleness_of(submit_button))
    
    # 2. Ждем появления нового элемента фидбека
    feedback = WebDriverWait(browser, 30).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text
    
    # Проверяем фидбек и собираем сообщение
    assert feedback == "Correct!"
       