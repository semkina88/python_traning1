from selenium import webdriver


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        # self.wd.get('http://localhost/addressbook/group.php')
        self.wd.implicitly_wait(30)

    def logout(self):
        wd = self.wd
        wd.find_element("link text", "Logout").click()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element("link text", "group page").click()

    def submit_group_creation(self):
        wd = self.wd
        wd.find_element("xpath", "//input[@value='Enter information']").click()

    def create_group(self, group):
        wd = self.wd
        self.open_group_page()
        # init group creation
        wd.find_element("xpath", "//input[@value='New group']").click()
        # fill group form
        wd.find_element("name", "group_name").click()
        wd.find_element("name", "group_name").clear()
        wd.find_element("name", "group_name").send_keys(group.name)
        wd.find_element("name", "group_header").click()
        wd.find_element("name", "group_header").clear()
        wd.find_element("name", "group_header").send_keys(group.header)
        wd.find_element("name", "group_footer").click()
        wd.find_element("name", "group_footer").clear()
        wd.find_element("name", "group_footer").send_keys(group.footer)
        self.submit_group_creation()
        self.return_to_groups_page()

    def open_group_page(self):
        wd = self.wd
        wd.find_element("link text", "groups").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element("name", "user").click()
        wd.find_element("name", "user").clear()
        wd.find_element("name", "user").send_keys(username)
        wd.find_element("name", "pass").clear()
        wd.find_element("name", "pass").send_keys(password)
        wd.find_element("xpath", "//input[@value='Login']").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def deastroy(self):
        self.wd.quit()

