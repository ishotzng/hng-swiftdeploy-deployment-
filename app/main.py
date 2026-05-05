import os
import time
import random
from flask import Flask, jsonify, request

app = Flask(__name__)

START_TIME = time.time()
CHAOS = {"mode": None, "duration": 0, "rate": 0}

MODE = os.getenv("MODE", "stable")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")


@app.after_request
def add_headers(response):
    if MODE == "canary":
        response.headers["X-Mode"] = "canary"
    return response


@app.before_request
def apply_chaos():
    if MODE != "canary":
        return None

    if CHAOS["mode"] == "slow":
        time.sleep(int(CHAOS["duration"]))

    if CHAOS["mode"] == "error":
        if random.random() < float(CHAOS["rate"]):
            return jsonify({"error": "chaos error active"}), 500

    return None


@app.get("/")
def home():
    return jsonify({
        "message": f"Welcome to SwiftDeploy running in {MODE} mode",
        "mode": MODE,
        "version": APP_VERSION,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    })


@app.get("/healthz")
def healthz():
    return jsonify({
        "status": "ok",
        "mode": MODE,
        "uptime_seconds": int(time.time() - START_TIME)
    })


@app.post("/chaos")
def chaos():
    if MODE != "canary":
        return jsonify({"error": "chaos endpoint only works in canary mode"}), 403

    body = request.get_json(force=True)

    if body.get("mode") == "slow":
        CHAOS["mode"] = "slow"
        CHAOS["duration"] = int(body.get("duration", 1))
        return jsonify({"status": "slow chaos enabled"})

    if body.get("mode") == "error":
        CHAOS["mode"] = "error"
        CHAOS["rate"] = float(body.get("rate", 0.5))
        return jsonify({"status": "error chaos enabled"})

    if body.get("mode") == "recover":
        CHAOS["mode"] = None
        CHAOS["duration"] = 0
        CHAOS["rate"] = 0
        return jsonify({"status": "chaos recovered"})

    return jsonify({"error": "invalid chaos mode"}), 400


if __name__ == "__main__":
    port = int(os.getenv("APP_PORT", "3000"))
    app.run(host="0.0.0.0", port=port)
