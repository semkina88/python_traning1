class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element("link text", "group page").click()

    def submit_group_creation(self):
        wd = self.app.wd
        wd.find_element("xpath", "//input[@value='Enter information']").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element("xpath", "//input[@value='New group']").click()
        # fill group form
        self.fill_group_form(group)
        self.submit_group_creation()
        self.return_to_groups_page()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # open modification form
        wd.find_element("name", "edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        wd.find_element("name", "update").click()
        self.return_to_groups_page()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element("name", field_name).click()
            wd.find_element("name", field_name).clear()
            wd.find_element("name", field_name).send_keys(text)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # submit deletion
        wd.find_element("xpath", "//input[@value='Delete group(s)']").click()
        self.return_to_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element("name", "selected[]").click()

    def edit(self, group):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        wd.find_element("xpath", "//input[@value='Edit group']").click()
        self.fill_group_form(group)
        # submit edit
        wd.find_element("xpath", "//input[@value='Update']").click()
        self.return_to_groups_page()


    def open_group_page(self):
        wd = self.app.wd
        wd.find_element("link text", "groups").click()


