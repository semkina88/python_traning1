from model.class_for_test import Group
from timeit import timeit

def test_group_list(app, db):
    print(timeit(lambda: app.group.get_group_list(), number=1))
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    print(timeit(lambda: map(clean, db.get_group_list()), number=1000))
    assert False #sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


# def test_contact_list(app, db):
#     ui_list = app.contact.get_contact_list()
#     def clean(contact):
#         return Contact(id=contact.id, name=contact.name.strip(), lastname=contact.lastname.strip())
#     db_list = map(clean, db.get_contact_list())
#     assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)