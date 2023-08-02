class Test_Multiple_Windows:

    def test_multiple_windows(self):
        import time

        from selenium import webdriver
        from selenium.webdriver.common.by import By

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")

        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        # time.sleep(1)

        driver.get("https://the-internet.herokuapp.com/windows")
        # time.sleep(1)
        driver.find_element(By.XPATH, "//a[normalize-space()='Click Here']").click()
        # time.sleep(1)
        select_window = driver.window_handles
        driver.switch_to.window(select_window[1])
        print('\n', driver.find_element(By.XPATH, "//h3[normalize-space()='New Window']").text)
        # time.sleep(1)
        driver.close()
        driver.switch_to.window(select_window[0])
        print('\n', driver.find_element(By.XPATH, "//h3[normalize-space()='Opening a new window']").text)
        # time.sleep(2)
        driver.quit()

