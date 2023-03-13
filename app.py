from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World! This is a sample Python Web App deployed to Azure App Services"

