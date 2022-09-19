from model.class_for_test import Group

def test_edit_first_group(app):
    app.group.edit(Group(name="name1", header="one1", footer="twrto1"))
