
import time

import pytest

from tecr_pageobjects.Login import LoginPage
from tecr_utilities.readProperties import ReadConfig
from tecr_utilities.logfile import LogGen




class Test_Login_002:
    appUrl = ReadConfig.getApplicationUrl()
    UN= ReadConfig.getUsername()
    PW = ReadConfig.getPassword()
    logger = LogGen.loggen()


    def test_title_001(self,setup):
        self.logger.info("****** title verifications *****:")
        self.driver = setup
        self.driver.get(self.appUrl)
        act_title = self.driver.title
        self.logger.info("****** title verifications *****:")
        print(act_title)
        if act_title == "ABSLI":
            self.driver.save_screenshot(".\\tecr_screenshots" + "Sample.png")
            self.driver.close()
            assert True

        else:
            self.driver.save_screenshot(".\\tecr_screenshots" + "Sample.png")
            time.sleep(3)
            self.driver.close()
            assert False


    def testlogo(self,setup):
        self.logger.info("****** title verifications *****:")
        self.driver = setup
        self.driver.get(self.appUrl)
        self.LP = LoginPage(self.driver)
        self.LP.logo()
        self.driver.quit()


    def testlogin(self,setup):
        self.driver = setup
        self.driver.get(self.appUrl)
        self.LP = LoginPage(self.driver)
        self.LP.setusername(self.UN)
        self.LP.setpassword(self.PW)
        self.LP.submit()

