import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistrationForms(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(10)
    
    def tearDown(self):
        self.browser.quit()
    
    def test_registration_form1(self):
        """Тест для страницы registration1.html"""
        self.browser.get("http://suninjuly.github.io/registration1.html")
        
        # Заполняем обязательные поля
        self.browser.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys("Ivan")
        self.browser.find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("Petrov")
        self.browser.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("game@mail.ru")
        self.browser.find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys("961522232")
        self.browser.find_element(By.XPATH, "(//input[@type='text'])[5]").send_keys("russia")


        # Отправляем форму
        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        
        # Проверяем успешность регистрации
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(
            "Congratulations! You have successfully registered!", 
            welcome_text,
            "Сообщение об успешной регистрации не соответствует ожидаемому"
        )
    
    def test_registration_form2(self):
        """Тест для страницы registration2.html"""
        self.browser.get("http://suninjuly.github.io/registration2.html")
        
        # Заполняем обязательные поля
        self.browser.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys("Ivan")
        self.browser.find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("game@mail.ru")
        self.browser.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("8912348129")
        self.browser.find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys("russia")
        
        # Отправляем форму
        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        
        # Проверяем успешность регистрации
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(
            "Congratulations! You have successfully registered!", 
            welcome_text,
            "Сообщение об успешной регистрации не соответствует ожидаемому"
        )

if __name__ == "__main__":
    unittest.main()