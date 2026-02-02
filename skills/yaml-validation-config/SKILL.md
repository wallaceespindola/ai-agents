# YAML Validation & Config Skill

**Master YAML syntax, schema validation, linting, and configuration management patterns for robust config files.**

## Overview

YAML is the standard configuration format for modern applications. This skill covers syntax, validation, schema enforcement, and best practices.

**What it does:**
- Validates YAML syntax and structure
- Enforces schema constraints
- Implements configuration linting
- Manages secrets in config files
- Validates Kubernetes manifests
- Generates config documentation
- Implements config inheritance patterns
- Prevents configuration errors

**Perfect for:**
- Application configuration
- Docker/Kubernetes manifests
- CI/CD pipeline configuration
- Infrastructure-as-code
- Configuration consistency

---

## When to Use This Skill

Use YAML Validation when you need to:

- **Validate config files** before deployment
- **Enforce schema** across team
- **Detect invalid YAML** early
- **Generate documentation** from config
- **Manage secrets** securely
- **Prevent deployment errors** caused by config
- **Lint configuration files** in CI/CD
- **Validate manifest syntax**

---

## Quick Start (10 Minutes)

### 1. Install YAML Validators

```bash
# Node.js
npm install --save-dev yaml-validator yamllint ajv

# Python
pip install pyyaml yamllint

# Or standalone
brew install yamllint  # macOS
apt-get install yamllint  # Linux
```

### 2. Create .yamllint Config

Create `.yamllint`:

```yaml
---
extends: default
rules:
  line-length:
    max: 120
    level: warning
  indentation:
    spaces: 2
  brackets:
    forbid: non-empty
  colons:
    max-spaces-after: 1
```

### 3. Validate YAML File

```bash
# Single file
yamllint config.yml

# Directory
yamllint -d relaxed .

# Output: Shows issues and line numbers
```

### 4. Create JSON Schema

Create `config.schema.json`:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "server": {
      "type": "object",
      "properties": {
        "port": {"type": "integer", "minimum": 1024},
        "host": {"type": "string"},
        "ssl": {"type": "boolean"}
      },
      "required": ["port", "host"]
    }
  }
}
```

### 5. Validate Against Schema

```bash
npm install --save-dev ajv-cli

ajv validate -s config.schema.json -d config.yml
```

---

## How It Works

### 1. YAML Syntax Essentials

**Basic Data Types:**

```yaml
# String
name: "John Doe"

# Integer
age: 30

# Float
height: 5.9

# Boolean
active: true
enabled: false

# Null
value: null

# Date
created: 2026-02-02

# List
colors:
  - red
  - green
  - blue

# Dictionary
user:
  name: John
  email: john@example.com

# Nested structures
teams:
  - name: Backend
    members:
      - alice
      - bob
  - name: Frontend
    members:
      - carol
```

**Multi-line Strings:**

```yaml
# Literal block (preserves newlines)
description: |
  This is a multi-line
  description that preserves
  line breaks.

# Folded block (folds newlines to spaces)
summary: >
  This is a long summary that
  will be folded into a single
  line with spaces.

# Quoted string
path: "C:\\Users\\john\\Documents"
```

**Anchors and Aliases:**

```yaml
# Define reusable content
defaults: &defaults
  timeout: 30
  retries: 3
  log_level: info

# Reuse content
api:
  <<: *defaults
  port: 8080

webhook:
  <<: *defaults
  port: 9090
  timeout: 60  # Override
```

### 2. Schema Validation

**JSON Schema for YAML:**

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Application Configuration",
  "type": "object",
  "properties": {
    "server": {
      "type": "object",
      "properties": {
        "port": {
          "type": "integer",
          "minimum": 1024,
          "maximum": 65535
        },
        "host": {
          "type": "string",
          "format": "hostname"
        },
        "ssl": {
          "type": "boolean"
        }
      },
      "required": ["port", "host"]
    },
    "database": {
      "type": "object",
      "properties": {
        "url": {
          "type": "string",
          "format": "uri"
        },
        "pool": {
          "type": "integer",
          "minimum": 1,
          "maximum": 100
        }
      },
      "required": ["url"]
    },
    "logging": {
      "type": "object",
      "properties": {
        "level": {
          "type": "string",
          "enum": ["debug", "info", "warn", "error"]
        },
        "format": {
          "type": "string",
          "enum": ["json", "text"]
        }
      }
    }
  },
  "required": ["server", "database"]
}
```

**Validation Constraints:**

```json
{
  "type": "object",
  "properties": {
    "email": {
      "type": "string",
      "format": "email"
    },
    "age": {
      "type": "integer",
      "minimum": 0,
      "maximum": 150
    },
    "status": {
      "type": "string",
      "enum": ["active", "inactive", "pending"]
    },
    "tags": {
      "type": "array",
      "items": {"type": "string"},
      "minItems": 1,
      "maxItems": 10
    },
    "metadata": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "created": {"type": "string"},
        "updated": {"type": "string"}
      }
    }
  }
}
```

### 3. YAML Linting Rules

**yamllint Configuration:**

```yaml
---
extends: default
rules:
  # Indentation
  indentation:
    spaces: 2
    indent-sequences: true
    check-multi-line-strings: false

  # Line length
  line-length:
    max: 120
    level: warning

  # Trailing spaces
  trailing-spaces: enable

  # Brackets
  brackets:
    min-spaces-inside: 0
    max-spaces-inside: 0
    forbid: non-empty

  # Braces
  braces:
    min-spaces-inside: 0
    max-spaces-inside: 0
    forbid: non-empty

  # Colons
  colons:
    max-spaces-after: 1

  # Commas
  commas:
    max-spaces-after: 1

  # Comments
  comments:
    min-spaces-from-content: 2

  # Document start
  document-start:
    present: true  # Require ---
```

### 4. Configuration Patterns

**Environment-Specific Configs:**

```yaml
# config.base.yml - shared config
server:
  host: localhost
  timeout: 30
database:
  pool: 10
logging:
  level: info
```

```yaml
# config.dev.yml - development overrides
server:
  port: 3000
database:
  url: postgresql://localhost/myapp_dev
logging:
  level: debug
```

```yaml
# config.prod.yml - production config
server:
  port: 8080
database:
  url: postgresql://prod-server/myapp
  pool: 50
  ssl: true
logging:
  level: error
```

**Load with Defaults:**

```javascript
const yaml = require('js-yaml');
const fs = require('fs');
const deepMerge = require('deep-merge');

function loadConfig(env = 'dev') {
  const base = yaml.load(fs.readFileSync('config.base.yml'));
  const env_config = yaml.load(fs.readFileSync(`config.${env}.yml`));
  return deepMerge(base, env_config);
}

const config = loadConfig('prod');
```

### 5. Secrets Management

**Do NOT Store Secrets in Config:**

```yaml
# BAD - Hardcoded secrets
database:
  password: "super_secret_password"
  api_key: "sk_live_123456789"
```

**Use Environment Variables:**

```yaml
# GOOD - Reference environment variables
database:
  url: ${DATABASE_URL}
  password: ${DATABASE_PASSWORD}

api:
  key: ${API_KEY}
  secret: ${API_SECRET}
```

**Load Variables:**

```javascript
const yaml = require('js-yaml');
const fs = require('fs');

// Custom constructor for env vars
const envConstructor = (data) => {
  if (data.startsWith('${') && data.endsWith('}')) {
    const key = data.slice(2, -1);
    return process.env[key] || '';
  }
  return data;
};

const schema = yaml.DEFAULT_SCHEMA.extend([
  new yaml.Type('!env', {
    kind: 'scalar',
    construct: envConstructor
  })
]);

const config = yaml.load(fs.readFileSync('config.yml'), { schema });
```

### 6. YAML Validation in CI/CD

**GitHub Actions Workflow:**

```yaml
name: Validate Config

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Validate YAML syntax
        run: |
          find . -name "*.yml" -o -name "*.yaml" | \
          xargs -I {} yamllint {}

      - name: Validate against schema
        run: |
          npm install -g ajv-cli
          ajv validate -s config.schema.json -d config.yml
```

**Pre-commit Hook:**

```bash
#!/bin/bash
# .git/hooks/pre-commit

yamllint $(git diff --cached --name-only --diff-filter=ACM | grep -E '\.(yml|yaml)$')
exit $?
```

### 7. Configuration Documentation

**Generate Docs from Schema:**

```bash
# Using json-schema-to-markdown
npm install -g json-schema-to-markdown

json-schema-to-markdown config.schema.json > CONFIG.md
```

**Example Generated Doc:**

```markdown
# Configuration Schema

## Properties

### server (required)
- **type**: object
- **properties**:
  - **port** (required): integer, minimum 1024, maximum 65535
  - **host** (required): string, format hostname
  - **ssl**: boolean, default false

### database (required)
- **type**: object
- **properties**:
  - **url** (required): string, format URI
  - **pool**: integer, minimum 1, maximum 100, default 10
```

---

## Configuration

### Complete YAML Linting Setup

`.yamllint`:

```yaml
---
extends: default
rules:
  # Indentation
  indentation:
    spaces: 2
    indent-sequences: true
    check-multi-line-strings: false

  # Line length
  line-length:
    max: 120
    level: warning

  # Document
  document-start:
    present: true
  document-end:
    present: false

  # Keys
  key-duplicates: enable
  key-ordering: disable

  # Comments
  comments:
    min-spaces-from-content: 2
    require-starting-space: true
    allow-block: false

  # Spacing
  brackets:
    min-spaces-inside: 0
    max-spaces-inside: 0
    forbid: non-empty

  braces:
    min-spaces-inside: 0
    max-spaces-inside: 0
    forbid: non-empty

  colons:
    max-spaces-before: 0
    max-spaces-after: 1

  commas:
    max-spaces-before: 0
    max-spaces-after: 1

  # Content
  trailing-spaces: enable
  truthy: enable
  empty-lines:
    max: 2
  empty-values: disable
```

### Complete JSON Schema

`config.schema.json`:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Application Configuration",
  "description": "Configuration schema for the application",
  "type": "object",
  "additionalProperties": false,
  "required": ["server", "database"],
  "properties": {
    "server": {
      "type": "object",
      "required": ["port", "host"],
      "additionalProperties": false,
      "properties": {
        "host": {
          "type": "string",
          "description": "Server hostname",
          "format": "hostname"
        },
        "port": {
          "type": "integer",
          "description": "Server port",
          "minimum": 1024,
          "maximum": 65535
        },
        "ssl": {
          "type": "boolean",
          "description": "Enable SSL",
          "default": false
        },
        "timeout": {
          "type": "integer",
          "description": "Request timeout in seconds",
          "minimum": 1
        }
      }
    },
    "database": {
      "type": "object",
      "required": ["url"],
      "additionalProperties": false,
      "properties": {
        "url": {
          "type": "string",
          "description": "Database connection URL",
          "format": "uri"
        },
        "pool": {
          "type": "integer",
          "description": "Connection pool size",
          "minimum": 1,
          "maximum": 100,
          "default": 10
        },
        "ssl": {
          "type": "boolean",
          "description": "Use SSL for database connection"
        }
      }
    },
    "logging": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "level": {
          "type": "string",
          "enum": ["debug", "info", "warn", "error"],
          "default": "info"
        },
        "format": {
          "type": "string",
          "enum": ["json", "text"],
          "default": "text"
        }
      }
    }
  }
}
```

---

## Examples

### Example 1: Application Configuration

`config.yml`:

```yaml
---
# Application Configuration

server:
  host: 0.0.0.0
  port: 8080
  ssl: false
  timeout: 30
  cors:
    enabled: true
    origins:
      - http://localhost:3000
      - https://example.com

database:
  url: ${DATABASE_URL}
  pool: 20
  ssl: true
  max_idle_connections: 10

authentication:
  jwt:
    secret: ${JWT_SECRET}
    expiry: 86400  # 24 hours
  oauth:
    enabled: true
    providers:
      - github
      - google

logging:
  level: info
  format: json
  output:
    stdout: true
    file:
      enabled: true
      path: /var/log/app.log
      rotation:
        max_size_mb: 100
        max_age_days: 30

cache:
  enabled: true
  redis_url: ${REDIS_URL}
  ttl: 3600
```

### Example 2: Kubernetes Manifest

`deployment.yaml`:

```yaml
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-server
  labels:
    app: api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: api
  template:
    metadata:
      labels:
        app: api
    spec:
      containers:
      - name: api
        image: myregistry/api:1.0.0
        ports:
        - containerPort: 8080
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: app-secrets
              key: database-url
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 10
```

### Example 3: Config Validation Script

`scripts/validate-config.js`:

```javascript
#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');
const Ajv = require('ajv');

const configFile = process.argv[2] || 'config.yml';
const schemaFile = 'config.schema.json';

// Load config
const config = yaml.load(fs.readFileSync(configFile, 'utf8'));

// Load schema
const schema = JSON.parse(fs.readFileSync(schemaFile, 'utf8'));

// Validate
const ajv = new Ajv();
const validate = ajv.compile(schema);
const valid = validate(config);

if (valid) {
  console.log('✓ Configuration is valid');
  process.exit(0);
} else {
  console.error('✗ Configuration validation failed:');
  console.error(JSON.stringify(validate.errors, null, 2));
  process.exit(1);
}
```

### Example 4: Environment-Specific Loading

`src/config.js`:

```javascript
const yaml = require('js-yaml');
const fs = require('fs');
const deepMerge = require('lodash/merge');

class Config {
  constructor(env = process.env.NODE_ENV || 'development') {
    this.env = env;
    this.config = this.loadConfig();
  }

  loadConfig() {
    // Load base config
    const base = yaml.load(
      fs.readFileSync('config/base.yml', 'utf8')
    );

    // Load environment-specific config
    const envFile = `config/${this.env}.yml`;
    if (!fs.existsSync(envFile)) {
      throw new Error(`Config file not found: ${envFile}`);
    }

    const envConfig = yaml.load(fs.readFileSync(envFile, 'utf8'));

    // Merge with env vars
    return this.replaceEnvVars(deepMerge(base, envConfig));
  }

  replaceEnvVars(obj) {
    if (typeof obj === 'string') {
      // Replace ${VAR} with environment variable
      return obj.replace(/\$\{([^}]+)\}/g, (match, varName) => {
        const value = process.env[varName];
        if (!value) {
          throw new Error(`Environment variable not found: ${varName}`);
        }
        return value;
      });
    }

    if (Array.isArray(obj)) {
      return obj.map(item => this.replaceEnvVars(item));
    }

    if (obj !== null && typeof obj === 'object') {
      const result = {};
      for (const [key, value] of Object.entries(obj)) {
        result[key] = this.replaceEnvVars(value);
      }
      return result;
    }

    return obj;
  }

  get(key) {
    return key.split('.').reduce((obj, k) => obj?.[k], this.config);
  }
}

module.exports = new Config();
```

### Example 5: Config Diff Tool

`scripts/config-diff.sh`:

```bash
#!/bin/bash

# Compare configuration between environments

ENV1=${1:-dev}
ENV2=${2:-prod}

FILE1="config/config.${ENV1}.yml"
FILE2="config/config.${ENV2}.yml"

if [ ! -f "$FILE1" ] || [ ! -f "$FILE2" ]; then
  echo "Error: Config files not found"
  exit 1
fi

echo "=== Configuration Differences: $ENV1 vs $ENV2 ==="
echo ""

# Convert YAML to JSON for comparison
python3 -c "
import yaml
import json
import sys

with open('$FILE1') as f1, open('$FILE2') as f2:
    c1 = yaml.safe_load(f1)
    c2 = yaml.safe_load(f2)

    # Show differences
    from deepdiff import DeepDiff
    diff = DeepDiff(c1, c2, ignore_order=False)
    print(json.dumps(diff, indent=2))
"
```

---

## Best Practices

### 1. Always Use Document Start

```yaml
# Good: Clear document start
---
server:
  port: 8080
```

### 2. Consistent Indentation

```yaml
# Good: 2-space indentation
server:
  host: localhost
  port: 8080

# Bad: Inconsistent indentation
server:
    host: localhost
  port: 8080
```

### 3. Use Anchors for Reuse

```yaml
# Good: DRY principle
defaults: &defaults
  timeout: 30
  retries: 3

api:
  <<: *defaults

webhook:
  <<: *defaults
  timeout: 60
```

### 4. Never Hardcode Secrets

```yaml
# Good: Use environment variables
database:
  password: ${DATABASE_PASSWORD}

# Bad: Hardcoded secrets
database:
  password: "super_secret"
```

### 5. Comment Complex Sections

```yaml
# Good: Clear comments
# Cache configuration
# TTL in seconds, Redis connection
cache:
  enabled: true
  ttl: 3600  # 1 hour
  url: ${REDIS_URL}
```

---

## Integration with Other Skills

YAML Validation integrates with:

- **kubernetes-yaml-generation** - Validate K8s manifests
- **docker-compose-setup** - Validate compose files
- **github-actions-workflows** - Validate workflow YAML
- **build-optimization** - Validate config
- **secrets-management** - Secure config storage

---

## Complete Command Reference

```bash
# Validation
yamllint config.yml
yamllint -d relaxed .

# Schema validation
ajv validate -s config.schema.json -d config.yml

# Convert formats
yq eval config.yml  # Pretty print
yq eval '.server' config.yml  # Extract section

# Comparison
diff <(yq eval config.dev.yml) <(yq eval config.prod.yml)
```

---

*Last Updated: 2026-02-02*
*Part of: AI Agents & Skills Repository*
