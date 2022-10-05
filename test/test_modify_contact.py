from model.class_for_test import Contact
from random import randrange

def test_modify_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="bla"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="New contact")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(new_contacts, key=lambda contact: contact.id_or_max(), reverse=False)


    # old_contacts[0] = contact
    # assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_modify_first_contact_company(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="bla"))
#     app.contact.modify_first_contact(Contact(company="Name"))
