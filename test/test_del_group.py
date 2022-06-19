import random


def test_delete_group(app):
    if len(app.group.get_groups_list()) <= 1:
        app.group.create('name_test')
    old_groups_list = app.group.get_groups_list()
    group = random.choice(old_groups_list)
    app.group.delete(group)
    new_groups_list = app.group.get_groups_list()
    old_groups_list.remove(group)
    assert sorted(old_groups_list) == sorted(new_groups_list)