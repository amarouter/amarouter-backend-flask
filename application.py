from flask import Flask

application = Flask(__name__)

@application.route('/')
def landing_page():
    return "Amarouter Backend"

if __name__ == "__main__":
    application.run()
