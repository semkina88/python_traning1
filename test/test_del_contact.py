from model.class_for_test import Contact
from random import randrange
import time

def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="new"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    time.sleep(3)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert sorted(old_contacts) == sorted(new_contacts)

  # new_contacts = app.contact.get_contact_list()