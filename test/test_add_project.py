from model.project import Project
import random
import string


def random_string(max_len):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(1, max_len))]).rstrip()


def test_add_project(app):
    project = Project(name=random_string(5), description=random_string(10))
    #app.session.login("administrator", "root")
    old_projects = app.project.get_project_list()
    app.project.create_new_project(project.project_name)
    app.project.go_to_manage_projects()
    new_projects = app.project.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(new_projects, key=Project.sort_by_name) == sorted(old_projects, key=Project.sort_by_name)