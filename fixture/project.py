from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def go_to_manage_projects(self):
        wd = self.app.wd
        # go to manage page
        wd.get("http://localhost/mantisbt-1.2.20/manage_overview_page.php")
        wd.find_element_by_link_text("Manage").click()
        # go to manage project page
        wd.find_element_by_link_text("Manage Projects").click()

    def create_new_project(self, project_name):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project_name)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    project_cache = None

    def get_project_list(self):
        wd = self.app.wd
        self.go_to_manage_projects()
        project_list = []
        for element in wd.find_elements_by_xpath("//table[3]/tbody/tr"):
            if element.get_attribute("class") not in ('', 'row-category'):
                cells = element.find_elements_by_tag_name("td")
                project_name = cells[0].text
                project_list.append(Project(project_name=project_name))
        return list(filter(None, project_list))

    def delete_project_by_name(self, name):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(text(),'" + name + "')]").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_css_selector("input.button").click()
        self.project_cash = None