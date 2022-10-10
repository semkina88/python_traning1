# -*- coding: utf-8 -*-

from model.class_for_test import Contact

def test_Add_Contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="ytf", middlename="rsth", lastname="fxgh", nickname="gfx",
                                  title="gfxh", company="vbn", address="xfr", home="12", mobile="3214", work="325",
                                  fax="45",
                                  email="456", email2="56", email3="78", address2="8876", phone2="ch6", notes="hkt6")
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
