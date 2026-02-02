# Helm Charts Creation Skill

**Master Helm chart structure, templating, values management, dependencies, repositories, and production deployments.**

## Overview

Helm is the package manager for Kubernetes. This skill covers creating, templating, and managing Helm charts for reproducible deployments.

**What it does:**
- Structures Helm charts correctly
- Implements Helm templating with variables
- Manages values files for different environments
- Handles chart dependencies
- Publishes to Helm repositories
- Implements hooks and jobs
- Manages upgrades and rollbacks
- Documents chart parameters

**Perfect for:**
- Kubernetes package management
- Multi-environment deployments
- Chart sharing and reuse
- Infrastructure-as-code
- Release management

---

## When to Use This Skill

Use Helm Charts when you need to:

- **Package Kubernetes applications** for distribution
- **Manage environment-specific configs** easily
- **Share applications** with teams
- **Install applications** with single command
- **Manage chart dependencies** (databases, message queues)
- **Implement upgrade strategies** safely
- **Rollback deployments** on failure
- **Publish to Helm repositories**

---

## Quick Start (10 Minutes)

### 1. Create Chart

```bash
helm create my-app
# Creates chart directory with templates

cd my-app
# Structure:
# ├── Chart.yaml
# ├── values.yaml
# ├── templates/
# │   ├── deployment.yaml
# │   ├── service.yaml
# │   └── ingress.yaml
# └── charts/
```

### 2. Define Values

Edit `values.yaml`:

```yaml
replicaCount: 3
image:
  repository: myapp
  tag: "1.0.0"
service:
  type: ClusterIP
  port: 80
```

### 3. Template Deployment

Edit `templates/deployment.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "my-app.fullname" . }}
spec:
  replicas: {{ .Values.replicaCount }}
  template:
    spec:
      containers:
      - name: {{ .Chart.Name }}
        image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
```

### 4. Install Chart

```bash
helm install my-release ./my-app
# Deploys with values from values.yaml
```

### 5. Override Values

```bash
helm install my-release ./my-app \
  --set replicaCount=5 \
  --set image.tag=2.0.0
```

---

## How It Works

### 1. Chart Structure

**Complete Chart Layout:**

```
my-app/
├── Chart.yaml                 # Chart metadata
├── values.yaml                # Default values
├── values.dev.yaml            # Dev overrides
├── values.prod.yaml           # Prod overrides
├── charts/                     # Dependent charts
│   └── postgresql/
│       ├── Chart.yaml
│       └── values.yaml
├── templates/                  # Kubernetes manifests
│   ├── NOTES.txt              # Post-install notes
│   ├── _helpers.tpl           # Template helpers
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── configmap.yaml
│   ├── secret.yaml
│   ├── hpa.yaml
│   ├── pdb.yaml
│   └── tests/
│       └── test-connection.yaml
├── .helmignore                # Ignore patterns
└── README.md
```

**Chart.yaml:**

```yaml
apiVersion: v2
name: my-app
description: My application Helm chart
type: application
version: 1.0.0
appVersion: "1.0.0"
keywords:
  - app
  - production
home: https://github.com/owner/my-app
sources:
  - https://github.com/owner/my-app
maintainers:
  - name: Wallace Espindola
    email: wallace@example.com
dependencies:
  - name: postgresql
    version: "13.0.0"
    repository: "https://charts.bitnami.com/bitnami"
    condition: postgresql.enabled
```

### 2. Templating

**Built-in Functions:**

```yaml
# Values interpolation
{{ .Values.replicaCount }}

# Chart metadata
{{ .Chart.Name }}
{{ .Chart.Version }}

# Release info
{{ .Release.Name }}
{{ .Release.Namespace }}

# Template functions
{{ include "my-app.fullname" . }}
{{ .Values.image.repository | quote }}

# Conditionals
{{ if .Values.ingress.enabled }}
apiVersion: networking.k8s.io/v1
kind: Ingress
{{ end }}

# Loops
{{ range .Values.env }}
- name: {{ .name }}
  value: {{ .value }}
{{ end }}

# String operations
{{ upper .Values.appName }}
{{ lower .Values.environment }}
{{ .Values.name | nospace }}
```

**Helper Template (_helpers.tpl):**

```yaml
{{/*
Expand the name of the chart.
*/}}
{{- define "my-app.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
*/}}
{{- define "my-app.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Create chart name and version
*/}}
{{- define "my-app.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}
```

### 3. Values Management

**values.yaml (defaults):**

```yaml
replicaCount: 3

image:
  repository: myapp
  pullPolicy: IfNotPresent
  tag: "1.0.0"

service:
  type: ClusterIP
  port: 80
  targetPort: 8080

ingress:
  enabled: true
  className: nginx
  hosts:
    - host: my-app.example.com
      paths:
        - path: /
          pathType: Prefix

resources:
  limits:
    cpu: 500m
    memory: 512Mi
  requests:
    cpu: 250m
    memory: 256Mi

autoscaling:
  enabled: true
  minReplicas: 3
  maxReplicas: 10
  targetCPUUtilizationPercentage: 70
```

**values-dev.yaml (overrides):**

```yaml
replicaCount: 1

image:
  tag: "latest"

ingress:
  hosts:
    - host: my-app.dev.example.com
      paths:
        - path: /

resources:
  limits:
    cpu: 200m
    memory: 256Mi
  requests:
    cpu: 100m
    memory: 128Mi

autoscaling:
  enabled: false
```

**values-prod.yaml (overrides):**

```yaml
replicaCount: 5

image:
  tag: "1.0.0"  # Pinned version

ingress:
  hosts:
    - host: my-app.example.com
      paths:
        - path: /

resources:
  limits:
    cpu: 1000m
    memory: 1Gi
  requests:
    cpu: 500m
    memory: 512Mi

autoscaling:
  enabled: true
  minReplicas: 5
  maxReplicas: 20
  targetCPUUtilizationPercentage: 60
```

### 4. Dependencies

**Chart.yaml with Dependencies:**

```yaml
dependencies:
  - name: postgresql
    version: "13.0.0"
    repository: "https://charts.bitnami.com/bitnami"
    alias: database
    condition: postgresql.enabled
    tags:
      - backend
    import-values:
      - child: postgresqlUsername
        parent: postgresUser

  - name: redis
    version: "17.0.0"
    repository: "https://charts.bitnami.com/bitnami"
    condition: redis.enabled
```

**values.yaml with Dependencies:**

```yaml
postgresql:
  enabled: true
  auth:
    username: myapp
    password: changeme
    database: myapp

redis:
  enabled: true
  auth:
    enabled: true
    password: changeme
```

**Update Dependencies:**

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm dependency update ./my-app
# Downloads to charts/ directory
```

### 5. Hooks

**Pre-install Hook (database migration):**

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: {{ include "my-app.fullname" . }}-db-migration
  annotations:
    "helm.sh/hook": pre-install
    "helm.sh/hook-weight": "-5"
spec:
  template:
    spec:
      containers:
      - name: migration
        image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
        command: ["python", "migrate.py"]
      restartPolicy: Never
```

**Post-install Hook (health check):**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: "{{ include "my-app.fullname" . }}-test"
  annotations:
    "helm.sh/hook": post-install
    "helm.sh/hook-weight": "5"
    "helm.sh/hook-delete-policy": before-hook-creation,hook-succeeded
spec:
  containers:
  - name: test
    image: curlimages/curl
    command:
      - sh
      - -c
      - curl {{ include "my-app.fullname" . }}/health
  restartPolicy: Never
```

### 6. Dry Run and Validation

```bash
# Preview without installing
helm install my-release ./my-app --dry-run --debug

# Lint for errors
helm lint ./my-app

# Check for deprecated APIs
helm lint ./my-app --strict

# Template output
helm template my-release ./my-app
```

### 7. Upgrades and Rollbacks

```bash
# Install
helm install my-release ./my-app --namespace prod --create-namespace

# Upgrade
helm upgrade my-release ./my-app --values values-prod.yaml

# Rollback
helm rollback my-release 1  # Rollback to revision 1

# View history
helm history my-release

# Uninstall
helm uninstall my-release
```

### 8. Publishing

**Create Repository:**

```bash
# Create package
helm package ./my-app
# Creates my-app-1.0.0.tgz

# Create index
helm repo index .

# Push to repository
# 1. Host on GitHub Pages, S3, or Helm registry
# 2. Users add repository:
helm repo add my-org https://charts.my-org.com
helm repo update
helm install my-release my-org/my-app
```

---

## Configuration

### Complete Production Chart

See examples section for full implementation.

---

## Examples

### Example 1: Full Application Chart

`Chart.yaml`:

```yaml
apiVersion: v2
name: my-app
version: 1.0.0
appVersion: "1.0.0"
description: Production application
type: application
```

`values.yaml`:

```yaml
replicaCount: 3

image:
  repository: myregistry/my-app
  tag: "1.0.0"
  pullPolicy: IfNotPresent

service:
  type: ClusterIP
  port: 80

ingress:
  enabled: true
  hosts:
    - host: my-app.example.com

resources:
  requests:
    cpu: 250m
    memory: 256Mi
  limits:
    cpu: 500m
    memory: 512Mi

autoscaling:
  enabled: true
  minReplicas: 3
  maxReplicas: 10
```

`templates/deployment.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "my-app.fullname" . }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app: {{ include "my-app.fullname" . }}
  template:
    metadata:
      labels:
        app: {{ include "my-app.fullname" . }}
    spec:
      containers:
      - name: {{ .Chart.Name }}
        image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
        ports:
        - containerPort: {{ .Values.service.port }}
        resources: {{- toYaml .Values.resources | nindent 12 }}
```

### Example 2: Chart with Database

`Chart.yaml`:

```yaml
dependencies:
  - name: postgresql
    version: "13.0.0"
    repository: https://charts.bitnami.com/bitnami
    condition: postgresql.enabled
```

`values.yaml`:

```yaml
postgresql:
  enabled: true
  auth:
    username: myapp
    password: changeme
    database: myapp

app:
  database:
    host: {{ .Release.Name }}-postgresql
    port: 5432
```

### Example 3: Multi-Environment

Install with environment-specific values:

```bash
# Development
helm install my-app ./my-app \
  --values values.yaml \
  --values values-dev.yaml \
  --namespace dev

# Production
helm install my-app ./my-app \
  --values values.yaml \
  --values values-prod.yaml \
  --namespace prod
```

### Example 4: Hooks

Pre-install migration job:

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  annotations:
    "helm.sh/hook": pre-install
spec:
  template:
    spec:
      containers:
      - name: migration
        image: myapp:1.0.0
        command: ["python", "migrate.py"]
```

### Example 5: Template Conditionals

```yaml
{{ if .Values.ingress.enabled }}
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: {{ include "my-app.fullname" . }}
spec:
  rules:
  {{ range .Values.ingress.hosts }}
  - host: {{ .host | quote }}
    http:
      paths:
      {{ range .paths }}
      - path: {{ .path }}
        pathType: {{ .pathType }}
        backend:
          service:
            name: {{ include "my-app.fullname" $ }}
            port:
              number: {{ $.Values.service.port }}
      {{ end }}
  {{ end }}
{{ end }}
```

---

## Best Practices

### 1. Semantic Versioning

```yaml
version: 1.0.0      # SemVer: MAJOR.MINOR.PATCH
appVersion: "1.0.0" # App version inside chart
```

### 2. Pin Dependency Versions

```yaml
dependencies:
  - name: postgresql
    version: "13.0.0"  # Exact version, not ~13.0.0
    repository: https://charts.bitnami.com/bitnami
```

### 3. Document Parameters

```yaml
# Create README.md
# Charts Parameters:
# - replicaCount: Number of replicas (default: 3)
# - image.tag: Application version (default: 1.0.0)
```

### 4. Validate Before Release

```bash
helm lint ./my-app --strict
helm template ./my-app | kubeval
```

### 5. Use Namespaces

```bash
helm install my-release ./my-app \
  --namespace my-app \
  --create-namespace
```

---

## Integration with Other Skills

Helm Charts integrates with:

- **kubernetes-yaml-generation** - Base Kubernetes manifests
- **docker-compose-setup** - Container definitions
- **yaml-validation-config** - Validate chart values
- **secrets-management** - Manage chart secrets

---

## Complete Command Reference

```bash
# Create and manage
helm create <name>
helm lint ./chart
helm package ./chart
helm repo index .

# Install and deploy
helm install <release> <chart>
helm upgrade <release> <chart>
helm rollback <release> [revision]
helm uninstall <release>

# View and manage
helm list
helm history <release>
helm get values <release>
helm get manifest <release>

# Repository
helm repo add <name> <url>
helm repo list
helm repo update
helm search repo <chart>
```

---

*Last Updated: 2026-02-02*
*Part of: AI Agents & Skills Repository*
