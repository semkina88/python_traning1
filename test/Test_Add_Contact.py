# -*- coding: utf-8 -*-
import pytest
from class_for_test import Contact
from application import ApplicationContact


@pytest.fixture
def app(request):
    fixture = ApplicationContact()
    request.addfinalizer(fixture.deastroy)
    return fixture


def test_Add_Contact(app):
    app.login(username="admin", password="secret")
    app.Creat_new_contact(Contact(firstname="ytf", middlename="rsth", lastname="fxgh", nickname="gfx",
                                  title="gfxh", company="vbn", address="xfr", home="12", mobile="3214", work="325",
                                  fax="45",
                                  email="456", email2="56", email3="78", address2="8876", phone2="ch6", notes="hkt6"))
    app.logout()


def test_Add_empty_Contact(app):
    app.login(username="admin", password="secret")
    app.Creat_new_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="",
                                  company="", address="", home="", mobile="", work="", fax="",
                                  email="", email2="", email3="", address2="",
                                  phone2="", notes=""))
    app.logout()
    # app.logout()
