# -*- coding: utf-8 -*-
from model.class_for_test import Group


def test_add_group(app):
    app.group.create(Group(name="name1", header="onn", footer="dfg"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
