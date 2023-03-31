from flask import (
    Flask,
    render_template,
    send_file,
    request,
    url_for,
    redirect,
    abort,
    make_response,
)
from pymongo import MongoClient
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def default_page():
    return render_template("index.html", mimetype="text/html")


@app.route("/style.css")
def default_page_style():
    return send_file("style.css", mimetype="text/css")


@app.route("/teampage.html")
def team_page():
    return render_template("teampage.html", mimetype="text/html")

@app.route("/terms.html")
def terms_page():
    return render_template("terms.html", mimetype="text/html")

@app.route("/<image_name>")
def display_image(image_name):
    return send_file("Images/" + image_name, mimetype="image/gif")


@app.route("/script.js")
def default_page_script():
    return send_file("templates/script.js", mimetype="text/javascript")

@app.route('/upload',methods=['POST','GET'])
def upload():
    if request.method =='POST':
        video = request.files['file']
        if video:
            filename = secure_filename(video.filename)
            video.save(os.path.join("/data2/dmitrijs", filename))
            return "success!"
        return "Please try again later, and let the team know the upload failed"

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)

