from model.class_for_test import Contact
from selenium.webdriver.common.by import By

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element("add new").click()

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/")):
            wd.find_element("link text", "home").click()

    def create(self, contact):
        wd = self.app.wd
        # init new contact
        wd.find_element("link text", "add new").click()
        self.fill_contact_form(contact)
        self.submit_contact_creation()
        self.contact_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element("name", field_name).click()
            wd.find_element("name", field_name).clear()
            wd.find_element("name", field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def submit_contact_creation(self):
        wd = self.app.wd
        wd.find_element("xpath", "//input[@value='Enter']").click()
        self.return_home_page()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element("xpath", "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.open_home_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements("name", "selected[]")[index].click()

    # def delete_first_contact(self):
    #     wd = self.app.wd
    #     self.open_home_page()
    #     self.select_first_contact(wd)
    #     submit deletion
        # wd.find_element("xpath", "//input[@value='Delete']").click()
        # wd.switch_to.alert.accept()
        # self.open_home_page()
        # self.contact_cache = None

    def select_first_contact(self, wd):
        wd = self.app.wd
        wd.find_element("name", "selected[]").click()


    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element("xpath", "//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element("name", "update").click()
        self.return_home_page()
        self.contact_cache = None

    # def modify_first_contact(self, new_contact_data):
    #     wd = self.app.wd
    #     self.open_home_page()
    #     self.select_first_contact(wd)
    #     wd.find_element("xpath", "//img[@alt='Edit']").click()
    #     self.fill_contact_form(new_contact_data)
    #     wd.find_element("name", "update").click()
    #     self.return_home_page()
    #     self.contact_cache = None

    def edit(self, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element("xpath", "//img[@alt='Edit']").click()
        self.fill_contact_form(contact)
        wd.find_element("name", "update").click()
        self.return_home_page()
        self.contact_cache = None

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element("link text", "home page").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements("name", "selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements(By.CSS_SELECTOR, "tr[name=entry]"):
                cells = element.find_elements(By.TAG_NAME, "td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = element.find_element("name", "selected[]").get_attribute("id")
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return list(self.contact_cache)