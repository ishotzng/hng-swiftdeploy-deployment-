# SwiftDeploy Audit Report

## Timeline

| Time | Event | Domain | Details |
|---|---|---|---|
| 2026-05-06T11:44:25Z | promote | canary | {"status": "confirmed"} |
| 2026-05-06T11:46:40Z | status_scrape | canary | {"mode": "canary", "uptime_seconds": 136.0, "error_rate": 0.0, "p99_latency_ms": 5.0, "chaos_state": "none", "total_requests": 19} |
| 2026-05-06T11:46:44Z | status_scrape | canary | {"mode": "canary", "uptime_seconds": 140.0, "error_rate": 0.0, "p99_latency_ms": 5.0, "chaos_state": "none", "total_requests": 21} |
| 2026-05-06T11:46:47Z | status_scrape | canary | {"mode": "canary", "uptime_seconds": 144.0, "error_rate": 0.0, "p99_latency_ms": 5.0, "chaos_state": "none", "total_requests": 23} |
| 2026-05-06T11:46:51Z | status_scrape | canary | {"mode": "canary", "uptime_seconds": 148.0, "error_rate": 0.0, "p99_latency_ms": 5.0, "chaos_state": "none", "total_requests": 26} |
| 2026-05-06T11:46:55Z | status_scrape | canary | {"mode": "canary", "uptime_seconds": 151.0, "error_rate": 0.0, "p99_latency_ms": 5.0, "chaos_state": "none", "total_requests": 28} |
| 2026-05-06T11:46:59Z | status_scrape | canary | {"mode": "canary", "uptime_seconds": 155.0, "error_rate": 0.0, "p99_latency_ms": 5.0, "chaos_state": "none", "total_requests": 30} |
| 2026-05-06T11:47:02Z | status_scrape | canary | {"mode": "canary", "uptime_seconds": 159.0, "error_rate": 0.0, "p99_latency_ms": 5.0, "chaos_state": "none", "total_requests": 33} |
| 2026-05-06T11:47:06Z | status_scrape | canary | {"mode": "canary", "uptime_seconds": 163.0, "error_rate": 0.0, "p99_latency_ms": 10.0, "chaos_state": "none", "total_requests": 35} |
| 2026-05-06T11:47:10Z | status_scrape | canary | {"mode": "canary", "uptime_seconds": 166.0, "error_rate": 0.0, "p99_latency_ms": 10.0, "chaos_state": "none", "total_requests": 37} |
| 2026-05-06T11:47:14Z | status_scrape | canary | {"mode": "canary", "uptime_seconds": 170.0, "error_rate": 0.0, "p99_latency_ms": 10.0, "chaos_state": "none", "total_requests": 40} |
| 2026-05-06T11:47:17Z | status_scrape | canary | {"mode": "canary", "uptime_seconds": 174.0, "error_rate": 0.0, "p99_latency_ms": 10.0, "chaos_state": "none", "total_requests": 42} |
| 2026-05-06T11:48:55Z | promote | stable | {"status": "confirmed"} |
| 2026-05-06T11:49:57Z | promote | canary | {"status": "confirmed"} |
| 2026-05-06T11:56:52Z | policy_violation | canary | {"error_rate": 0.0, "p99_latency_ms": 2500.0} |
| 2026-05-06T11:57:42Z | policy_violation | canary | {"error_rate": 0.0, "p99_latency_ms": 2500.0} |
| 2026-05-06T11:59:18Z | promote | stable | {"status": "confirmed"} |
| 2026-05-06T12:02:13Z | deploy | stable | {"status": "healthy"} |
| 2026-05-06T12:03:12Z | promote | canary | {"status": "confirmed"} |
| 2026-05-06T12:03:34Z | policy_violation | canary | {"error_rate": 0.0, "p99_latency_ms": 2500.0} |
| 2026-05-06T12:04:04Z | policy_violation | canary | {"error_rate": 0.0, "p99_latency_ms": 2500.0} |
| 2026-05-06T12:04:04Z | status_scrape | canary | {"mode": "canary", "uptime_seconds": 53.0, "error_rate": 0.0, "p99_latency_ms": 2500.0, "chaos_state": "slow", "total_requests": 27} |
| 2026-05-06T12:04:23Z | policy_violation | canary | {"error_rate": 0.0, "p99_latency_ms": 2500.0} |
| 2026-05-06T12:04:23Z | status_scrape | canary | {"mode": "canary", "uptime_seconds": 71.0, "error_rate": 0.0, "p99_latency_ms": 2500.0, "chaos_state": "slow", "total_requests": 28} |

## Policy Violations

| Time | Domain | Reasons |
|---|---|---|
| 2026-05-06T11:56:52Z | canary | P99 latency too high: 2500ms |
| 2026-05-06T11:57:42Z | canary | P99 latency too high: 2500ms |
| 2026-05-06T12:03:34Z | canary | P99 latency too high: 2500ms |
| 2026-05-06T12:04:04Z | canary | P99 latency too high: 2500ms |
| 2026-05-06T12:04:23Z | canary | P99 latency too high: 2500ms |
