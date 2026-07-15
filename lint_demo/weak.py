from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/run")
def run_report():
    user_input = request.args.get("name")
    subprocess.call("generate_report " + user_input, shell=True)
    return "done"
