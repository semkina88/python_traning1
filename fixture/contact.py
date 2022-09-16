class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element("add new").click()

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element("link text", "home").click()

    def create(self, contact):
        wd = self.app.wd
        # init new contact
        wd.find_element("link text", "add new").click()
        self.fill_contact_form(contact)
        self.submit_contact_creation()
        # self.return_home_page()
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
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact(wd)
        # submit deletion
        wd.find_element("xpath", "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()

    def select_first_contact(self, wd):
        wd = self.app.wd
        wd.find_element("name", "selected[]").click()


    # self.return_home_page()
    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact(wd)
        wd.find_element("xpath", "//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element("name", "update").click()
        self.return_home_page()

    def edit(self, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element("xpath", "//img[@alt='Edit']").click()
        self.fill_contact_form(contact)
        wd.find_element("name", "update").click()
        self.return_home_page()

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element("link text", "home page").click()