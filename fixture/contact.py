from model.class_for_test import Contact
from selenium.webdriver.common.by import By
from random import randrange
import re

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
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.cell_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.secondary_phone)
        self.change_field_value("notes", contact.notes)

    def submit_contact_creation(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
        self.return_home_page()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element(By.CSS_SELECTOR, 'input[type="button"]').click()
        wd.switch_to.alert.accept()
        self.open_home_page()
        self.contact_cache = None

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element("xpath", "//img[@alt='Details']").click()
        # row = wd.find_elements(By.CSS_SELECTOR, "tr[name = 'entry']")[index]
        # cell = row.find_elements(By.TAG_NAME, "td")[6]
        # cell.find_elements(By.TAG_NAME, "a").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements("name","selected[]")[index].click()


    def select_first_contact(self, wd):
        wd = self.app.wd
        wd.find_element("name", "selected[]").click()


    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.find_modify_button_by_index(index)
        # self.select_contact_by_index(index)
        # wd.find_element("xpath", "//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element("name", "update").click()
        self.return_home_page()
        self.contact_cache = None

    def find_modify_button_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.CSS_SELECTOR, 'img[title="Edit"]')[index].click()

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
            for row in wd.find_elements(By.CSS_SELECTOR, "tr[name = 'entry']"):
                cells = row.find_elements(By.TAG_NAME, "td")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                id = cells[0].find_element("name", "selected[]").get_attribute("id")
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, address=address,
                                                  id=id, all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.find_modify_button_by_index(index)
        firstname = wd.find_element("name", "firstname").get_attribute("value")
        lastname = wd.find_element("name", "lastname").get_attribute("value")
        id = wd.find_element("name", "id").get_attribute("value")
        home_phone = wd.find_element("name", "home").get_attribute("value")
        cell_phone = wd.find_element("name", "mobile").get_attribute("value")
        work_phone = wd.find_element("name", "work").get_attribute("value")
        secondary_phone = wd.find_element("name", "phone2").get_attribute("value")
        address = wd.find_element("name", "address").get_attribute("value")
        email = wd.find_element("name", "email").get_attribute("value")
        email2 = wd.find_element("name", "email2").get_attribute("value")
        email3 = wd.find_element("name", "email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       home_phone=home_phone, cell_phone=cell_phone,
                       work_phone=work_phone, secondary_phone=secondary_phone, address=address,
                       email=email, email2=email2, email3=email3)


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element("id", "content").text
        home_phone = re.search("H: (.*)", text).group(1)
        cell_phone = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        secondary_phone = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, cell_phone=cell_phone,
                       work_phone=work_phone, secondary_phone=secondary_phone)
