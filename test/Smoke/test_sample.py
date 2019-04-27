import unittest
import json
from lib.ui.Login_page import Loginpage
from lib.util import timeout_handlers,Create_Driver

class Testsample(unittest.TestCase):

    def setUp(self):
        self.driver=Create_Driver.get_browser_instance()
        self.login= Loginpage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_sample_script(self):
        test_data=json.load(open("./test/Smoke/Test_Data/Sample_Data.json"))
        self.login.wait_for_login_page_to_load()
        timeout_handlers.wait_for_title_of_webpage(self.driver,test_data['title'])
        actual_title =self.driver.title
        assert actual_title == test_data['title']
        print(actual_title)



