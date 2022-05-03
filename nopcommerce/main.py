# D:/python/automation/selenium/webdriver/geckodriver.exe

from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginTests():

    def test_validLogin(self):
        baseURL = "https://letskodeit.teachable.com/"
        driver = webdriver.Chrome('D:/python/automation/selenium/webdriver/chromedriver.exe')
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        loginLink = driver.find_element(By.LINK_TEXT, "Login")
        loginLink.click()

        emailField = driver.find_element(By.ID, "email")
        emailField.send_keys("test@email.com")

        passwordField = driver.find_element(By.ID, "password")
        passwordField.send_keys("abcabc")

        loginButton = driver.find_element(By.NAME, "commit")
        loginButton.click()

        userIcon = driver.find_element(By.XPATH, ".//*[@id='navbar']//span[text()='User Settings']")
        if userIcon is not None:
            print("Login Successful")
        else:
            print("Login Failed")


    def loggen(self):
        import logging
        ##loging
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename='.\\Logs\\automation.log',
                            filemode='w')
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        # add the handler to the root logger
        logging.getLogger().addHandler(console)
        logging.info("\nParameters:")
        for i in range(10):
            logging.info(i)
        logging.info("end!")

    def test_browser(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By

        driver = webdriver.Chrome()

        driver.get("https://www.google.com")

        driver.title  # => "Google"

        driver.implicitly_wait(0.5)

        search_box = driver.find_element(By.NAME, "q")
        search_button = driver.find_element(By.NAME, "btnK")

        search_box.send_keys("Selenium")
        search_button.click()

        driver.find_element(By.NAME, "q").get_attribute("value")  # => "Selenium"

        driver.quit()

ff = LoginTests()
# ff.test_validLogin()
# ff.loggen()
ff.test_browser()
