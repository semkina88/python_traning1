from fixture.orm import ORMFixture
from model.class_for_test import Group

tempdb = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = tempdb.get_contacts_in_group(Group(id=2))
    # l = db.get_contact_list()
    for item in l:
        print(item)
    print(len(l))
finally:
    pass  # db.destroy()
