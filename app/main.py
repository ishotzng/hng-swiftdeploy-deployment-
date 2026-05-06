import os
import time
import random
from flask import Flask, jsonify, request, Response
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

START_TIME = time.time()
CHAOS = {"mode": None, "duration": 0, "rate": 0}

MODE = os.getenv("MODE", "stable")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

http_requests_total = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "path", "status_code"]
)

http_request_duration_seconds = Histogram(
    "http_request_duration_seconds",
    "HTTP request latency in seconds",
    ["method", "path"],
    buckets=[0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10]
)

app_uptime_seconds = Gauge(
    "app_uptime_seconds",
    "Application uptime in seconds"
)

app_mode = Gauge(
    "app_mode",
    "Application mode, 0 stable, 1 canary"
)

chaos_active = Gauge(
    "chaos_active",
    "Chaos state, 0 none, 1 slow, 2 error"
)


def update_state_metrics():
    app_uptime_seconds.set(int(time.time() - START_TIME))
    app_mode.set(1 if MODE == "canary" else 0)

    if CHAOS["mode"] == "slow":
        chaos_active.set(1)
    elif CHAOS["mode"] == "error":
        chaos_active.set(2)
    else:
        chaos_active.set(0)


@app.before_request
def before_request():
    request.start_time = time.time()

    if MODE == "canary":
        if CHAOS["mode"] == "slow":
            time.sleep(int(CHAOS["duration"]))

        if CHAOS["mode"] == "error":
            if random.random() < float(CHAOS["rate"]):
                response = jsonify({"error": "chaos error active"})
                response.status_code = 500
                return response

    return None


@app.after_request
def after_request(response):
    latency = time.time() - getattr(request, "start_time", time.time())

    http_requests_total.labels(
        method=request.method,
        path=request.path,
        status_code=str(response.status_code)
    ).inc()

    http_request_duration_seconds.labels(
        method=request.method,
        path=request.path
    ).observe(latency)

    update_state_metrics()

    if MODE == "canary":
        response.headers["X-Mode"] = "canary"

    return response


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


@app.get("/metrics")
def metrics():
    update_state_metrics()
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


@app.post("/chaos")
def chaos():
    if MODE != "canary":
        return jsonify({"error": "chaos endpoint only works in canary mode"}), 403

    body = request.get_json(force=True)

    if body.get("mode") == "slow":
        CHAOS["mode"] = "slow"
        CHAOS["duration"] = int(body.get("duration", 1))
        update_state_metrics()
        return jsonify({"status": "slow chaos enabled"})

    if body.get("mode") == "error":
        CHAOS["mode"] = "error"
        CHAOS["rate"] = float(body.get("rate", 0.5))
        update_state_metrics()
        return jsonify({"status": "error chaos enabled"})

    if body.get("mode") == "recover":
        CHAOS["mode"] = None
        CHAOS["duration"] = 0
        CHAOS["rate"] = 0
        update_state_metrics()
        return jsonify({"status": "chaos recovered"})

    return jsonify({"error": "invalid chaos mode"}), 400


if __name__ == "__main__":
    port = int(os.getenv("APP_PORT", "3000"))
    app.run(host="0.0.0.0", port=port)
