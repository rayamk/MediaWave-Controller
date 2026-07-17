from flask import Flask, request, jsonify, render_template
from services.logger import get_logger
from services.tv_monitor import start_monitor
from services.subtitle import translate_subtitle

app = Flask(__name__)
TV_IP = "192.168.1.100"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/status")
def get_status():
    return jsonify({"online": start_monitor(TV_IP)})

@app.route("/translate", methods=['POST'])
def translate():
    data = request.json
    text = data.get("text", "")
    return jsonify({"translated": translate_subtitle(text)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

