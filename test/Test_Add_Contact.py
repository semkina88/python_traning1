# -*- coding: utf-8 -*-

from model.class_for_test import Contact


def test_Add_Contact(app):
    app.contact.create(Contact(firstname="ytf", middlename="rsth", lastname="fxgh", nickname="gfx",
                                  title="gfxh", company="vbn", address="xfr", home="12", mobile="3214", work="325",
                                  fax="45",
                                  email="456", email2="56", email3="78", address2="8876", phone2="ch6", notes="hkt6"))



def test_Add_empty_Contact(app):
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="",
                                  company="", address="", home="", mobile="", work="", fax="",
                                  email="", email2="", email3="", address2="",
                                  phone2="", notes=""))

