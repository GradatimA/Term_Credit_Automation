import time
from tecr_pageobjects.Login import LoginPage
from tecr_utilities.readProperties import ReadConfig
from tecr_utilities.logfile import LogGen


class Test_Login_001:
    appUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    def test_title(self,setup):
        self.logger.info("****** title verifications success *****:")
        self.driver = setup
        self.driver.get(self.appUrl)
        act_title = self.driver.title
        self.logger.info("****** title verifications *****:")
        print(act_title)
        if act_title == "ABSLI":
            self.driver.save_screenshot(".\\tecr_screenshots\\" + "Sample.png")
            self.driver.close()
            assert True

        else:
            self.driver.save_screenshot(".\\tecr_screenshots\\" + "Sample.png")
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
        self.LP.setusername(self.username)
        self.LP.setpassword(self.password)
        time.sleep(3.0)
        self.LP.submit()


