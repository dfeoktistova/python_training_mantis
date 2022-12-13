import re


class SignupHelper:

    def __init__(self, app):
        self.app = app

    def new_user(self, username, email, password):
        wd = self.app.wd
        wd.get(self.app.base_url + "/signup_page.php")
        wd.find_element("name", "username").send_keys(username)
        wd.find_element("name", "email").send_keys(email)
        wd.find_element_by_css_selector('input[type="submit"]').click()

        mail = self.app.mail.get_mail(username, password, "[MantisBT] Account registration")
        url = self.extract_confirmation_url(mail)

        wd.get(url)
        wd.find_element("name", "password").send_keys(password)
        wd.find_element("name", "password_confirm").send_keys(password)
        wd.find_element_by_css_selector('input[value="Update User"]').click()


    def extract_confirmation_url(self, text):
        return re.search("http://.*$", text, re.MULTILINE).group(0)