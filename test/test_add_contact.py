# -*- coding: utf-8 -*-
from model.class_for_test import Contact
import pytest
import random
import string
import re

def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="",
                                  company="", address="", home_phone="", cell_phone="", work_phone="", fax="",
                                  email="", email2="", email3="", address2="",
                                  secondary_phone="", notes="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 20),
            nickname=random_string("nickname", 20), title=random_string("title", 20),
                                company=random_string("company", 20), address=random_string("address", 30),
                                home_phone=random_string("home_phone", 10), cell_phone=random_string("cell_phone", 10),
                                work_phone=random_string("work_phone", 10), fax=random_string("fax", 10),
                                email=random_string("email", 20), email2=random_string("email2", 20), email3=random_string("email3", 20),
                                address2=random_string("address2", 30), secondary_phone=random_string("secondary_phone", 10), notes=random_string("notes", 40))
    for i in range(5)
    ]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_Add_Contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_Add_empty_Contact(app):
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(firstname="", middlename="", lastname="", nickname="", title="",
#                                   company="", address="", home="", mobile="", work="", fax="",
#                                   email="", email2="", email3="", address2="",
#                                   phone2="", notes="")
#     app.contact.create(contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
