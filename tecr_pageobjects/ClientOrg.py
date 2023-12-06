import time
import selenium
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common import alert
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement
from selenium.webdriver.support.wait import WebDriverWait
from selenium import actions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ClientOrgPage:
    textbox_username_id = "ContentPlaceHolder1_txtUserName"
    textbox_password_id = "ctl00$ContentPlaceHolder1$txtPassword"
    LoginBtn_xpath = "//body[1]/form[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[7]/input[1]"
    # logo_xpath = "//body/form[@id='ctl00']/div[@id='ContentPlaceHolder1_upLoginPage']/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]"
    logout_xpath = "//body[1]/form[1]/div[4]/nav[1]/ul[1]/li[17]/a[1]"
    client_master_linktext = "Client Master"
    client_org_xpath = "//a[contains(text(),'Client Organization')]"
    client_name_id = "ContentPlaceHolder1_ucGroupParty_txtOrgName"
    occupation_id = "ContentPlaceHolder1_ucGroupParty_txtCoreBusiness"
    salutation_id = "select2-ContentPlaceHolder1_ucGroupParty_ddlSalutation-container"
    first_name_id = "ContentPlaceHolder1_ucGroupParty_txtContactPersonFirstName"
    middle_name_id = "ContentPlaceHolder1_ucGroupParty_txtContactPersonMiddleName"
    last_name_id = "ContentPlaceHolder1_ucGroupParty_txtContactPersonLastName"
    sms_id = "ContentPlaceHolder1_ucGroupParty_chkIsSMS"
    email_id = "ContentPlaceHolder1_ucGroupParty_chkEmail"
    mobile_id = "ContentPlaceHolder1_ucGroupParty_txtContactNo"
    risk_details_id = "select2-ContentPlaceHolder1_ucGroupParty_ddlRiskCategory-container"
    turnover_id = "ContentPlaceHolder1_ucGroupParty_txtTurnOver"
    type_of_client_id = "select2-ContentPlaceHolder1_ucGroupParty_ddlTypeOfClient-container"
    gst_type_id = "select2-ContentPlaceHolder1_ucGroupParty_ddlGSTType-container"
    pan_number_id = "ContentPlaceHolder1_ucGroupParty_txtPANNo"
    gst_number_id = "ContentPlaceHolder1_ucGroupParty_txtGSTNo"
    login_based_id = "select2-ContentPlaceHolder1_ucGroupParty_ddlLoginBasedOn-container"
    access_based_xpath = "//span[@id='select2-ContentPlaceHolder1_ucGroupParty_ddlAccessBasedOn-container']"
    emailid_id = "ContentPlaceHolder1_ucGroupParty_txtEmail"
    journey_type_id = "select2-ContentPlaceHolder1_ucGroupParty_ddlJourneyType-container"
    source_type_xpath = "//span[@id='select2-ContentPlaceHolder1_ucGroupParty_ddlSourceType-container']"
    dyanamic_EmailID_id= "ContentPlaceHolder1_ucGroupParty_chkIsOTPDisabledClaims"
    domain_name_id = "ContentPlaceHolder1_ucGroupParty_txtDomainName"
    service_branch_id = "select2-ContentPlaceHolder1_ddlBranch-container"
    market_code_xpath = "//input[@id='ContentPlaceHolder1_txtAgentCode']"
    grade_xpath = "//textarea[@id='ContentPlaceHolder1_txtGrade']"
    save_grade_xpath = "//input[@id='ContentPlaceHolder1_btnGradeSave']"
    popup_xpath = "//body[1]/div[7]"
    confirm_button_xpath = "//button[contains(text(),'Ok')]"
    department_id = "ContentPlaceHolder1_txtDepartment"
    designation_id = "ContentPlaceHolder1_txtDesignation"
    save_button_depdes_xpath = "//input[@id='ContentPlaceHolder1_btnSaveDepartment']"
    role_id = "ContentPlaceHolder1_txtRole"
    save_button_role_id = "ContentPlaceHolder1_btnSaveRole"
    address1_xpath = "//input[@id='ContentPlaceHolder1_ucPartyAddress_txtAddress1']"
    address2_xpath = "//input[@id='ContentPlaceHolder1_ucPartyAddress_txtAddress2']"
    address3_xpath = "//input[@id='ContentPlaceHolder1_ucPartyAddress_txtAddress3']"
    address4_xpath = "//input[@id='ContentPlaceHolder1_ucPartyAddress_txtAddress4']"
    state_id = "select2-ContentPlaceHolder1_ucPartyAddress_ddlState-container"
    district_id = "select2-ContentPlaceHolder1_ucPartyAddress_ddlDistrict-container"
    taluk_id = "select2-ContentPlaceHolder1_ucPartyAddress_ddlTaluk-container"
    landline_no_xpath = "//input[@id='ContentPlaceHolder1_ucPartyAddress_txtPhoneNo']"
    address_type_xpath = "//span[@id='select2-ContentPlaceHolder1_ucPartyAddress_ddlAddressType-container']"
    save_button_address_id = "ContentPlaceHolder1_ucPartyAddress_btnAddress"
    add_client_id = "ContentPlaceHolder1_btnAddParty"
    logoff_link_xpath = "//body/form[@id='frm']/div[@id='wrapper']/nav[@id='sidebar_wrapper']/ul[1]/li[17]/a[1]"

    def __init__(self, driver):
        self.element = None
        self.alert = None
        self.actions = None
        self.driver = driver


    def setUserName(self, username):
        self.driver.find_element(By.NAME, self.textbox_username_id).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element(By.NAME, self.textbox_password_id).send_keys(password)

    def submit(self):
        self.driver.find_element(By.XPATH, self.LoginBtn_xpath).click()

    def clickCm(self):
        self.driver.find_element(By.LINK_TEXT, self.client_master_linktext).click()

    def clickclo(self):
        self.driver.find_element(By.XPATH, self.client_org_xpath).click()

    def setclientname(self, client_name):
        self.driver.find_element(By.ID, self.client_name_id).send_keys(client_name)

    def setoccupation(self, occupation):
        self.driver.find_element(By.ID, self.occupation_id).send_keys(occupation)

    def setsalutation(self, sal):
        self.driver.find_element(By.ID, self.salutation_id).click()
        self.actions = ActionChains(self.driver)
        self.actions.move_to()
        self.actions.send_keys(sal)
        self.actions.move_to()
        self.actions.send_keys(Keys.ENTER).perform()

    def setfirstname(self, firstName):
        self.driver.find_element(By.ID, self.first_name_id).send_keys(firstName)

    def setmiddlename(self, middleName):
        self.driver.find_element(By.ID, self.middle_name_id).send_keys(middleName)

    def setlastname(self, lastName):
        self.driver.find_element(By.ID, self.last_name_id).send_keys(lastName)

    def clicksms(self):
        self.driver.find_element(By.ID, self.sms_id).click()

    def clickemail(self):
        self.driver.find_element(By.ID, self.email_id).click()

    def setmobileno(self, mobileno):
        self.driver.find_element(By.ID, self.mobile_id).send_keys(mobileno)

    def setriskcategory(self, RiskCategory):
        self.driver.find_element(By.ID, self.risk_details_id).click()
        self.actions = ActionChains(self.driver)
        self.actions.move_to()
        self.actions.send_keys(RiskCategory)
        self.actions.move_to()
        self.actions.send_keys(Keys.ENTER).perform()
        return self

    def setturnover(self, TURNOVER):
        self.driver.find_element(By.ID, self.turnover_id).send_keys(TURNOVER)

    def settypeofclient(self, TYPOFCLIENT):
        self.driver.find_element(By.ID, self.type_of_client_id).click()
        self.actions = ActionChains(self.driver)
        self.actions.move_to()
        self.actions.send_keys(TYPOFCLIENT)
        self.actions.move_to()
        self.actions.send_keys(Keys.ENTER).perform()
        return self

    def setgsttype(self, gsttype):
        self.driver.find_element(By.ID, self.gst_type_id).click()
        self.actions = ActionChains(self.driver)
        self.actions.move_to()
        self.actions.send_keys(gsttype)
        self.actions.move_to()
        self.actions.send_keys(Keys.ENTER).perform()

    def setpanno(self, PanNo):
        self.driver.find_element(By.ID, self.pan_number_id).send_keys(PanNo)

    def setgstnno(self, GstnNo):
        self.driver.find_element(By.ID, self.gst_number_id).send_keys(GstnNo)

    def setloginbased(self, Logbased):
        self.driver.find_element(By.ID, self.login_based_id).click()
        self.actions = ActionChains(self.driver)
        self.actions.move_to()
        self.actions.send_keys(Logbased)
        self.actions.move_to()
        self.actions.send_keys(Keys.ENTER).perform()

    def setaccessbased(self, accessbased):
        self.driver.find_element(By.XPATH, self.access_based_xpath).click()
        self.actions = ActionChains(self.driver)
        self.actions.move_to()
        self.actions.send_keys(accessbased)
        self.actions.move_to()
        self.actions.send_keys(Keys.ENTER).perform()

    def setemailid(self, emaildidinfo):
        self.driver.find_element(By.ID, self.emailid_id).send_keys(emaildidinfo)

    def setjourneytype(self, journeytype):
        self.driver.find_element(By.ID, self.journey_type_id).click()
        self.actions = ActionChains(self.driver)
        self.actions.move_to()
        self.actions.send_keys(journeytype)
        self.actions.move_to()
        self.actions.send_keys(Keys.ENTER).perform()

    def setsourcetype(self, sourcetype):
        self.driver.find_element(By.XPATH, self.source_type_xpath).click()
        self.actions = ActionChains(self.driver)
        self.actions.move_to()
        self.actions.send_keys(sourcetype)
        self.actions.move_to()
        self.actions.send_keys(Keys.ENTER).perform()


    def clickdyemailid(self):
        self.driver.find_element(By.ID,self.dyanamic_EmailID_id).click()

    def setdomainname(self,domainname):
        self.driver.find_element(By.ID,self.domain_name_id).send_keys(domainname)

    def setserbradetails(self, servicebaranchdetails):
        self.driver.find_element(By.ID, self.service_branch_id).click()
        self.actions = ActionChains(self.driver)
        self.actions.move_to()
        self.actions.send_keys(servicebaranchdetails)
        self.actions.move_to()
        self.actions.send_keys(Keys.ENTER).perform()

    def setmarketcode(self, marketcode):
        self.driver.find_element(By.XPATH, self.market_code_xpath).click()
        self.actions = ActionChains(self.driver)
        self.actions.move_to()
        self.actions.send_keys(marketcode)
        self.actions.move_to()
        self.actions.send_keys(Keys.ENTER).perform()

    def setgrade(self, grade):
        self.driver.find_element(By.XPATH, self.grade_xpath).send_keys(grade)

    def clickgradesavebtn(self):
        self.driver.find_element(By.XPATH, self.save_grade_xpath).click()

    def clickpopup(self):
        self.driver.find_element(By.XPATH, self.popup_xpath).click()

    def clickokbtn(self, driver):
        self.element = driver.find_element(By.XPATH, self.confirm_button_xpath)
        driver.execute_script("arguments[0].click();", self.element)

    def setdept(self, department):
        self.driver.find_element(By.ID, self.department_id).send_keys(department)

    def setdesi(self, designation):
        self.driver.find_element(By.ID, self.designation_id).send_keys(designation)

    def clicksavedepdesbtn(self):
        self.driver.find_element(By.XPATH, self.save_button_depdes_xpath).click()

    def setrole(self, role):
        self.driver.find_element(By.ID, self.role_id).send_keys(role)

    def clickrolsavebtn(self):
        self.driver.find_element(By.ID, self.save_button_role_id).click()

    def setaddress1(self, address1):
        self.driver.find_element(By.XPATH, self.address1_xpath).send_keys(address1)

    def setaddress2(self, address2):
        self.driver.find_element(By.XPATH, self.address2_xpath).send_keys(address2)

    def setaddress3(self, address3):
        self.driver.find_element(By.XPATH, self.address3_xpath).send_keys(address3)

    def setaddress4(self, address4):
        self.driver.find_element(By.XPATH, self.address4_xpath).send_keys(address4)

    def setstate(self, state):
        self.driver.find_element(By.ID, self.state_id).click()
        self.actions = ActionChains(self.driver)
        self.actions.move_to()
        self.actions.send_keys(state)
        self.actions.move_to()
        self.actions.send_keys(Keys.ENTER).perform()

    def setdistrict(self, district):
        self.driver.find_element(By.ID, self.district_id).click()
        self.actions = ActionChains(self.driver)
        self.actions.move_to()
        self.actions.send_keys(district)
        self.actions.move_to()
        self.actions.send_keys(Keys.ENTER).perform()

    def settaluk(self, taluk):
        self.driver.find_element(By.ID, self.taluk_id).click()
        self.actions = ActionChains(self.driver)
        self.actions.move_to()
        self.actions.send_keys(taluk)
        self.actions.move_to()
        self.actions.send_keys(Keys.ENTER).perform()

    def setlandlineno(self, landlineno):
        self.driver.find_element(By.XPATH, self.landline_no_xpath).send_keys(landlineno)

    def setaddresstype(self, addresstype):
        self.driver.find_element(By.XPATH, self.address_type_xpath).click()
        self.actions = ActionChains(self.driver)
        self.actions.move_to()
        self.actions.send_keys(addresstype)
        self.actions.move_to()
        self.actions.send_keys(Keys.ENTER).perform()

    def clicksaveaddbtn(self):
        self.driver.find_element(By.ID, self.save_button_address_id).click()

    def clickaddclibtn(self):
        self.driver.find_element(By.ID, self.add_client_id).click()
    def logout(self):
        self.driver.find_element(By.XPATH, self.logout_xpath).click()

    def WebDriverWait(self, driver, param):
        pass







