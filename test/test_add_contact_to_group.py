import random

from fixture.orm import ORMFixture
from model.class_for_test import Contact
from model.class_for_test import Group

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Test contact"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test", header="group test", footer="test group"))
    old_groups = db.get_group_list()
    old_contacts = db.get_contact_list()
    group = random.choice(old_groups)
    contact = random.choice(old_contacts)
    app.contact.add_contact_to_group(contact.id, group.id)

    # contacts_in_group = orm.get_contacts_in_group(group)
    # assert contact in contacts_in_group
