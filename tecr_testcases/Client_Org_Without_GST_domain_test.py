import time

from tecr_pageobjects.ClientOrg import ClientOrgPage


class Test_Login_002:
    Url = "http://113.193.29.163/ABSLI/Account/Login"
    username = "gradatim"
    password = "Password1$"
    client_name = "automation3"
    occupation = "business"
    sal="Mr."
    firsrtname ='Ganesan'
    middleName ='Ganesan'
    lastName ='Ganesan'
    mobileno = "9840974246"
    RiskCategory = "Medium"
    TURNOVER = "1000"
    TYPOFCLIENT ="SEZ Customer"
    gsttype = "NO GST PAYABLE"
    PanNo = "AAECK4949B"
    GstnNo = "27AAECK4949B1ZK"
    Logbased = "Login Details"
    accessbased = "Role"
    emaildidinfo = "ganesan@gmail.com"
    journeytype = "Medical"
    sourcetype = "API"
    domainname = "gg@domain"
    servicebaranchdetails = "Mumbai"
    marketcode = "123451"
    grade = 'Band5'
    department = "HR"
    designation = "Manager"
    role="tester"
    address1 = "test"
    address2 = "test"
    address3 = "test"
    address4 = "test"
    state = "Maharashtra"
    district = "Pune"
    taluk = "Purandhar"
    landlineno = "9840974345"
    addresstype = "Postal Address"

    def test_CLORG(self,setup):
        self.driver = setup
        self.driver.get(self.Url)
        self.CLORGPA = ClientOrgPage(self.driver)
        self.CLORGPA.setUserName(self.username)
        self.CLORGPA.setpassword(self.password)
        self.CLORGPA.submit()
        self.CLORGPA.clickCm()
        self.CLORGPA.clickclo()
        time.sleep(2)
        self.CLORGPA.setclientname(self.client_name)
        self.CLORGPA.setoccupation(self.occupation)
        time.sleep(2)
        self.CLORGPA.setsalutation(self.sal)
        time.sleep(2)
        self.CLORGPA.setfirstname(self.firsrtname)
        self.CLORGPA.setmiddlename(self.middleName)
        self.CLORGPA.setlastname(self.lastName)
        time.sleep(1)
        self.CLORGPA.clicksms()
        self.CLORGPA.clickemail()
        self.CLORGPA.setmobileno(self.mobileno)
        self.CLORGPA.setriskcategory(self.RiskCategory)
        time.sleep(1)
        self.CLORGPA.setturnover(self.TURNOVER)
        time.sleep(1)
        self.CLORGPA.settypeofclient(self.TYPOFCLIENT)
        time.sleep(2)
        #self.CLORGPA.setgsttype(self.gsttype)
        #time.sleep(1)
        self.CLORGPA.setpanno(self.PanNo)
        time.sleep(1)
        #self.CLORGPA.setgstnno(self.GstnNo)
        #time.sleep(1)
        self.CLORGPA.setloginbased(self.Logbased)
        time.sleep(2)
        self.CLORGPA.setaccessbased(self.accessbased)
        time.sleep(2)
        self.CLORGPA.setemailid(self.emaildidinfo)
        time.sleep(2)
        self.CLORGPA.setjourneytype(self.journeytype)
        time.sleep(2)
        self.CLORGPA.setsourcetype(self.sourcetype)
        time.sleep(2)
        #self.CLORGPA.clickdyemailid()
        #time.sleep(1)
        #self.CLORGPA.setdomainname(self.domainname)
        #time.sleep(1)
        self.CLORGPA.setserbradetails(self.servicebaranchdetails)
        time.sleep(2)
        self.CLORGPA.setmarketcode(self.marketcode)
        time.sleep(2)
        self.CLORGPA.setgrade(self.grade)
        time.sleep(2)
        self.CLORGPA.clickgradesavebtn()
        time.sleep(2)
        self.CLORGPA.clickokbtn(self.driver)
        time.sleep(2)
        self.CLORGPA.setdept(self.department)
        time.sleep(1)
        self.CLORGPA.setdesi(self.designation)
        self.CLORGPA.clicksavedepdesbtn()
        time.sleep(2)
        self.CLORGPA.clickokbtn(self.driver)
        self.CLORGPA.setrole(self.role)
        self.CLORGPA.clickrolsavebtn()
        self.CLORGPA.clickokbtn(self.driver)
        self.CLORGPA.setaddress1(self.address1)
        self.CLORGPA.setaddress2(self.address2)
        self.CLORGPA.setaddress3(self.address3)
        self.CLORGPA.setaddress4(self.address4)
        time.sleep(2.0)
        self.CLORGPA.setstate(self.state)
        time.sleep(2.0)
        self.CLORGPA.setdistrict(self.district)
        time.sleep(2.0)
        self.CLORGPA.settaluk(self.taluk)
        time.sleep(2.0)
        self.CLORGPA.setlandlineno(self.landlineno)
        time.sleep(1.0)
        self.CLORGPA.setaddresstype(self.addresstype)
        time.sleep(1.0)
        self.CLORGPA.setoccupation(self.occupation)
        time.sleep(1)
        #self.CLORGPA.setgstnno(self.GstnNo)
        #time.sleep(1)
        self.CLORGPA.clicksaveaddbtn()
        time.sleep(1.0)
        self.CLORGPA.clickokbtn(self.driver)
        time.sleep(1.0)
        self.CLORGPA.clickaddclibtn()
        time.sleep(5.0)
        self.CLORGPA.clickokbtn(self.driver)

