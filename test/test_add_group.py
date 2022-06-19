def test_add_group(app, data_groups):
    group = data_groups
    old_groups_list = app.group.get_groups_list()
    app.group.create(group)
    new_groups_list = app.group.get_groups_list()
    old_groups_list.append(group)
    assert sorted(old_groups_list) == sorted(new_groups_list)