from flask import Flask, request, jsonify
import librosa
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return 'AI Music Analyzer Running!'

@app.route('/analyze', methods=['POST'])
def analyze_audio():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    y, sr = librosa.load(file, sr=None)
    duration = librosa.get_duration(y=y, sr=sr)

    return jsonify({
        'duration_sec': duration,
        'sample_rate': sr
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)