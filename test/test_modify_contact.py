from random import randrange

from model.class_for_test import Contact


def test_modify_contact_firstname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="bla"))
    old_contacts = db.get_contact_list()
    contact = Contact(firstname="swyug")
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
#     contact.firstname == new_contacts[index].firstname
    old_contacts[index] = contact
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


