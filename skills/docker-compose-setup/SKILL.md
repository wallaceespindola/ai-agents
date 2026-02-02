# Docker Compose Setup Skill

**Master Docker Compose for multi-container applications. Configure services, networks, volumes, health checks, and production deployments.**

## Overview

Docker Compose enables defining and running multi-container applications. This skill covers configuration, service orchestration, and best practices.

**What it does:**
- Defines multi-container applications
- Manages networks and inter-service communication
- Configures volumes and storage
- Implements health checks
- Manages environment variables and secrets
- Handles service dependencies
- Enables scaling and resource limits
- Supports development and production workflows

**Perfect for:**
- Local development environments
- Testing multi-service applications
- Microservices orchestration
- Database and cache services
- Complete application stacks

---

## When to Use This Skill

Use Docker Compose when you need to:

- **Run multiple services locally** for development
- **Test microservices** together
- **Define application stack** in code
- **Manage service dependencies** and startup order
- **Persist data** with volumes
- **Network containers** together
- **Scale services** for testing
- **Document infrastructure** for team

---

## Quick Start (10 Minutes)

### 1. Create docker-compose.yml

```yaml
version: '3.9'

services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      DATABASE_URL: postgresql://postgres:password@db:5432/myapp
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: password
      POSTGRES_DB: myapp
    volumes:
      - db_data:/var/lib/postgresql/data

volumes:
  db_data:
```

### 2. Build and Start

```bash
docker-compose up -d
# Services start in background
```

### 3. View Status

```bash
docker-compose ps
docker-compose logs app
docker-compose logs -f app  # Follow logs
```

### 4. Stop Services

```bash
docker-compose down
# Removes containers, keeps volumes
```

---

## How It Works

### 1. Service Configuration

**Basic Service:**

```yaml
services:
  web:
    image: nginx:latest
    ports:
      - "80:80"
    volumes:
      - ./html:/usr/share/nginx/html
    environment:
      - NGINX_HOST=example.com
```

**Build from Dockerfile:**

```yaml
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
      args:
        NODE_ENV: production
    ports:
      - "3000:3000"
```

**Service with Credentials:**

```yaml
services:
  api:
    image: myapi:1.0.0
    container_name: api-server
    restart: always
    ports:
      - "8080:8080"
    environment:
      PORT: 8080
      LOG_LEVEL: info
    networks:
      - app-network
```

### 2. Networks

**Default Network:**

```yaml
services:
  app:
    image: myapp:1.0.0
    # Automatically on 'default' network
    # Access postgres via: postgres:5432
```

**Custom Network:**

```yaml
version: '3.9'

services:
  app:
    image: myapp:1.0.0
    networks:
      - backend
      - frontend

  postgres:
    image: postgres:15
    networks:
      - backend  # Only app can access

  nginx:
    image: nginx:latest
    networks:
      - frontend

networks:
  backend:
    driver: bridge
  frontend:
    driver: bridge
```

**Service Discovery:**

```yaml
services:
  app:
    environment:
      DATABASE_URL: postgresql://postgres:password@db:5432/myapp
      # Services accessible by name: db, cache, api
      CACHE_URL: redis://cache:6379

  db:
    image: postgres:15
    networks:
      - backend

  cache:
    image: redis:7
    networks:
      - backend
```

### 3. Volumes

**Named Volumes (persistent):**

```yaml
services:
  postgres:
    image: postgres:15
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
    driver: local
```

**Bind Mounts (local directory):**

```yaml
services:
  app:
    image: node:20
    volumes:
      - ./src:/app/src        # Mount local code
      - /app/node_modules     # Anonymous volume for deps
    working_dir: /app
    command: npm start
```

**Volume Options:**

```yaml
volumes:
  - type: bind
    source: ./data
    target: /data
    read_only: true

  - type: volume
    source: db_data
    target: /var/lib/postgresql/data

  - type: tmpfs
    target: /tmp
```

### 4. Depends On

**Service Dependencies:**

```yaml
services:
  app:
    image: myapp:1.0.0
    depends_on:
      - db
      - cache
    # Waits for db and cache to start
    # NOT for them to be healthy

  db:
    image: postgres:15

  cache:
    image: redis:7
```

**Wait for Healthiness:**

```yaml
services:
  app:
    image: myapp:1.0.0
    depends_on:
      db:
        condition: service_healthy

  db:
    image: postgres:15
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
```

### 5. Health Checks

```yaml
services:
  app:
    image: myapp:1.0.0
    ports:
      - "3000:3000"
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

  postgres:
    image: postgres:15
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
```

### 6. Environment Variables

**Inline Environment:**

```yaml
services:
  app:
    image: myapp:1.0.0
    environment:
      PORT: 3000
      NODE_ENV: production
      DATABASE_URL: postgresql://user:pass@db:5432/myapp
```

**From .env File:**

```yaml
services:
  app:
    image: myapp:1.0.0
    env_file:
      - .env
      - .env.production
```

**.env File:**

```
PORT=3000
NODE_ENV=production
DATABASE_URL=postgresql://user:pass@db:5432/myapp
```

**Secrets (Docker Swarm):**

```yaml
version: '3.9'

services:
  app:
    image: myapp:1.0.0
    secrets:
      - db_password
    environment:
      DB_PASSWORD_FILE: /run/secrets/db_password

secrets:
  db_password:
    file: ./secrets/db_password.txt
```

### 7. Resource Limits

```yaml
services:
  app:
    image: myapp:1.0.0
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
    # Or (older syntax)
    mem_limit: 512m
    cpus: 0.5
```

### 8. Scaling

```yaml
services:
  worker:
    image: worker:1.0.0
    deploy:
      replicas: 3
    # Or command line: docker-compose up -d --scale worker=5
```

---

## Configuration

### Complete Production Setup

```yaml
version: '3.9'

services:
  nginx:
    image: nginx:latest
    container_name: nginx
    restart: always
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./ssl:/etc/nginx/ssl:ro
      - ./html:/usr/share/nginx/html:ro
    networks:
      - frontend
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost"]
      interval: 30s
      timeout: 10s
      retries: 3

  app:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: app
    restart: always
    ports:
      - "3000:3000"
    environment:
      NODE_ENV: production
      PORT: 3000
      DATABASE_URL: postgresql://${DB_USER}:${DB_PASSWORD}@db:5432/${DB_NAME}
      REDIS_URL: redis://cache:6379
      LOG_LEVEL: info
    volumes:
      - app_logs:/var/log/app
    depends_on:
      db:
        condition: service_healthy
      cache:
        condition: service_healthy
    networks:
      - frontend
      - backend
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 1G
        reservations:
          cpus: '0.5'
          memory: 512M

  db:
    image: postgres:15
    container_name: postgres
    restart: always
    environment:
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: ${DB_NAME}
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
    networks:
      - backend
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER}"]
      interval: 10s
      timeout: 5s
      retries: 5
    deploy:
      resources:
        limits:
          memory: 2G

  cache:
    image: redis:7
    container_name: redis
    restart: always
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    networks:
      - backend
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5
    command: redis-server --appendonly yes
    deploy:
      resources:
        limits:
          memory: 512M

volumes:
  postgres_data:
  redis_data:
  app_logs:

networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
```

---

## Examples

### Example 1: Node.js + PostgreSQL + Redis

```yaml
version: '3.9'

services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      DATABASE_URL: postgresql://user:password@db:5432/myapp
      REDIS_URL: redis://cache:6379
    depends_on:
      - db
      - cache
    networks:
      - app-network

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: myapp
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - app-network

  cache:
    image: redis:7
    networks:
      - app-network

volumes:
  postgres_data:

networks:
  app-network:
```

### Example 2: Django + PostgreSQL + Celery

```yaml
version: '3.9'

services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    ports:
      - "8000:8000"
    environment:
      DEBUG: "True"
      DATABASE_URL: postgresql://user:password@db:5432/myapp
      REDIS_URL: redis://redis:6379
    volumes:
      - .:/app
    depends_on:
      - db
      - redis

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: myapp
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7

  celery:
    build: .
    command: celery -A myapp worker -l info
    environment:
      DATABASE_URL: postgresql://user:password@db:5432/myapp
      REDIS_URL: redis://redis:6379
    volumes:
      - .:/app
    depends_on:
      - db
      - redis

  celery_beat:
    build: .
    command: celery -A myapp beat -l info
    environment:
      DATABASE_URL: postgresql://user:password@db:5432/myapp
      REDIS_URL: redis://redis:6379
    volumes:
      - .:/app
    depends_on:
      - db
      - redis

volumes:
  postgres_data:
```

### Example 3: Microservices Architecture

```yaml
version: '3.9'

services:
  nginx:
    image: nginx:latest
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - api_gateway
    networks:
      - frontend

  api_gateway:
    build: ./gateway
    ports:
      - "3000:3000"
    environment:
      USER_SERVICE_URL: http://user-service:8001
      PRODUCT_SERVICE_URL: http://product-service:8002
      ORDER_SERVICE_URL: http://order-service:8003
    networks:
      - frontend
      - backend

  user_service:
    build: ./user-service
    environment:
      DATABASE_URL: postgresql://user:pass@db:5432/users
    depends_on:
      - db
    networks:
      - backend

  product_service:
    build: ./product-service
    environment:
      DATABASE_URL: postgresql://user:pass@db:5432/products
    depends_on:
      - db
    networks:
      - backend

  order_service:
    build: ./order-service
    environment:
      DATABASE_URL: postgresql://user:pass@db:5432/orders
      USER_SERVICE_URL: http://user-service:8001
      PRODUCT_SERVICE_URL: http://product-service:8002
    depends_on:
      - db
    networks:
      - backend

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
    volumes:
      - db_data:/var/lib/postgresql/data
    networks:
      - backend

volumes:
  db_data:

networks:
  frontend:
  backend:
```

### Example 4: Override Configuration

`docker-compose.yml`:

```yaml
version: '3.9'
services:
  app:
    image: myapp:1.0.0
    ports:
      - "3000:3000"
```

`docker-compose.override.yml`:

```yaml
# Automatically merged for development
services:
  app:
    build: .
    volumes:
      - .:/app
    environment:
      DEBUG: "True"
```

### Example 5: Production Deployment

```yaml
version: '3.9'

services:
  app:
    image: myregistry/app:1.0.0
    restart: always
    deploy:
      replicas: 3
    networks:
      - backend
    environment:
      NODE_ENV: production
      LOG_LEVEL: error
    # No volumes, no ports (behind load balancer)

  postgres:
    image: postgres:15
    restart: always
    networks:
      - backend
    volumes:
      - /persistent-storage/postgres:/var/lib/postgresql/data
    environment:
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}

networks:
  backend:
    driver: overlay  # For Swarm mode
```

---

## Best Practices

### 1. Use .dockerignore

```
node_modules
.git
.gitignore
README.md
.env
.DS_Store
```

### 2. Health Checks Required

```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost/health"]
  interval: 30s
  timeout: 10s
  retries: 3
```

### 3. Resource Limits

```yaml
deploy:
  resources:
    limits:
      cpus: '1'
      memory: 1G
```

### 4. Use Secrets for Sensitive Data

```yaml
environment:
  DB_PASSWORD_FILE: /run/secrets/db_password
secrets:
  db_password:
    file: ./secrets/db_password.txt
```

### 5. Version Your Images

```yaml
image: postgres:15-alpine  # Specific version
# NOT: image: postgres:latest
```

---

## Integration with Other Skills

Docker Compose integrates with:

- **kubernetes-yaml-generation** - Deploy to K8s
- **build-optimization** - Optimize image builds
- **secrets-management** - Manage environment variables
- **yaml-validation-config** - Validate compose files

---

## Complete Command Reference

```bash
# Start/Stop
docker-compose up               # Start in foreground
docker-compose up -d           # Start in background
docker-compose down            # Stop and remove
docker-compose stop            # Stop without removing
docker-compose start           # Start stopped containers

# Logs
docker-compose logs            # View all logs
docker-compose logs app        # Specific service
docker-compose logs -f app     # Follow logs

# Execute
docker-compose exec app bash   # Run command in service

# Status
docker-compose ps              # List services
docker-compose top             # Process list

# Build
docker-compose build           # Build images
docker-compose build --no-cache

# Clean
docker-compose down -v         # Remove volumes
docker system prune            # Remove unused resources
```

---

*Last Updated: 2026-02-02*
*Part of: AI Agents & Skills Repository*
