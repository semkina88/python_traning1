import random
from random import randrange

from model.class_for_test import Contact


def test_modify_contact_firstname(app, db, check_ui):
    # если контактов нет создадим контакт
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="bla"))
    # получаем текущий список контактов из бд
    old_contacts = db.get_contact_list()

    # Создадим сущность контакт с определенным именем
    contact = Contact(firstname="kjgu")
    # выбиарем слуйное число по длине списка контактов
    index = randrange(len(old_contacts))
    # Присвоим созданной сущности id выбранного контакт из списка
    contact.id = old_contacts[index].id
    # Через интерфейс изменим имя для выбранного контакта
    app.contact.modify_contact_by_id(contact.id, contact)
    # Получим актуальный список контактов из бд
    new_contacts = db.get_contact_list()
    # Проведем сравнение имен для имеющейся сущности и контакта из актуального списка с известным id
    contact.firstname == new_contacts[index].firstname
    # Установим флаг для проведения проверки
    check_ui = True
    if check_ui:
        # проверим состав списков
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


    # selection = random.choice(old_contacts)
    # contact.id = old_contacts[index].id
    # app.contact.modify_contact_by_id(selection.id, contact)
    # new_contacts = db.get_contact_list()
    # old_contacts[index] = contact
    # old_contacts[index].id = new_contacts[index].id
    # old_contacts[index].firstname = new_contacts[index].firstname
    # assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    # if check_ui:
    #     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


