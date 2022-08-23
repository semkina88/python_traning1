# -*- coding: utf-8 -*-
from selenium import webdriver


from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class Select:
    pass


class AddNewContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        # self.wd.get('http://localhost/addressbook/')
        self.wd.implicitly_wait(30)

    def test_untitled_test_case(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        # Login
        wd.find_element("name", "user").click()
        wd.find_element("name", "user").clear()
        wd.find_element("name", "user").send_keys("admin")
        wd.find_element("name", "pass").clear()
        wd.find_element("name", "pass").send_keys("secret")
        wd.find_element("xpath", "//input[@value='Login']").click()
        # create new contact
        wd.find_element("link text", "add new").click()
        wd.find_element("name", "firstname").click()
        wd.find_element("name", "firstname").clear()
        wd.find_element("name", "firstname").send_keys("ewq")
        wd.find_element("name", "middlename").clear()
        wd.find_element("name", "middlename").send_keys("kjh")
        wd.find_element("name", "lastname").clear()
        wd.find_element("name", "lastname").send_keys("oiu")
        wd.find_element("name", "nickname").clear()
        wd.find_element("name", "nickname").send_keys("oiu")
        wd.find_element("name", "title").click()
        wd.find_element("name", "title").clear()
        wd.find_element("name", "title").send_keys("iu")
        wd.find_element("name", "company").clear()
        wd.find_element("name", "company").send_keys("iuy")
        wd.find_element("name", "address").clear()
        wd.find_element("name", "address").send_keys("yugu")
        wd.find_element("name", "home").clear()
        wd.find_element("name", "home").send_keys("uyg")
        wd.find_element("name", "mobile").clear()
        wd.find_element("name", "mobile").send_keys("uyf")
        wd.find_element("name", "work").clear()
        wd.find_element("name", "work").send_keys("uyf")
        wd.find_element("name", "fax").clear()
        wd.find_element("name", "fax").send_keys("gc")
        wd.find_element("name", "email").clear()
        wd.find_element("name", "email").send_keys("hjgck@yg.e")
        wd.find_element("name", "email2").clear()
        wd.find_element("name", "email2").send_keys("sdf@;l")
        wd.find_element("name", "email2").click()
        wd.find_element("name", "email2").clear()
        wd.find_element("name", "email2").send_keys("sdf@er.ew")
        wd.find_element("name", "email3").clear()
        wd.find_element("name", "email3").send_keys("kjwer@ert.rt")
        wd.find_element("name", "address2").click()
        wd.find_element("name", "address2").clear()
        wd.find_element("name", "address2").send_keys("hfdtrds")
        wd.find_element("name", "phone2").clear()
        wd.find_element("name", "phone2").send_keys("trdtrd")
        wd.find_element("name", "notes").clear()
        wd.find_element("name", "notes").send_keys("hjfjfj")
        wd.find_element("xpath", "//input[@value='Enter']").click()
        # return to Contact page
        wd.find_element("link_text", "home page").click()
        # Logout
        wd.find_element("link_text", "Logout").click()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True


    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
