from lib.util import timeout_handlers

class Loginpage():
    def __init__(self,driver):
        self.driver=driver

    def wait_for_login_page_to_load(self):
        element= self.driver.find_element_by_id("newContentWrapper")
        timeout_handlers.wait_for_element_visibility(self.driver,element)

    def get_username_textbox(self):
        try:
             return self.driver.find_element_by_name("UserName")
        except:
            return None
    def get_password_textbox(self):
        try:
            return  self.driver.find_element_by_name("Password")
        except:
            return None

    def get_login_button(self):
        try:
            return self.driver.find_element_by_id("submitButton")
        except:
            return None

