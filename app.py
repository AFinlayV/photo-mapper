from flask import Flask, jsonify, render_template, url_for
import os
from photo_parser import parse_photo_metadata

app = Flask(__name__)

TEST_PHOTOS_DIR = "static"

@app.route('/photos', methods=['GET'])
def get_photos():
    """Return a list of photos with parsed metadata."""
    photos = []
    for filename in os.listdir(TEST_PHOTOS_DIR):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            photo_path = os.path.join(TEST_PHOTOS_DIR, filename)
            metadata = parse_photo_metadata(photo_path)
            metadata["image_url"] = url_for('static', filename=filename)
            photos.append(metadata)

    return jsonify(photos)

@app.route('/display', methods=['GET'])
def display_photos():
    """Render a webpage showing photos and their GPS coordinates."""
    photos = []
    for filename in os.listdir(TEST_PHOTOS_DIR):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            photo_path = os.path.join(TEST_PHOTOS_DIR, filename)
            metadata = parse_photo_metadata(photo_path)
            metadata["image_url"] = url_for('static', filename=filename)
            photos.append(metadata)

    return render_template("display.html", photos=photos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
