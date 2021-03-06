import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

# Test case for login
class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.logger()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("************ Test_001_Login ************")
        self.logger.info("************ Verifying Home page title  ************")
        self.driver = setup  # initialize driver from setup fixture method
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************ Home page title test is passed ************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("************ Home page title test is failed ************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("************ Verifying Login test ************")
        self.driver = setup  # initialize driver from setup fixture method
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            time.sleep(3)
            self.lp.clickLogout()  # Logout action
            time.sleep(5)
            self.driver.close()
            self.logger.info("************  Login test is passed ************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("************  Login test is failed ************")
            assert False
