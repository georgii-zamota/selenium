import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    # Инициализация драйвера с неявным ожиданием
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # Неявное ожидание 10 секунд
    yield driver
    driver.quit()

def test_registration_form1(browser):
    """Тест для страницы registration1.html"""
    browser.get("http://suninjuly.github.io/registration1.html")
    
    # Заполнение полей формы
    browser.find_element(By.XPATH, "//input[contains(@class, 'first')]").send_keys("Ivan")
    browser.find_element(By.XPATH, "//input[contains(@class, 'second')]").send_keys("Petrov")
    browser.find_element(By.XPATH, "//input[contains(@class, 'third')]").send_keys("game@mail.ru")
    browser.find_element(By.XPATH, "//input[contains(@class, 'first') and @type='text']").send_keys("961522232")
    browser.find_element(By.XPATH, "//input[contains(@class, 'second') and @type='text']").send_keys("russia")

    # Отправка формы
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    
    # Проверка результата (неявное ожидание уже работает)
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert welcome_text == "Congratulations! You have successfully registered!", \
        f"Ожидалось 'Congratulations!', получено '{welcome_text}'"

def test_registration_form2(browser):
    """Тест для страницы registration2.html"""
    browser.get("http://suninjuly.github.io/registration2.html")
    
    # Заполнение полей формы
    browser.find_element(By.XPATH, "//input[contains(@class, 'first')]").send_keys("Ivan")
    browser.find_element(By.XPATH, "//input[contains(@class, 'second')]").send_keys("game@mail.ru")
    browser.find_element(By.XPATH, "//input[contains(@class, 'third')]").send_keys("8912348129")
    browser.find_element(By.XPATH, "//input[contains(@class, 'first') and @type='text']").send_keys("russia")
    
    # Отправка формы
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    
    # Проверка результата
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert welcome_text == "Congratulations! You have successfully registered!", \
        f"Ожидалось 'Congratulations!', получено '{welcome_text}'"