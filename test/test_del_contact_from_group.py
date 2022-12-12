import random
from fixture.orm import ORMFixture
from model.class_for_test import Contact
from model.class_for_test import Group

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_remove_contact_from_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Test contact"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test", header="group test", footer="test group"))
    group_list = db.get_group_list()
    group = random.choice(group_list)
    contacts_in_group_db_old = orm.get_contacts_in_group(Group(id=group.id))
    contact = random.choice(contacts_in_group_db_old)
    app.contact.del_contact_from_group(contact.id, group.id)
    contacts_in_group_db_new = orm.get_contacts_in_group(Group(id=group.id))
    contacts_not_in_group = orm.get_contacts_not_in_group(Group(id=group.id))
    assert len(contacts_in_group_db_old) - 1 == len(contacts_in_group_db_new)
    assert contact in contacts_not_in_group


# def test_del_contact_in_group(app, db):
#     if len(db.get_contact_list()) == 0:
#         app.contact.create(Contact(firstname="Test contact"))
#     if len(db.get_group_list()) == 0:
#         app.group.create(Group(name="test", header="group test", footer="test group"))
#     all_groups = db.get_group_list()
#     group = random.choice(all_groups)
#     contact = random.choice(app.contact.get_id_from_group_view_page(group.name))
#     app.contact.del_contact_from_group(contact.id)
#     contacts_in_group = orm.get_contacts_in_group(group)
#     assert contact not in contacts_in_group


    # groups = db.get_group_list()
    # contacts = db.get_contact_list()
    # if len(groups) == 0:
    #     app.group.create(Group(name="name", header="one", footer="two"))
    #     groups = db.get_group_list()
    # if len(contacts) == 0:
    #     app.contact.create(Contact(firstname="test1", lastname="test2", nickname="bla", title="Title",
    #                                company="Company", address="msk", home_phone="8990", cell_phone="3434",
    #                                work_phone="3434", fax="3443", email="yrt@mail.ru", secondary_phone="233333"))
    #     contacts = db.get_contact_list()
    #
    # random_group = random.choice(groups)
    # old_contacts_in_group = orm.get_contacts_in_group(random_group)
    #
    # if len(old_contacts_in_group) != 0:
    #     random_contact = random.choice(old_contacts_in_group)
    #     app.contact.del_contact_by_id_from_group(random_contact, random_group)
    # else:
    #     random_contact = random.choice(contacts)
    #     app.contact.add_contact_by_id_in_group(random_contact, random_group)
    #     old_contacts_in_group = orm.get_contacts_in_group(random_group)
    #     app.contact.del_contact_by_id_from_group(random_contact, random_group)
    #
    # new_contacts_in_group = orm.get_contacts_in_group(random_group)
    # old_contacts_in_group.remove(random_contact)
    # assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)