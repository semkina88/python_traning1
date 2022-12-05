import random
from random import randrange

from model.class_for_test import Contact


def test_modify_contact_firstname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="bla"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="test")
    selection = random.choice(old_contacts)
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_id(selection.id, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    old_contacts[index].id = new_contacts[index].id
    old_contacts[index].firstname = new_contacts[index].firstname
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
