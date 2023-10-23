from flask import Flask, request, jsonify
from models import Video, Shot
from utils import analyze_shot

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload_video():
    file_path = request.form.get("file_path")
    video = Video(file_path)
    video.save()
    return jsonify({"video_id": video.id})

@app.route("/analyze", methods=["POST"])
def analyze_video():
    video_id = request.form.get("video_id")
    video = Video.get(video_id)
    analyzed_shots = []
    for shot in video.shots:
        analyzed_shot = analyze_shot(shot)
        analyzed_shots.append(analyzed_shot)
    return jsonify({"analyzed_shots": analyzed_shots})

if __name__ == "__main__":
    app.run()
