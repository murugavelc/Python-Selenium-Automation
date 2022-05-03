import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//testData/loginData.xlsx"
    logger = LogGen.logger()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("========== Starts Test_002_DDT_Login ===========")
        self.logger.info("************ Verifying Login DDT test ************")
        self.driver = setup  # initialize driver from setup fixture method
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows in excel:", self.rows)

        self.lst_status = []  # Empty list variable for list of status

        for r in range(2, self.rows+1):
            self.username = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)

            self.lp.setUsername(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == "pass":
                    self.logger.info("************  Login DDT test is passed ************")
                    time.sleep(5)
                    self.lp.clickLogout()
                    self.lst_status.append("Pass")
                elif self.exp == "fail":
                    self.logger.info("************  Login is failed ************")
                    time.sleep(5)
                    self.lp.clickLogout()
                    self.lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == "pass":
                    self.logger.info("************  Login is failed ************")
                    time.sleep(5)
                    self.lp.clickLogout()
                    self.lst_status.append("Fail")
                elif self.exp == "fail":
                    self.logger.info("************  Login is passed ************")
                    time.sleep(5)
                    self.lp.clickLogout()
                    self.lst_status.append("Pass")

        if "fail" not in self.lst_status:
            self.logger.info("************  Login DDT test is passed... ************")
            self.driver.close()
            assert True
        else:
            self.logger.error("************  Login DDT test is failed... ************")
            self.driver.close()
            assert False
        self.logger.info("========  End of Login DDT test ==========")
        self.logger.info("========  Completed TC_LoginDDT_002  ==========")
