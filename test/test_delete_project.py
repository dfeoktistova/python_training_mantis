from model.project import Project
import random
import string


def random_string(max_len):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(1, max_len))]).rstrip()


def test_add_project(app):
    app.session.login("administrator", "root")
    if len(app.project.get_project_list()) == 0:
        app.project.create_new_project(Project(project_name="projects_new"))
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project(project)
    new_projects = app.project.get_project_list()
    old_projects.remove(project)
    assert sorted(new_projects, key=Project.sort_by_name) == sorted(old_projects, key=Project.sort_by_name)