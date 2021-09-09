import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

valid_email = "s.dobiech@gmail.com"
invalid_pswd = "haslo"

class Registration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.castorama.pl/")
        self.driver.implicitly_wait(5)

    def testInvalidPassword(self):
        driver=self.driver
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.NAME,"Zaakceptuj")))
        driver.find_element_by_name("Zaakceptuj").click()
        sleep(5)
        driver.find_element_by_xpath('//a[@title="Logowanie i rejestracja"]').click()
        sleep(5)
        email_input = driver.find_element_by_id("email_address")
        email_input.send_keys(valid_email)
        pswd_input = driver.find_element_by_id("password")
        pswd_input.send_keys(invalid_pswd)
        pswd2_input = driver.find_element_by_name("confirmation")
        pswd2_input.send_keys(invalid_pswd)
        driver.find_element_by_xpath('//label[@for="is_accept"]').click()
        sleep(5)
        driver.find_element_by_xpath('//form[@id="form-validate-register"]//button[@type="submit"]').click()
        sleep(5)

        error_messages = driver.find_elements_by_xpath('//div[@class="validation-advice"]')
        visible_error_notices = list()
        for error in error_messages:
                if error.is_displayed():
                    visible_error_notices.append(error)

        self.assertEqual(len(visible_error_notices), 1, msg="Liczba widocznych komunikatow nie zgadza sie!")
        self.assertEqual(visible_error_notices[0].text, "Hasło powinno składać się co najmniej z 8 znaków: dużej litery, małej litery, cyfry lub znaku specjalnego (!\\'^£$%&*()}{@#~?><>,|=_+¬-]).")


    def tearDown(self):
        self.driver.quit()




if __name__ == "__main__":
    unittest.main(verbosity=2)
