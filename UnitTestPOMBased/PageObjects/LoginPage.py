class LoginPage():
    #Locator of all the elements
    user_id_txt_id = "Email"
    user_password_txt_id = "Password"
    login_btn_xpath = "//input[@type='submit']"
    logout_link_linktext = "welcome"
    
    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,userName):
        self.driver.find_element_by_id(self.user_id_txt_id).clear()
        self.driver.find_element_by_id(self.user_id_txt_id).send_keys(userName)


    def setPassword(self,Password):
        self.driver.find_element_by_id(self.user_password_txt_id).clear()
        self.driver.find_element_by_id(self.user_password_txt_id).send_keys(Password)

    
    def clickLogin(self):
        self.driver.find_element_by_xpath(self.login_btn_xpath).click()

    

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.logout_link_linktext).click()