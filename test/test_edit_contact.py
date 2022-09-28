from model.class_for_test import Contact

def test_edit(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="fiu"))
    app.contact.edit(Contact(firstname="yfgf", middlename="sth", lastname="tryh", nickname="hgm",
                                  title="gfxgh", company="vbghjn", address="xhfgfr", home="1y52", mobile="3214", work="326575",
                                  fax="4545",
                                  email="459806", email2="5645", email3="73578", address2="878876", phone2="ch656", notes="hk56t6"))
