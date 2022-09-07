class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element("add new").click()

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element("link text", "home").click()

    def create(self, Contact):
        wd = self.app.wd
        # init new contact
        wd.find_element("link text", "add new").click()
        # fill contact form
        wd.find_element("name", "firstname").click()
        wd.find_element("name", "firstname").clear()
        wd.find_element("name", "firstname").send_keys(Contact.firstname)
        wd.find_element("name", "middlename").clear()
        wd.find_element("name", "middlename").send_keys(Contact.middlename)
        wd.find_element("name", "lastname").clear()
        wd.find_element("name", "lastname").send_keys(Contact.lastname)
        wd.find_element("name", "nickname").clear()
        wd.find_element("name", "nickname").send_keys(Contact.nickname)
        # wd.find_element("xpath", "//input[@name='photo']").click()
        # wd.find_element("name", "photo").send_keys("C:\\fakepath\\973.jpg")
        wd.find_element("name", "title").click()
        wd.find_element("name", "title").clear()
        wd.find_element("name", "title").send_keys(Contact.title)
        wd.find_element("name", "company").clear()
        wd.find_element("name", "company").send_keys(Contact.company)
        wd.find_element("name", "address").clear()
        wd.find_element("name", "address").send_keys(Contact.address)
        wd.find_element("name", "home").clear()
        wd.find_element("name", "home").send_keys(Contact.home)
        wd.find_element("name", "mobile").clear()
        wd.find_element("name", "mobile").send_keys(Contact.mobile)
        wd.find_element("name", "work").clear()
        wd.find_element("name", "work").send_keys(Contact.work)
        wd.find_element("name", "fax").clear()
        wd.find_element("name", "fax").send_keys(Contact.fax)
        wd.find_element("name", "email").clear()
        wd.find_element("name", "email").send_keys(Contact.email)
        wd.find_element("name", "email2").clear()
        wd.find_element("name", "email2").send_keys(Contact.email2)
        wd.find_element("name", "email3").clear()
        wd.find_element("name", "email3").send_keys(Contact.email3)
        # wd.find_element("bday").click()
        # Select(wd.find_element("bday")).select_by_visible_text(contact.bday)
        # if contact.bmonth != '':
        #    wd.find_element("bmonth").click()
        #    Select(wd.find_element("bmonth")).select_by_visible_text(contact.bmonth)
        #wd.find_element("byear").click()
        #wd.find_element("byear").clear()
        #wd.find_element("byear").send_keys(contact.byear)
        #wd.find_element("aday").click()
        #Select(wd.find_element("aday")).select_by_visible_text(contact.aday)
        #if contact.amonth != '':
        #    wd.find_element("amonth").click()
        #    Select(wd.find_element("amonth")).select_by_visible_text(contact.amonth)
        #wd.find_element("ayear").click()
        #wd.find_element("ayear").clear()
        #wd.find_element("ayear").send_keys(contact.ayear)
        wd.find_element("name", "address2").click()
        wd.find_element("name", "address2").clear()
        wd.find_element("name", "address2").send_keys(Contact.address2)
        wd.find_element("name", "phone2").clear()
        wd.find_element("name", "phone2").send_keys(Contact.phone2)
        wd.find_element("name", "notes").clear()
        wd.find_element("name", "notes").send_keys(Contact.notes)
        # submit contact creation
        wd.find_element("xpath", "//input[@value='Enter']").click()
        self.return_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        # select first contact
        wd.find_element("name", "selected[]").click()
        # submit deletion
        wd.find_element("xpath", "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
       # self.return_home_page()

    def edit(self, Contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element("name", "selected[]").click()
        wd.find_element("xpath", "//img[@alt='Edit']").click()
        # fill contact form
        wd.find_element("name", "firstname").click()
        wd.find_element("name", "firstname").clear()
        wd.find_element("name", "firstname").send_keys(Contact.firstname)
        wd.find_element("name", "middlename").clear()
        wd.find_element("name", "middlename").send_keys(Contact.middlename)
        wd.find_element("name", "lastname").clear()
        wd.find_element("name", "lastname").send_keys(Contact.lastname)
        wd.find_element("name", "nickname").clear()
        wd.find_element("name", "nickname").send_keys(Contact.nickname)
        # wd.find_element("xpath", "//input[@name='photo']").click()
        # wd.find_element("name", "photo").send_keys("C:\\fakepath\\973.jpg")
        wd.find_element("name", "title").click()
        wd.find_element("name", "title").clear()
        wd.find_element("name", "title").send_keys(Contact.title)
        wd.find_element("name", "company").clear()
        wd.find_element("name", "company").send_keys(Contact.company)
        wd.find_element("name", "address").clear()
        wd.find_element("name", "address").send_keys(Contact.address)
        wd.find_element("name", "home").clear()
        wd.find_element("name", "home").send_keys(Contact.home)
        wd.find_element("name", "mobile").clear()
        wd.find_element("name", "mobile").send_keys(Contact.mobile)
        wd.find_element("name", "work").clear()
        wd.find_element("name", "work").send_keys(Contact.work)
        wd.find_element("name", "fax").clear()
        wd.find_element("name", "fax").send_keys(Contact.fax)
        wd.find_element("name", "email").clear()
        wd.find_element("name", "email").send_keys(Contact.email)
        wd.find_element("name", "email2").clear()
        wd.find_element("name", "email2").send_keys(Contact.email2)
        wd.find_element("name", "email3").clear()
        wd.find_element("name", "email3").send_keys(Contact.email3)
        wd.find_element("name", "address2").click()
        wd.find_element("name", "address2").clear()
        wd.find_element("name", "address2").send_keys(Contact.address2)
        wd.find_element("name", "phone2").clear()
        wd.find_element("name", "phone2").send_keys(Contact.phone2)
        wd.find_element("name", "notes").clear()
        wd.find_element("name", "notes").send_keys(Contact.notes)
        wd.find_element("name", "update").click()
        self.return_home_page()

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element("link text", "home page").click()