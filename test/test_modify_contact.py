from model.class_for_test import Contact


def test_modify_first_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="New contact"))
    app.session.logout()

def test_modify_first_contact_company(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(company="Name"))
    app.session.logout()