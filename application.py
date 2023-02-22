from flask import Flask
application = Flask(__name__) 


@application.route("/")
def index():
    return "<h1>Hello World!</h1>"


@application.route("/another")
def another():
    return "<h1>Another Page!</h1>"


if __name__ == "__main__":
    application.run(port="4000",debug=True)