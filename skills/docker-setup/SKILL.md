---
name: docker-setup
description: Create Dockerfile and docker-compose configurations for containerization
---

# Docker Setup Skill

## When to Use This Skill

- Containerizing applications
- Creating multi-container setups
- Development environment setup
- Production deployment preparation
- Database and service containers

## Quick Start

```
/docker-setup <application_type>
```

## Dockerfile Best Practices

```dockerfile
# Multi-stage build
FROM node:18-alpine AS base
WORKDIR /app

# Install dependencies
FROM base AS dependencies
COPY package*.json ./
RUN npm ci

# Build application
FROM dependencies AS build
COPY . .
RUN npm run build

# Production image
FROM node:18-alpine
WORKDIR /app
ENV NODE_ENV=production
COPY package*.json ./
RUN npm ci --only=production
COPY --from=build /app/dist ./dist
EXPOSE 3000
HEALTHCHECK --interval=30s CMD node healthcheck.js
CMD ["node", "dist/server.js"]
```

## Docker Compose Example

```yaml
version: '3.8'

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

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: myapp
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  cache:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  postgres_data:
```

## Integration with Other Skills

- **`cicd-pipeline-setup`**: Docker builds in CI/CD
- **`kubernetes-setup`**: Kubernetes deployment
- **`monitoring-setup`**: Container monitoring

