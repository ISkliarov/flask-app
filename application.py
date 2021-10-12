from flask import Flask

application = Flask(__name__)

@application.route("/")
def index():
    return "Hello world from Flask main Page"

@application.route("/help")
def helppage():
    return "<b><font color = blue>This is help page of my-app</b>"

@application.route("/user")
def userpage():
    return "Users main page version2"

@application.route("/user/<username>")
def show_user_page(username):
    return "Hello from " + username.upper() + " name is variable"

@application.route("/path/<path:subpath>")
def print_subpath(subpath):
    return "Subpath is: " + subpath

@application.route("/kvadrat/<int:x>")
def calc_kvadrat(x):
    return "Kvadrat ot: " + str(x) + " = " + str(x*x)

@application.route("/htmlpage")
def show_html_page():
    myfile = open("index.html", mode='r')
    page = myfile.read()
    myfile.close()
    return page

if __name__ == "__main__":
#    application.debug = True
#    application.env = "Testing"
    application.run()