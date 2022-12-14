import random
from model.class_for_test import Contact
from model.class_for_test import Group


def test_del_contact_from_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Test contact"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test", header="group test", footer="test group"))
    group_list = orm.get_group_list()
    group = random.choice(group_list)
    if len(orm.get_contacts_in_group(Group(id=group.id))) == 0:
        contact = random.choice(orm.get_contact_list())
        app.contact.add_contact_to_group(contact.id, group.id)
    contacts_in_group_db_old = orm.get_contacts_in_group(Group(id=group.id))
    contact = random.choice(contacts_in_group_db_old)
    app.contact.del_contact_from_group(contact.id, group.id)
    contacts_in_group_db_new = orm.get_contacts_in_group(Group(id=group.id))
    assert contact not in contacts_in_group_db_new