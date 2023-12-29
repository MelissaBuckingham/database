# Initializes a new Flask application

from flask import Flask
app = Flask(__name__)


# Defines a route for the home page that returns a greeting

@app.route('/')
def home():
    return 'Hello, Flask!'



# Runs the Flask app with debug mode enabled


if __name__ == '__main__':
    app.run(debug=True)
