services:
  app:
    image: {{SERVICE_IMAGE}}
    container_name: swiftdeploy-app
    environment:
      MODE: "{{MODE}}"
      APP_VERSION: "{{APP_VERSION}}"
      APP_PORT: "{{APP_PORT}}"
    networks:
      - swiftdeploy-net
    restart: {{RESTART_POLICY}}
    user: "1000:1000"
    cap_drop:
      - ALL
    security_opt:
      - no-new-privileges:true
    volumes:
      - swiftdeploy-logs:/logs
    healthcheck:
      test: ["CMD", "python", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:{{APP_PORT}}/healthz')"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 10s

  nginx:
    image: {{NGINX_IMAGE}}
    container_name: swiftdeploy-nginx
    ports:
      - "{{NGINX_PORT}}:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - swiftdeploy-logs:/var/log/nginx
    depends_on:
      app:
        condition: service_healthy
    networks:
      - swiftdeploy-net
    restart: {{RESTART_POLICY}}
    security_opt:
      - no-new-privileges:true
    command: >
      sh -c "touch /var/log/nginx/access.log &&
             chmod 666 /var/log/nginx/access.log &&
             nginx -g 'daemon off;'"

networks:
  swiftdeploy-net:
    name: {{NETWORK_NAME}}
    driver: {{NETWORK_DRIVER}}

volumes:
  swiftdeploy-logs:
