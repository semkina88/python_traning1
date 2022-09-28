from model.class_for_test import Contact


def test_modify_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="bla"))
    app.contact.modify_first_contact(Contact(firstname="New contact"))

def test_modify_first_contact_company(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="bla"))
    app.contact.modify_first_contact(Contact(company="Name"))
