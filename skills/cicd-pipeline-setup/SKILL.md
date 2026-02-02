---
name: cicd-pipeline-setup
description: Create CI/CD pipelines for automated testing, building, and deployment
---

# CI/CD Pipeline Setup Skill

## When to Use This Skill

- Setting up GitHub Actions, GitLab CI, or Jenkins pipelines
- Automating tests, builds, and deployments
- Implementing blue-green or canary deployments
- Setting up Docker image builds
- Configuring deployment environments
- Implementing security scanning

## Quick Start

```
/cicd-pipeline-setup <application_technology_stack>
```

## GitHub Actions Pipeline Example

```yaml
name: CI/CD Pipeline
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: 18

      - name: Install dependencies
        run: npm ci

      - name: Lint
        run: npm run lint

      - name: Unit tests
        run: npm run test:unit

      - name: Integration tests
        run: npm run test:integration

      - name: E2E tests
        run: npm run test:e2e

      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage/coverage-final.json

  build:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v3
      - name: Build Docker image
        run: docker build -t myapp:${{ github.sha }} .

      - name: Push to registry
        run: docker push myapp:${{ github.sha }}

  deploy:
    needs: build
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - name: Deploy to production
        env:
          DEPLOY_KEY: ${{ secrets.DEPLOY_KEY }}
        run: |
          ssh -i $DEPLOY_KEY user@prod.example.com \
            "docker pull myapp:${{ github.sha }} && \
             docker run -d myapp:${{ github.sha }}"
```

## Pipeline Stages

1. **Trigger**: On push/PR
2. **Lint**: Code quality checks
3. **Test**: Unit, integration, E2E
4. **Build**: Compile/Docker image
5. **Security**: Vulnerability scanning
6. **Deploy**: Staging or production

## Docker Example

```dockerfile
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY --from=builder /app/dist ./dist
CMD ["node", "dist/server.js"]
```

## Best Practices

1. **Fast Feedback**: Tests complete in minutes
2. **Fail Fast**: Stop on first failure
3. **Automate**: Everything should be automated
4. **Security**: Scan dependencies, run SAST
5. **Notifications**: Alert on failures
6. **Rollback**: Easy to revert deployments

## Integration with Other Skills

- **`docker-setup`**: Container building
- **`kubernetes-setup`**: Deployment orchestration
- **`monitoring-setup`**: Deploy monitoring
- **`security-scanning`**: Security scanning

