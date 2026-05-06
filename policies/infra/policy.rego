package infra

default allow := false

allow if {
    input.disk_free_gb >= data.infra.limits.min_disk_gb
    input.cpu_load <= data.infra.limits.max_cpu_load
}

reasons contains msg if {
    input.disk_free_gb < data.infra.limits.min_disk_gb
    msg := sprintf("Disk free too low: %vGB", [input.disk_free_gb])
}

reasons contains msg if {
    input.cpu_load > data.infra.limits.max_cpu_load
    msg := sprintf("CPU load too high: %v", [input.cpu_load])
}
