import pytest
from tecr_pageobjects.Login import LoginPage
from tecr_utilities.readProperties import ReadConfig
from tecr_utilities.logfile import LogGen
from tecr_utilities import ExcelUtility
import time
from selenium.webdriver.firefox.options import Options



class Test_002_DDT_Login():
    baseURL = ReadConfig.getApplicationUrl()
    path = ".//tecr_TestData/LoginData.xlsx"
    logger = LogGen.loggen()  # Logger
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("******* Starting Test_002_DDT_Login Test **********")
        self.logger.info("******* Starting Login DDT Test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.LP = LoginPage(self.driver)

        self.rows = ExcelUtility.getRowCount(self.path, 'Sheet1')
        self.Col = ExcelUtility.getRowCount(self.path, 'Sheet1')
        print('Number of rows...',self.rows)
        lst_status=[]

        for r in range(2,self.rows+1):
            self.user = ExcelUtility.readData(self.path, 'Sheet1', r, 1)
            self.password = ExcelUtility.readData(self.path, 'Sheet1', r, 2)
            self.exp = ExcelUtility.readData(self.path, 'Sheet1', r, 3)

            self.LP.setusername(self.user)
            self.LP.setpassword(self.password)
            self.LP.submit()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "ABSLI"

            if act_title==exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** passed ****")
                lst_status.append("Pass")
                self.driver.get(self.baseURL)
            elif self.exp == 'Fail':
                self.logger.info("**** failed ****")
                lst_status.append("Pass")
                self.driver.get(self.baseURL)


            elif act_title != exp_title:
                if self.exp == 'Pass':
                     self.logger.info("**** failed ****")
                     lst_status.append("Pass")
                elif self.exp == 'Fail':
                    self.logger.info("**** passed ****")
                    lst_status.append("Pass")
            print(lst_status)
        if "Fail" not in lst_status:
            self.logger.info("******* DDT Login test passed **********")
            assert True

        else:
            self.logger.info("******* DDT Login test failed **********")
            assert False
        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ")


