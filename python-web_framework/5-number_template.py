#!/usr/bin/python3
"""
Flask application that renders a template with a number.
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Renders an HTML page displaying a number inside an <h1> tag"""
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
