import random
from model.class_for_test import Contact
from model.class_for_test import Group


def test_add_contact_to_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Test contact"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test", header="group test", footer="test group"))
    old_groups = orm.get_group_list()
    group = random.choice(old_groups)
    contacts_not_in_group = orm.get_contacts_not_in_group(Group(id=group.id))
    if len(contacts_not_in_group) == 0:
        app.contact.create(Contact(firstname="Contact1"))
    contacts_not_in_group = orm.get_contacts_not_in_group(Group(id=group.id))
    contact = random.choice(contacts_not_in_group)
    app.contact.add_contact_to_group(contact.id, group.id)
    contacts_in_group_db_new = orm.get_contacts_in_group(group)
    assert contact in contacts_in_group_db_new


