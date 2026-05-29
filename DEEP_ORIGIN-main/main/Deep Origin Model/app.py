from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
from model_utils import analyze_fasta

# Upload folder setup
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Flask app setup
app = Flask(__name__, static_folder="static", template_folder="templates")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# Home Route
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


# Prediction Route
@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    f = request.files["file"]

    if f.filename == "":
        return jsonify({"error": "No file selected"}), 400

    filename = secure_filename(f.filename)
    path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    f.save(path)

    try:
        result = analyze_fasta(path)
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Run App (Local + Deployment Ready)
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )