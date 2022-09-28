from model.class_for_test import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="bla"))
    app.contact.delete_first_contact()
