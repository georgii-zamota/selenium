import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    yield driver
    driver.quit()

def test_stepik_auth(browser):
    # 1. Открываем страницу урока
    expected_url = "https://stepik.org/lesson/236895/step/1"
    browser.get(expected_url)
    
    # Проверка начального URL
    assert browser.current_url == expected_url, \
        "Не удалось открыть начальную страницу урока"
    
    # 2. Нажимаем кнопку входа
    login_button = browser.find_element(By.CSS_SELECTOR, "a.navbar__auth_login")
    login_button.click()
    
    # 3. Заполняем форму авторизации
    email_input = browser.find_element(By.ID, "id_login_email")
    email_input.send_keys("*")
    
    password_input = browser.find_element(By.ID, "id_login_password")
    password_input.send_keys("*")
    
    # 4. Отправляем форму
    submit_button = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn")
    submit_button.click()
    
    # 5. Проверяем, что остались на той же странице
    WebDriverWait(browser, 15).until(
        EC.url_to_be(expected_url)
    )
    
    # Дополнительная проверка видимости элементов страницы
    WebDriverWait(browser, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".lesson-header"))
    )
    
    # 6. Проверка финального URL
    current_url = browser.current_url
    assert current_url == expected_url, \
        f"После авторизации URL изменился. Ожидался: {expected_url}, получен: {current_url}"