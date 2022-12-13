import random
from model.class_for_test import Contact
from model.class_for_test import Group


def test_add_contact_to_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Test contact"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test", header="group test", footer="test group"))
    old_contacts = orm.get_contact_list()
    contact = random.choice(old_contacts)
    old_groups = orm.get_group_list()
    group = random.choice(old_groups)
    app.contact.add_contact_to_group(contact.id, group.id)
    contacts_in_group = orm.get_contacts_in_group(group)
    assert contact in contacts_in_group

# c965c306911b47baa8bbd954a41d55e1
