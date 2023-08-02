import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class Test_Credence:

    def test_sum_001(self):
        a = 5
        b = 2
        sum = a + b
        print("Sum of a and b is: " + str(sum))
        if sum == 7:
            assert True
        else:
            assert False

    def test_credence_login(self):
        # 1. Open Browser
        driver = webdriver.Chrome()
        driver.maximize_window()
        # time.sleep(5)

        # 2. Go To URL
        driver.get('https://automation.credence.in/login')
        # time.sleep(2)

        # 3. Enter login credentials
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys('7eliwar.ganesh@gmail.com')
        # time.sleep(2)

        # 4. Enter Password
        driver.find_element(By.CSS_SELECTOR, 'input[id="password"]').send_keys('s@t07Ganesh')
        # time.sleep(2)

        # 5. Click on login
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)

        try:
            print('Login Successful')
            driver.find_element(By.XPATH, '//h2[normalize-space()="CredKart"]')
            assert True

        except NoSuchElementException:
            print('Login Failed')
            assert False

        driver.quit()
