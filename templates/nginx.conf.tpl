events {}

http {
    log_format swiftdeploy '$time_iso8601 | $status | ${request_time}s | $upstream_addr | "$request"';

    access_log /var/log/nginx/access.log swiftdeploy;

    upstream swiftdeploy_app {
        server swiftdeploy-app:{{APP_PORT}};
    }

    server {
        listen 80;

        proxy_connect_timeout {{PROXY_TIMEOUT}}s;
        proxy_send_timeout {{PROXY_TIMEOUT}}s;
        proxy_read_timeout {{PROXY_TIMEOUT}}s;

        add_header X-Deployed-By swiftdeploy always;

        location / {
            proxy_pass http://swiftdeploy_app;
            proxy_http_version 1.1;
            proxy_set_header Host $host;
            proxy_set_header Connection "";
            proxy_set_header X-Real-IP $remote_addr;
            proxy_pass_header X-Mode;
        }

        error_page 502 503 504 /custom_error.json;

        location = /custom_error.json {
            internal;
            default_type application/json;
            return 503 '{"error":"upstream unavailable","code":"503","service":"swiftdeploy","contact":"{{CONTACT}}"}';
        }
    }
}
