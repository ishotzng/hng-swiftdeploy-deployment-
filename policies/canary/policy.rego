package canary

default allow := false

allow if {
    input.error_rate <= data.canary.thresholds.max_error_rate
    input.p99_latency_ms <= data.canary.thresholds.max_latency_ms
}

reasons contains msg if {
    input.error_rate > data.canary.thresholds.max_error_rate
    msg := sprintf("Error rate too high: %v%%", [input.error_rate])
}

reasons contains msg if {
    input.p99_latency_ms > data.canary.thresholds.max_latency_ms
    msg := sprintf("P99 latency too high: %vms", [input.p99_latency_ms])
}
