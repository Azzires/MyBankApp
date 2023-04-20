
from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template(
        "main/index.html"

    )
@app.route("/user")
def user_information():
    return render_template(
        "user/index.html"
    )
# @app.route("/app")
# def nginx_test():
#     return render_template(
        
#     )

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)