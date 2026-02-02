# Kubernetes YAML Generation Skill

**Master Kubernetes manifests: Deployments, Services, Ingress, ConfigMaps, Secrets, StatefulSets, Custom Resources, and best practices.**

## Overview

Kubernetes manifests define containerized applications. This skill covers manifest generation, resource types, and configuration patterns.

**What it does:**
- Generates Kubernetes Deployments
- Creates Services for network exposure
- Configures Ingress for routing
- Manages ConfigMaps and Secrets
- Deploys StatefulSets for stateful apps
- Handles Custom Resource Definitions (CRDs)
- Implements resource limits and requests
- Manages multi-container pods

**Perfect for:**
- Container orchestration
- Cloud-native applications
- Microservices deployment
- Scalable infrastructure
- GitOps workflows

---

## When to Use This Skill

Use Kubernetes YAML Generation when you need to:

- **Deploy containerized apps** to Kubernetes
- **Scale applications** dynamically
- **Manage configuration** and secrets
- **Route traffic** with Ingress
- **Monitor health** with probes
- **Manage storage** with PersistentVolumes
- **Implement StatefulSets** for databases
- **Define Custom Resources** for your platform

---

## Quick Start (10 Minutes)

### 1. Create Basic Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
  labels:
    app: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-app
        image: myregistry/my-app:1.0.0
        ports:
        - containerPort: 8080
```

### 2. Expose with Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-app-service
spec:
  selector:
    app: my-app
  type: ClusterIP
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
```

### 3. Configure with ConfigMap

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-app-config
data:
  LOG_LEVEL: "info"
  APP_ENV: "production"
```

### 4. Route with Ingress

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-app-ingress
spec:
  ingressClassName: nginx
  rules:
  - host: my-app.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: my-app-service
            port:
              number: 80
```

### 5. Apply to Cluster

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f configmap.yaml
kubectl apply -f ingress.yaml

# Verify
kubectl get deployments
kubectl get services
kubectl get ingress
```

---

## How It Works

### 1. Deployments

**Rolling Update Strategy:**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-server
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1        # 1 extra pod during update
      maxUnavailable: 0  # No pods down during update
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
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        env:
        - name: LOG_LEVEL
          value: "info"
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 10
          timeoutSeconds: 5
          failureThreshold: 3
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 5
```

**Deployment Strategies:**

```yaml
# Rolling update (default)
strategy:
  type: RollingUpdate

# Blue-green (new version alongside old)
strategy:
  type: Recreate

# Canary (progressive rollout)
# Requires traffic splitting (service mesh)
```

### 2. Services

**Service Types:**

```yaml
# ClusterIP (internal only)
kind: Service
spec:
  type: ClusterIP
  ports:
  - port: 80
    targetPort: 8080

# NodePort (external via node port)
kind: Service
spec:
  type: NodePort
  ports:
  - port: 80
    targetPort: 8080
    nodePort: 30000

# LoadBalancer (cloud provider)
kind: Service
spec:
  type: LoadBalancer
  ports:
  - port: 80
    targetPort: 8080

# ExternalName (external service)
kind: Service
spec:
  type: ExternalName
  externalName: example.com
```

**Headless Service (for StatefulSets):**

```yaml
apiVersion: v1
kind: Service
metadata:
  name: postgres-headless
spec:
  clusterIP: None  # Headless
  selector:
    app: postgres
  ports:
  - port: 5432
    targetPort: 5432
```

### 3. ConfigMaps and Secrets

**ConfigMap:**

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  LOG_LEVEL: "info"
  APP_ENV: "production"
  database_host: "postgres.default.svc.cluster.local"
  config.json: |
    {
      "features": ["feature1", "feature2"],
      "timeout": 30
    }
```

**Mount ConfigMap:**

```yaml
containers:
- name: app
  image: myapp:1.0.0
  env:
  - name: LOG_LEVEL
    valueFrom:
      configMapKeyRef:
        name: app-config
        key: LOG_LEVEL
  volumeMounts:
  - name: config
    mountPath: /etc/config
volumes:
- name: config
  configMap:
    name: app-config
```

**Secret (base64 encoded):**

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: app-secrets
type: Opaque
data:
  database_password: cGFzc3dvcmQxMjM=  # base64 encoded
  api_key: c2tyX2xpdmVfMTIzNDU2Nzg5MA==
```

**Mount Secret:**

```yaml
containers:
- name: app
  env:
  - name: DB_PASSWORD
    valueFrom:
      secretKeyRef:
        name: app-secrets
        key: database_password
```

### 4. Ingress

**Basic Ingress:**

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-ingress
  annotations:
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
    nginx.ingress.kubernetes.io/rate-limit: "100"
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - my-app.example.com
    secretName: my-app-tls
  rules:
  - host: my-app.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: app-service
            port:
              number: 80
      - path: /api
        pathType: Prefix
        backend:
          service:
            name: api-service
            port:
              number: 8080
```

**Advanced Routing:**

```yaml
rules:
- host: api.example.com
  http:
    paths:
    - path: /v1
      pathType: Prefix
      backend:
        service:
          name: api-v1
          port:
            number: 8080
    - path: /v2
      pathType: Prefix
      backend:
        service:
          name: api-v2
          port:
            number: 8080
```

### 5. StatefulSets

**Stateful Application (Database):**

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: postgres
spec:
  serviceName: postgres-headless
  replicas: 1
  selector:
    matchLabels:
      app: postgres
  template:
    metadata:
      labels:
        app: postgres
    spec:
      containers:
      - name: postgres
        image: postgres:15
        ports:
        - containerPort: 5432
          name: postgres
        env:
        - name: POSTGRES_PASSWORD
          valueFrom:
            secretKeyRef:
              name: postgres-secret
              key: password
        volumeMounts:
        - name: postgres-storage
          mountPath: /var/lib/postgresql/data
          subPath: postgres
        resources:
          requests:
            memory: "512Mi"
            cpu: "500m"
          limits:
            memory: "1Gi"
            cpu: "1000m"
  volumeClaimTemplates:
  - metadata:
      name: postgres-storage
    spec:
      accessModes: ["ReadWriteOnce"]
      resources:
        requests:
          storage: 20Gi
```

### 6. Health Probes

**Liveness Probe (restart if unhealthy):**

```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 8080
  initialDelaySeconds: 30
  periodSeconds: 10
  timeoutSeconds: 5
  failureThreshold: 3
```

**Readiness Probe (traffic only if ready):**

```yaml
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 10
  periodSeconds: 5
  timeoutSeconds: 3
  failureThreshold: 1
```

**Startup Probe (long startup time):**

```yaml
startupProbe:
  httpGet:
    path: /health
    port: 8080
  failureThreshold: 30
  periodSeconds: 10
  # Allows 5 minutes (30 * 10s) for app to start
```

### 7. Resource Management

**Resource Requests and Limits:**

```yaml
resources:
  requests:
    memory: "256Mi"  # Guaranteed allocation
    cpu: "250m"      # 250 millicores = 0.25 CPU
  limits:
    memory: "512Mi"  # Max memory
    cpu: "500m"      # Max CPU
```

**Quality of Service (QoS):**

```
Guaranteed: requests == limits (highest priority)
Burstable:  requests < limits (medium priority)
BestEffort: no requests/limits (lowest priority, evicted first)
```

### 8. Custom Resources (CRDs)

**Define CRD:**

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: databases.custom.io
spec:
  names:
    kind: Database
    plural: databases
  scope: Namespaced
  group: custom.io
  versions:
  - name: v1
    served: true
    storage: true
    schema:
      openAPIV3Schema:
        type: object
        properties:
          spec:
            type: object
            properties:
              engine:
                type: string
              version:
                type: string
              size:
                type: string
```

**Use CRD:**

```yaml
apiVersion: custom.io/v1
kind: Database
metadata:
  name: my-postgres
spec:
  engine: postgres
  version: "15"
  size: large
```

---

## Configuration

### Complete Production Deployment

```yaml
---
apiVersion: v1
kind: Namespace
metadata:
  name: production
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
  namespace: production
data:
  LOG_LEVEL: "info"
  APP_ENV: "production"
  DATABASE_HOST: "postgres.production.svc.cluster.local"
---
apiVersion: v1
kind: Secret
metadata:
  name: app-secrets
  namespace: production
type: Opaque
data:
  DB_PASSWORD: cGFzcw==
  API_KEY: YWJjMTIz
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app
  namespace: production
  labels:
    app: app
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: app
  template:
    metadata:
      labels:
        app: app
    spec:
      affinity:
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 100
            podAffinityTerm:
              labelSelector:
                matchExpressions:
                - key: app
                  operator: In
                  values:
                  - app
              topologyKey: kubernetes.io/hostname
      containers:
      - name: app
        image: myregistry/app:1.0.0
        imagePullPolicy: IfNotPresent
        ports:
        - containerPort: 8080
          name: http
        env:
        - name: LOG_LEVEL
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: LOG_LEVEL
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: app-secrets
              key: DB_PASSWORD
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
          initialDelaySeconds: 30
          periodSeconds: 10
          timeoutSeconds: 5
          failureThreshold: 3
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 5
          timeoutSeconds: 3
          failureThreshold: 1
        securityContext:
          runAsNonRoot: true
          runAsUser: 1000
          readOnlyRootFilesystem: true
          allowPrivilegeEscalation: false
          capabilities:
            drop:
            - ALL
---
apiVersion: v1
kind: Service
metadata:
  name: app
  namespace: production
spec:
  selector:
    app: app
  type: ClusterIP
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app
  namespace: production
  annotations:
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - app.example.com
    secretName: app-tls
  rules:
  - host: app.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: app
            port:
              number: 80
---
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: app-pdb
  namespace: production
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: app
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: app-hpa
  namespace: production
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: app
  minReplicas: 3
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
```

---

## Examples

### Example 1: Multi-Container Pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: web-app
spec:
  initContainers:
  - name: init
    image: busybox
    command: ['sh', '-c', 'echo "Initializing..."']

  containers:
  - name: app
    image: myapp:1.0.0
    ports:
    - containerPort: 8080
    volumeMounts:
    - name: shared
      mountPath: /tmp/shared

  - name: sidecar
    image: logging-sidecar:1.0.0
    volumeMounts:
    - name: shared
      mountPath: /tmp/shared

  volumes:
  - name: shared
    emptyDir: {}
```

### Example 2: Canary Deployment

```yaml
# 95% traffic to stable
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-stable
spec:
  replicas: 19
  selector:
    matchLabels:
      app: app
      version: stable
  template:
    metadata:
      labels:
        app: app
        version: stable
    spec:
      containers:
      - name: app
        image: myapp:1.0.0

---
# 5% traffic to canary
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-canary
spec:
  replicas: 1
  selector:
    matchLabels:
      app: app
      version: canary
  template:
    metadata:
      labels:
        app: app
        version: canary
    spec:
      containers:
      - name: app
        image: myapp:1.1.0-canary
```

### Example 3: Job and CronJob

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: data-migration
spec:
  template:
    spec:
      containers:
      - name: migration
        image: myapp:1.0.0
        command: ["python", "migration.py"]
      restartPolicy: Never
  backoffLimit: 3

---
apiVersion: batch/v1
kind: CronJob
metadata:
  name: backup
spec:
  schedule: "0 2 * * *"  # Daily at 2 AM
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: backup
            image: backup-tool:1.0.0
            command: ["backup.sh"]
          restartPolicy: OnFailure
```

### Example 4: DaemonSet

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: monitoring-agent
spec:
  selector:
    matchLabels:
      app: monitoring
  template:
    metadata:
      labels:
        app: monitoring
    spec:
      containers:
      - name: agent
        image: monitoring:1.0.0
        volumeMounts:
        - name: host
          mountPath: /host
          readOnly: true
      volumes:
      - name: host
        hostPath:
          path: /
```

### Example 5: Network Policy

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: app-network-policy
spec:
  podSelector:
    matchLabels:
      app: app
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: ingress-controller
    ports:
    - protocol: TCP
      port: 8080
  egress:
  - to:
    - podSelector:
        matchLabels:
          app: database
    ports:
    - protocol: TCP
      port: 5432
  - to:
    - namespaceSelector: {}
    ports:
    - protocol: TCP
      port: 53  # DNS
    - protocol: UDP
      port: 53
```

---

## Best Practices

### 1. Use Namespaces

```yaml
# Organize by environment
metadata:
  namespace: production
```

### 2. Set Resource Limits

```yaml
resources:
  requests:
    memory: "256Mi"
    cpu: "250m"
  limits:
    memory: "512Mi"
    cpu: "500m"
```

### 3. Health Checks

```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 8080
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
```

### 4. Use Secrets for Sensitive Data

```yaml
env:
- name: DB_PASSWORD
  valueFrom:
    secretKeyRef:
      name: db-secret
      key: password
```

### 5. Pod Disruption Budgets

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: app
```

---

## Integration with Other Skills

Kubernetes YAML Generation integrates with:

- **docker-compose-setup** - Container definitions
- **helm-charts-creation** - Template Kubernetes manifests
- **yaml-validation-config** - Validate manifests
- **build-optimization** - Build container images
- **secrets-management** - Manage sensitive data

---

## Complete Command Reference

```bash
# Apply manifests
kubectl apply -f deployment.yaml
kubectl apply -f . -R

# View resources
kubectl get deployments
kubectl get services
kubectl get pods
kubectl describe pod <pod-name>

# Logs
kubectl logs <pod-name>
kubectl logs -f <pod-name>

# Execute commands
kubectl exec -it <pod-name> -- bash

# Edit resources
kubectl edit deployment <name>

# Delete resources
kubectl delete deployment <name>
kubectl delete -f deployment.yaml
```

---

*Last Updated: 2026-02-02*
*Part of: AI Agents & Skills Repository*
