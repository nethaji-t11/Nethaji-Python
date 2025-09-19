from flask import Flask, render_template_string

app = Flask(__name__)

# Load HTML manually from the same folder
@app.route("/")
def home():
    with open("index.html", "r") as f:
        html_content = f.read()
    return render_template_string(html_content)
