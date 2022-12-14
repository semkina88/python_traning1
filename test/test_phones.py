import re

from model.class_for_test import Contact


def test_field_on_home_page(app, db):
    contact_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    assert len(contact_from_db) == len(contact_from_home_page)
    for index in range(len(contact_from_db)):
        assert contact_from_home_page[index].firstname == contact_from_db[index].firstname
        assert contact_from_home_page[index].lastname == contact_from_db[index].lastname
        assert contact_from_home_page[index].address == contact_from_db[index].address
        assert contact_from_home_page[index].all_phones_from_home_page == merge_phones_like_on_home_page(
            contact_from_db[index])
        assert contact_from_home_page[index].all_emails_from_home_page == merge_emails_like_on_home_page(
            contact_from_db[index])


def clear(s):
    return re.sub("[ ()-]", "", s)


def clear_emails(s):
    return re.sub(" + ", " ", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.cell_phone, contact.work_phone,
                                        contact.secondary_phone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != '',
                            map(lambda x: clear_emails(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))

# тесты для сравнения одного контакта
#  contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
# contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
# def test_phones_on_home_page(app):
#     contact_from_home_page = app.contact.get_contact_list()[0]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_home_page.firstname == contact_from_edit_page.firstname
#     assert contact_from_home_page.lastname == contact_from_edit_page.lastname
#     assert contact_from_home_page.address == contact_from_edit_page.address
#     assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
#     assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
#
# def test_phones_on_contact_view_page(app):
#     contact_from_view_page = app.contact.get_contact_from_view_page(0)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
#     assert contact_from_view_page.cell_phone == contact_from_edit_page.cell_phone
#     assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
#     assert contact_from_view_page.secondary_phone == contact_from_edit_page.secondary_phone
