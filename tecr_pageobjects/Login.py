from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_id= "ContentPlaceHolder1_txtUserName"
    textbox_password_xpath = "//body[1]/form[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[3]/input[1]"
    LoginBtn_id = "ContentPlaceHolder1_btnSubmit"
    logo_xpath = "//body/form[@id='ctl00']/div[@id='ContentPlaceHolder1_upLoginPage']/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]"
    Logout_xpath="//body[1]/form[1]/div[4]/nav[1]/ul[1]/li[17]/a[1]"

    def __init__(self,driver):
        self.driver = driver

    def setusername(self, username):
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).send_keys(password)

    def submit(self):
        self.driver.find_element(By.ID, self.LoginBtn_id).click()

    def logo(self):
        self.driver.find_element(By.XPATH,self.logo_xpath).click()

    def logout(self):
        self.driver.find_element(By.XPATH,self.Logout_xpath).click()
