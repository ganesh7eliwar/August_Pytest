from selenium.common import NoSuchElementException


class Test_Credence_Checkout:

    def test_checkout_003(self):
        import time

        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.select import Select

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://automation.credence.in/login')
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@id='email']").send_keys('7eliwar.ganesh@gmail.com')
        time.sleep(1)

        driver.find_element(By.XPATH, "//input[@id='password']").send_keys('s@t07Ganesh')
        time.sleep(1)

        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # 1st Product

        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/a[1]/img[1]").click()
        time.sleep(1)

        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        time.sleep(1)

        driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()

        # 2nd Product

        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[3]/div[1]/div[1]/a[1]/img[1]").click()
        time.sleep(1)

        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        time.sleep(1)

        driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()

        # 3rd Product

        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[4]/div[1]/div[1]/a[1]/img[1]").click()
        time.sleep(1)

        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        time.sleep(1)

        # Proceed to Checkout
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/a[2]").click()
        time.sleep(1)

        # Checkout Page
        # First Name
        driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys('Ganesh')
        time.sleep(1)

        # Last Name
        driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys('Sateliwar')
        time.sleep(1)

        # Mobile No.
        driver.find_element(By.XPATH, "//input[@id='phone']").send_keys(8237327387)
        time.sleep(1)

        # Address
        driver.find_element(By.XPATH, "//textarea[@id='address']").send_keys('Bhokar, Nanded, Maharashtra, 431801')
        time.sleep(1)

        # Zip Code
        driver.find_element(By.XPATH, "//input[@id='zip']").send_keys(431801)
        time.sleep(1)

        # State Selection
        state = Select(driver.find_element(By.XPATH, "//select[@id='state']"))
        state.select_by_visible_text('Pune')
        time.sleep(1)

        # Card Details
        # Owner Name
        driver.find_element(By.XPATH, "//input[@id='owner']").send_keys("Ganesh Sateliwar")
        time.sleep(1)

        # Master Card CVV
        # driver.find_element(By.XPATH, "//input[@id='cvv']").send_keys('043')
        # time.sleep(1)

        # Master Card
        # driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys('5281')
        # driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys('0370')
        # driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys('4891')
        # driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys('6168')

        # year
        # year = Select(driver.find_element(By.XPATH, "//select[@id='exp_year']"))
        # year.select_by_index(4)
        # time.sleep(1)

        # month
        # month = Select(driver.find_element(By.XPATH, "//select[@id='exp_month']"))
        # month.select_by_index(7)
        # time.sleep(1)

        # Visa CVV
        # driver.find_element(By.XPATH, "//input[@id='cvv']").send_keys('257')
        # time.sleep(1)

        # Visa
        # driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys('4716')
        # driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys('1089')
        # driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys('9971')
        # driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys('6531')

        # year
        # year = Select(driver.find_element(By.XPATH, "//select[@id='exp_year']"))
        # year.select_by_index(5)
        # time.sleep(1)

        # month
        # month = Select(driver.find_element(By.XPATH, "//select[@id='exp_month']"))
        # month.select_by_index(12)
        # time.sleep(1)

        # American Express CVV
        driver.find_element(By.XPATH, "//input[@id='cvv']").send_keys('3156')
        time.sleep(1)

        # American Express
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys('3424')
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys('988186')
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys('30298')

        # year
        year = Select(driver.find_element(By.XPATH, "//select[@id='exp_year']"))
        year.select_by_index(4)
        time.sleep(1)

        # month
        month = Select(driver.find_element(By.XPATH, "//select[@id='exp_month']"))
        month.select_by_index(5)
        time.sleep(1)

        # Continue Checkout
        driver.find_element(By.XPATH, "//button[@id='confirm-purchase']").click()
        time.sleep(5)

        try:
            print('\n', driver.find_element(By.XPATH, "//p[@class='lead w-lg-50 mx-auto']").text)
            assert True

        except NoSuchElementException:
            print('Checkout Failed')
            assert False

        time.sleep(5)
        driver.quit()
