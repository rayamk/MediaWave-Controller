from flask import Flask, render_template, jsonify
from services.tv_monitor import get_tv_status

app = Flask(__name__)
TV_IP = "192.168.1.100"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/status")
def status():
    return jsonify({"status": get_tv_status(TV_IP)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

