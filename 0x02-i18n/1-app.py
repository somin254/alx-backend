#!/usr/bin/env/python3
""" basic babel setup"""


from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class config:
    """configuration classs for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(config)


@app.route('/')
def index():
    """Render the index page"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
