from model.class_for_test import Contact


def test_modify_first_contact_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="New contact"))

def test_modify_first_contact_company(app):
    app.contact.modify_first_contact(Contact(company="Name"))
