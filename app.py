# from flask import Flask, render_template, jsonify
# import sys, os

# # Add Backend folder to path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Backend')))
# from audio import main   # ✅ import main() from audio.py

# app = Flask(__name__, template_folder="templates", static_folder="static")

# @app.route("/")
# def index():
#     return render_template("index2.html")

# @app.route("/start-camera", methods=["POST"])
# def start_camera():
#     main()   # ✅ calls Backend/audio.py → main()
#     return jsonify({"status": "Camera started"})

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, render_template, jsonify
import sys, os

# Import backend
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Backend')))
import audio   # your audio.py with main()

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def index():
    return render_template("index2.html")

@app.route("/start-camera", methods=["POST"])
def start_camera():
    try:
        audio.main()   # call your main() from audio.py
        return jsonify({"status": "Camera started successfully!"})
    except Exception as e:
        return jsonify({"status": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)