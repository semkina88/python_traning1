# -*- coding: utf-8 -*-
from model.class_for_test import Group

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="name1", header="onn", footer="dfg"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
