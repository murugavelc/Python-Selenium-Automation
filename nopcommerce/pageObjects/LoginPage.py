from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_xpath = '//*[@id="Email"]'
    textbox_password_xpath = '//*[@id="Password"]'
    button_login_xpath = "//button[contains(text(),'Log in')]"
    link_logout_link_xpath = "//a[contains(text(),'Logout')]"
    link_logout_link_text = 'Logout'

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        logout = self.driver.find_element(By.XPATH, self.link_logout_link_xpath)
        self.driver.execute_script("arguments[0].click();", logout)
       # logout = self.driver.find_element(By.LINK_TEXT, self.link_logout_link_text)
       # self.driver.execute_script("arguments[0].click();", logout)
       # self.driver.find_element(By.LINK_TEXT, self.link_logout_link_text).click()
       # self.driver.find_element(By.XPATH, self.link_logout_link_xpath).click()


