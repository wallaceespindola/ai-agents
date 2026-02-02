# Secrets Management Skill

**Master environment variables, HashiCorp Vault, GitHub Secrets, AWS Secrets Manager, and key rotation strategies.**

## Overview

Secrets management prevents credential leaks and ensures secure application configuration. This skill covers multiple secret storage and access patterns.

**What it does:**
- Manages environment variables securely
- Implements HashiCorp Vault integration
- Configures GitHub Actions secrets
- Uses AWS Secrets Manager
- Handles secret rotation
- Prevents secret leaks
- Implements access control
- Audits secret usage

**Perfect for:**
- Protecting API keys and credentials
- Multi-environment secret management
- Compliance and auditing
- Automated secret rotation
- Enterprise security

---

## When to Use This Skill

Use Secrets Management when you need to:

- **Secure API keys and tokens** safely
- **Manage secrets across environments** (dev, staging, prod)
- **Rotate credentials** automatically
- **Prevent accidental leaks** to git or logs
- **Control secret access** by role
- **Audit who accessed** which secrets
- **Integrate with CI/CD** securely
- **Store database passwords** securely

---

## Quick Start (10 Minutes)

### 1. Environment Variables (.env)

Create `.env` (never commit):

```bash
DATABASE_URL=postgresql://user:password@localhost/myapp
API_KEY=sk_live_123456789
JWT_SECRET=my_jwt_secret_key
LOG_LEVEL=info
```

Load in application:

```javascript
// Node.js
require('dotenv').config();
const dbUrl = process.env.DATABASE_URL;
```

```python
# Python
from dotenv import load_dotenv
import os
load_dotenv()
db_url = os.getenv('DATABASE_URL')
```

### 2. GitHub Secrets

Set in GitHub UI:

Settings → Secrets and variables → Actions → New repository secret

Or via CLI:

```bash
gh secret set DATABASE_PASSWORD --body "password123"
gh secret set API_KEY --body "sk_live_..."
```

Use in workflow:

```yaml
steps:
  - run: npm test
    env:
      DATABASE_PASSWORD: ${{ secrets.DATABASE_PASSWORD }}
      API_KEY: ${{ secrets.API_KEY }}
```

### 3. AWS Secrets Manager

```bash
# Create secret
aws secretsmanager create-secret \
  --name MyAppDatabase \
  --secret-string '{"username":"admin","password":"secret"}'

# Retrieve secret
aws secretsmanager get-secret-value \
  --secret-id MyAppDatabase
```

### 4. HashiCorp Vault

```bash
# Login
vault login -method=github

# Store secret
vault kv put secret/myapp/database \
  username="admin" \
  password="secret"

# Retrieve secret
vault kv get secret/myapp/database
```

### 5. .gitignore Secrets

```
# .gitignore
.env
.env.local
.env.*.local
secrets/
*.key
*.pem
credentials.json
```

---

## How It Works

### 1. Environment Variables

**Multiple Environment Files:**

```
.env              (committed, default values)
.env.local        (not committed, local overrides)
.env.development  (committed, dev defaults)
.env.production   (not committed, prod values)
```

**Load Strategy:**

```javascript
// Node.js
require('dotenv').config({
  path: [
    '.env',
    `.env.${process.env.NODE_ENV || 'development'}`,
    `.env.${process.env.NODE_ENV || 'development'}.local`,
    '.env.local'
  ]
});
```

**Variable Expansion:**

```bash
# .env
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_URL=postgresql://${DATABASE_HOST}:${DATABASE_PORT}/myapp
```

### 2. GitHub Secrets

**Repository Secrets:**

```bash
# Set
gh secret set SECRET_NAME --body "value"

# List
gh secret list

# Delete
gh secret delete SECRET_NAME
```

**Organization Secrets:**

```bash
# Available to multiple repositories
gh secret set SECRET_NAME --org my-org --body "value"
```

**Environment Secrets:**

```yaml
jobs:
  deploy:
    environment: production
    steps:
      - run: deploy.sh
        env:
          # Only available in production environment
          PROD_API_KEY: ${{ secrets.PROD_API_KEY }}
```

**Use in Workflows:**

```yaml
env:
  # Repository secret
  LOG_LEVEL: ${{ secrets.LOG_LEVEL }}

jobs:
  build:
    steps:
      - run: npm test
        env:
          # Job-level secret
          DB_PASSWORD: ${{ secrets.DB_PASSWORD }}
```

### 3. AWS Secrets Manager

**Store Secrets:**

```bash
# Simple secret
aws secretsmanager create-secret \
  --name api-key \
  --secret-string "sk_live_123456789"

# JSON secret
aws secretsmanager create-secret \
  --name database/prod \
  --secret-string '{
    "username": "admin",
    "password": "secure_password",
    "host": "prod.example.com"
  }'
```

**Retrieve Secrets:**

```bash
# Get entire secret
aws secretsmanager get-secret-value \
  --secret-id api-key \
  --query SecretString \
  --output text

# Get JSON field
aws secretsmanager get-secret-value \
  --secret-id database/prod \
  --query SecretString \
  --output text | jq '.password'
```

**Rotate Secrets:**

```bash
# Enable rotation
aws secretsmanager rotate-secret \
  --secret-id api-key \
  --rotation-rules AutomaticallyAfterDays=30
```

**Application Integration:**

```python
import boto3
import json

client = boto3.client('secretsmanager')

def get_secret(secret_id):
  response = client.get_secret_value(SecretId=secret_id)
  if 'SecretString' in response:
    return json.loads(response['SecretString'])

db_secret = get_secret('database/prod')
username = db_secret['username']
password = db_secret['password']
```

### 4. HashiCorp Vault

**Setup and Login:**

```bash
# Start dev server
vault server -dev

# Login
vault login -method=github
# Or with token
vault login <token>
```

**Store Secrets:**

```bash
# Key-value store
vault kv put secret/myapp/database \
  username="admin" \
  password="secure_password"

# JSON
vault kv put secret/myapp/config \
  config=@config.json
```

**Retrieve Secrets:**

```bash
# Get all
vault kv get secret/myapp/database

# Specific field
vault kv get -field=password secret/myapp/database
```

**Dynamic Secrets (auto-rotating):**

```bash
# Database credentials
vault write database/config/myapp \
  plugin_name=postgresql-database-plugin \
  allowed_roles="readonly" \
  connection_url="postgresql://{{username}}:{{password}}@localhost/postgres"

# Request temporary credentials
vault read database/creds/readonly
# Returns temporary username/password that expire automatically
```

**Application Integration:**

```python
import hvac

client = hvac.Client(url='http://127.0.0.1:8200', token='mytoken')

# Read secret
response = client.secrets.kv.read_secret_version(
  path='myapp/database'
)
username = response['data']['data']['username']
password = response['data']['data']['password']

# Read dynamic credentials
response = client.secrets.databases.read_dynamic_credentials(
  name='readonly',
  db_name='myapp'
)
temp_user = response['data']['username']
temp_pass = response['data']['password']
```

### 5. Secret Rotation

**Automatic Rotation:**

```bash
# AWS Secrets Manager
aws secretsmanager rotate-secret \
  --secret-id my-secret \
  --rotation-rules AutomaticallyAfterDays=30

# Vault
vault write -f /auth/kubernetes/config/rotate
```

**Manual Rotation Script:**

```bash
#!/bin/bash

# Generate new secret
NEW_SECRET=$(openssl rand -base64 32)

# Store new version
aws secretsmanager put-secret-value \
  --secret-id my-api-key \
  --secret-string "$NEW_SECRET"

# Update in application
# Application automatically picks up new version
# No downtime for properly configured apps

echo "Secret rotated: $NEW_SECRET"
```

### 6. Secret Scanning Prevention

**Pre-commit Hook:**

```bash
#!/bin/bash
# .git/hooks/pre-commit

# Check for common patterns
if grep -r "password\|secret\|api.key" . --exclude-dir=.git; then
  echo "Possible secrets detected!"
  exit 1
fi
```

**Automated Scanning:**

```yaml
# GitHub Secret Scanning
# Settings → Security → Secret scanning → Enable

# Trivy
trivy fs . --security-checks secret

# gitLeaks
gitleaks detect --source=local --verbose
```

**If Secret Leaked:**

```bash
# Immediately rotate the secret
aws secretsmanager rotate-secret --secret-id my-secret

# Remove from git history
git filter-branch --tree-filter 'git rm -f secrets.env' HEAD

# Force push (after review)
git push origin --force-with-lease
```

---

## Configuration

### Environment Variable Setup

`.env` (committed with defaults):

```bash
# Application
APP_ENV=development
APP_DEBUG=true
LOG_LEVEL=debug

# Database (default/development)
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=myapp_dev
DATABASE_USER=postgres
DATABASE_PASSWORD=  # Empty, set in .env.local

# External Services
STRIPE_API_KEY=  # Empty, set in .env.local
SENDGRID_API_KEY=  # Empty, set in .env.local
```

`.env.local` (never committed):

```bash
DATABASE_PASSWORD=secret_password
STRIPE_API_KEY=sk_live_123456789
SENDGRID_API_KEY=SG.xxx
```

`.env.production` (committed):

```bash
APP_ENV=production
APP_DEBUG=false
LOG_LEVEL=error
DATABASE_HOST=prod.db.example.com
DATABASE_PORT=5432
DATABASE_NAME=myapp_prod
```

### AWS Secrets Manager Setup

```bash
#!/bin/bash

# Create database secret
aws secretsmanager create-secret \
  --name prod/database \
  --description "Production database credentials" \
  --secret-string '{
    "host": "prod-db.example.com",
    "port": 5432,
    "username": "dbadmin",
    "password": "'$(openssl rand -base64 32)'",
    "dbname": "myapp_prod"
  }'

# Create API keys secret
aws secretsmanager create-secret \
  --name prod/api-keys \
  --secret-string '{
    "stripe": "sk_live_xxx",
    "sendgrid": "SG.xxx",
    "aws_access_key": "AKIAIOSFODNN7EXAMPLE",
    "aws_secret_key": "'$(openssl rand -base64 32)'"
  }'

# Enable automatic rotation
aws secretsmanager rotate-secret \
  --secret-id prod/api-keys \
  --rotation-rules AutomaticallyAfterDays=30
```

---

## Examples

### Example 1: Application Loading Secrets

```python
# app.py
import os
from dotenv import load_dotenv
import boto3

# Load local .env files
load_dotenv()

def get_database_url():
  # Try environment variable first
  url = os.getenv('DATABASE_URL')
  if url:
    return url

  # Try AWS Secrets Manager
  try:
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(SecretId='prod/database')
    secret = json.loads(response['SecretString'])
    return f"postgresql://{secret['username']}:{secret['password']}@{secret['host']}/{secret['dbname']}"
  except:
    pass

  # Fallback to individual variables
  return f"postgresql://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}/{ os.getenv('DATABASE_NAME')}"

database_url = get_database_url()
```

### Example 2: GitHub Actions with Secrets

```yaml
name: Deploy

on:
  push:
    branches: [main]

env:
  # Use repository secrets
  REGISTRY: ${{ secrets.REGISTRY }}

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: actions/checkout@v4

      - name: Deploy
        env:
          # Multiple secrets
          DATABASE_URL: ${{ secrets.DATABASE_URL }}
          API_KEY: ${{ secrets.API_KEY }}
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        run: |
          ./deploy.sh

      - name: Notify
        if: failure()
        env:
          SLACK_WEBHOOK: ${{ secrets.SLACK_WEBHOOK }}
        run: |
          curl -X POST $SLACK_WEBHOOK \
            -d '{"text":"Deploy failed"}'
```

### Example 3: Vault Integration

```python
import hvac
import os

# Connect to Vault
client = hvac.Client(
  url=os.getenv('VAULT_ADDR', 'http://127.0.0.1:8200'),
  token=os.getenv('VAULT_TOKEN')
)

# Read static secret
db_secret = client.secrets.kv.read_secret_version(
  path='myapp/database'
)
db_config = db_secret['data']['data']

# Read dynamic credentials (auto-rotating)
db_creds = client.secrets.databases.read_dynamic_credentials(
  name='readonly',
  db_name='myapp'
)
temp_user = db_creds['data']['username']
temp_pass = db_creds['data']['password']

print(f"Username: {temp_user}")
print(f"Password: {temp_pass}")
print(f"TTL: {db_creds['lease_duration']}")
```

### Example 4: Secret Rotation Script

```bash
#!/bin/bash
# scripts/rotate-secrets.sh

set -e

ENVIRONMENT=$1

if [ -z "$ENVIRONMENT" ]; then
  echo "Usage: ./rotate-secrets.sh <dev|staging|prod>"
  exit 1
fi

echo "Rotating secrets for $ENVIRONMENT..."

# Generate new API key
NEW_API_KEY=$(openssl rand -base64 32 | head -c 32)

# Store in AWS Secrets Manager
aws secretsmanager put-secret-value \
  --secret-id "$ENVIRONMENT/api-key" \
  --secret-string "$NEW_API_KEY"

# Store in Vault
vault kv put "secret/$ENVIRONMENT/api-key" \
  value="$NEW_API_KEY"

# Update GitHub
gh secret set "$(echo $ENVIRONMENT | tr '[:lower:]' '[:upper:]')_API_KEY" \
  --body "$NEW_API_KEY"

echo "Secrets rotated successfully"
```

### Example 5: Prevent Secret Leaks

`.gitignore`:

```
# Environment files
.env
.env.*.local
.env.local

# Configuration
config/secrets.json
config/database.yml
secrets/

# Keys and certificates
*.key
*.pem
*.p12
*.pfx

# Build artifacts with secrets
dist/
build/
node_modules/
```

`pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/Yelp/detect-secrets
    rev: v1.4.0
    hooks:
      - id: detect-secrets
        args: ['--baseline', '.secrets.baseline']

  - repo: https://github.com/zricethezav/gitleaks
    rev: v8.18.0
    hooks:
      - id: gitleaks
```

---

## Best Practices

### 1. Never Commit Secrets

```bash
# Good: .gitignore
.env.local
secrets/

# Bad: Committed to git (REMOVE IMMEDIATELY!)
DATABASE_PASSWORD=secret123
```

### 2. Use Unique Secrets Per Environment

```bash
# Good: Different secrets for each environment
SECRET_NAME=prod/api-key     # Production
SECRET_NAME=staging/api-key  # Staging
SECRET_NAME=dev/api-key      # Development

# Bad: Same secret everywhere
SECRET_NAME=api-key
```

### 3. Rotate Regularly

```bash
# Every 90 days minimum
# Every 30 days recommended
# Immediately after exposure
```

### 4. Use Strong Secrets

```bash
# Good: 32+ character random
openssl rand -base64 32

# Bad: Simple password
mypassword123
```

### 5. Audit Secret Access

```bash
# Enable CloudTrail for AWS Secrets Manager
# Enable audit logging in Vault
# Review GitHub secret usage logs
```

---

## Integration with Other Skills

Secrets Management integrates with:

- **github-actions-workflows** - Use secrets in CI/CD
- **ssh-key-management** - Secure key storage
- **kubernetes-yaml-generation** - K8s Secret resources
- **docker-compose-setup** - Environment variable passing
- **github-security-scanning** - Detect exposed secrets

---

## Complete Command Reference

```bash
# GitHub Secrets
gh secret set <name> --body <value>
gh secret list
gh secret delete <name>

# AWS Secrets Manager
aws secretsmanager create-secret --name <name> --secret-string <value>
aws secretsmanager get-secret-value --secret-id <id>
aws secretsmanager put-secret-value --secret-id <id> --secret-string <value>
aws secretsmanager rotate-secret --secret-id <id>

# Vault
vault kv put secret/path key1=value1 key2=value2
vault kv get secret/path
vault kv get -field=key1 secret/path
vault write -f /auth/token/renew-self
```

---

*Last Updated: 2026-02-02*
*Part of: AI Agents & Skills Repository*
