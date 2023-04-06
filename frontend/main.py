from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template(
        "page.html"

    )
@app.route("/information")
def user_information():
    return render_template(
        "information.html"
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)