from selenium import webdriver


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        # self.wd.get('http://localhost/addressbook/group.php')
        self.wd.implicitly_wait(30)

    def Logout(self):
        wd = self.wd
        wd.find_element("link text", "Logout").click()

    def Return_home_page(self):
        wd = self.wd
        wd.find_element("link text", "home page").click()

    def Creat_new_contact(self, Contact):
        wd = self.wd
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
        # wd.find_element("name", "bday").click()
        # wd.find_element("name", "bday").select_by_visible_text("1")
        # wd.find_element("xpath", "//input[@value='1']").click()
        # wd.find_element("name", "bmonth").click()
        # Select(wd.find_element("name", "bmonth")).select_by_visible_text("January")
        # wd.find_element("xpath", "//input[@value='January']").click()
        # wd.find_element("name", "byear").click()
        # wd.find_element("name", "byear").clear()
        # wd.find_element("name", "byear").send_keys("1990")
        # wd.find_element("name", "aday").click()
        # Select(wd.find_element("name", "aday")).select_by_visible_text("4")
        # wd.find_element("xpath", "//div[@id='content']/form/select[3]/option[6]").click()
        # wd.find_element("name", "amonth").click()
        # Select(wd.find_element("name", "amonth")).select_by_visible_text("September")
        # wd.find_element("xpath", "//div[@id='content']/form/select[4]/option[10]").click()
        # wd.find_element("name", "ayear").click()
        # wd.find_element("name", "ayear").clear()
        # wd.find_element("name", "ayear").send_keys("1999")
        wd.find_element("name", "address2").click()
        wd.find_element("name", "address2").clear()
        wd.find_element("name", "address2").send_keys(Contact.address2)
        wd.find_element("name", "phone2").clear()
        wd.find_element("name", "phone2").send_keys(Contact.phone2)
        wd.find_element("name", "notes").clear()
        wd.find_element("name", "notes").send_keys(Contact.notes)
        # submit contact creation
        wd.find_element("xpath", "//input[@value='Enter']").click()
        self.Return_home_page()

    def Open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def Login(self, username="admin", password="secret"):
        wd = self.wd
        self.Open_home_page()
        wd.find_element("name", "user").click()
        wd.find_element("name", "user").clear()
        wd.find_element("name", "user").send_keys(username)
        wd.find_element("name", "pass").clear()
        wd.find_element("name", "pass").send_keys(password)
        wd.find_element("xpath", "//input[@value='Login']").click()

    def deastroy(self):
        self.wd.quit()
