from flask import Flask, render_template, jsonify
import sys, os

# Add Backend folder to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Backend')))
from audio import main   # ✅ import main() from audio.py

app = Flask(__name__, template_folder="Frontend/templates", static_folder="Frontend/static")

@app.route("/")
def index():
    return render_template("index2.html")

@app.route("/start-camera", methods=["POST"])
def start_camera():
    main()   # ✅ calls Backend/audio.py → main()
    return jsonify({"status": "Camera started"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


