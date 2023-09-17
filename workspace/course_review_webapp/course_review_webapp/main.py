"""
main.py

This file contains the main entry point of the web application.
"""

from course_review_webapp.models import User, Course, Review, Search, Filter, Sort, Authentication

def main():
    # Open web app
    web_app = WebApp()
    web_app.open()

class WebApp:
    def __init__(self):
        self.authentication = Authentication()

    def open(self):
        # Check if user is logged in
        if not self.authentication.is_logged_in():
            # User is not logged in
            self.display_login_signup_page()
        else:
            # User is logged in
            self.display_homepage()

    def display_login_signup_page(self):
        # TODO: Implement the display_login_signup_page function
        pass

    def display_homepage(self):
        # TODO: Implement the display_homepage function
        pass

if __name__ == "__main__":
    main()
