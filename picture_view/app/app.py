import os
import threading
import time
from datetime import datetime, timedelta
from pathlib import Path

from flask import Flask, abort, jsonify, render_template, send_file

app = Flask(__name__)

IMAGE_FOLDER = os.environ.get("IMAGE_FOLDER", "/share/camera")
DELETE_AFTER_DAYS = int(os.environ.get("DELETE_AFTER_DAYS", "30"))
WEB_PORT = int(os.environ.get("WEB_PORT", "8200"))

ALLOWED_EXT = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp"}


def get_images():
    folder = Path(IMAGE_FOLDER)
    if not folder.exists():
        return []
    images = []
    for f in folder.iterdir():
        if f.suffix.lower() in ALLOWED_EXT:
            try:
                mtime = f.stat().st_mtime
                images.append({"name": f.name, "mtime": mtime, "path": str(f)})
            except OSError:
                pass
    images.sort(key=lambda x: x["mtime"])
    return images


def cleanup_old_images():
    while True:
        cutoff = time.time() - DELETE_AFTER_DAYS * 86400
        folder = Path(IMAGE_FOLDER)
        if folder.exists():
            for f in folder.iterdir():
                if f.suffix.lower() in ALLOWED_EXT:
                    try:
                        if f.stat().st_mtime < cutoff:
                            f.unlink()
                    except OSError:
                        pass
        time.sleep(3600)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/images")
def api_images():
    images = get_images()
    result = []
    for img in images:
        dt = datetime.fromtimestamp(img["mtime"])
        result.append({
            "name": img["name"],
            "date": dt.strftime("%Y-%m-%d"),
            "datetime": dt.strftime("%Y-%m-%d %H:%M:%S"),
            "timestamp": img["mtime"],
        })
    return jsonify(result)


@app.route("/api/image/<path:filename>")
def api_image(filename):
    folder = Path(IMAGE_FOLDER)
    filepath = (folder / filename).resolve()
    if not str(filepath).startswith(str(folder.resolve())):
        abort(403)
    if not filepath.exists() or filepath.suffix.lower() not in ALLOWED_EXT:
        abort(404)
    return send_file(filepath)


@app.route("/api/stats")
def api_stats():
    images = get_images()
    total = len(images)
    days_set = set()
    for img in images:
        dt = datetime.fromtimestamp(img["mtime"])
        days_set.add(dt.strftime("%Y-%m-%d"))
    return jsonify({
        "total": total,
        "days": len(days_set),
        "delete_after_days": DELETE_AFTER_DAYS,
        "folder": IMAGE_FOLDER,
    })


if __name__ == "__main__":
    t = threading.Thread(target=cleanup_old_images, daemon=True)
    t.start()
    app.run(host="0.0.0.0", port=WEB_PORT, debug=False)
