---
name: deploy-infrastructure
description: Infrastructure, deployment, and DevOps tasks for hiddenbeer and skipy (Docker, systemd, GitHub Actions, Fail2Ban, UFW). Use when deploying, troubleshooting production, or managing infrastructure.
user-invocable: true
allowed-tools: Bash(docker *), Bash(systemctl *), Bash(ssh *), Bash(git *), Read, Grep
---

# Infrastructure & Deployment

Production deployment patterns for hiddenbeer and skipy.

## Deployment Architectures

### hiddenbeer
- **Environment**: Single VPS with Docker Compose
- **Stack**: MongoDB + FastAPI + Next.js (all containerized)
- **Domains**: Production domain with HTTPS
- **Orchestration**: Docker Compose
- **Process Manager**: Docker containers with restart policies

### skipy
- **Environment**: Dual VPS (Belgium + Brazil)
- **Stack**: MongoDB + FastAPI + Next.js (Client + Admin) + Expo Web (Manager)
- **Domains**:
  - skipy.online (Belgium)
  - skipy.com.br (Brazil)
- **Orchestration**: systemd services
- **Reverse Proxy**: Caddy (HTTPS on port 443, Let's Encrypt auto-renewal)
- **Images**: Private Docker images on GitHub Container Registry (GHCR)

## Container Management

### Docker Commands (hiddenbeer)

```bash
# Start full stack
make docker-up              # docker compose up --build

# Stop all services
docker compose down

# View logs
docker compose logs -f backend
docker compose logs -f frontend
docker compose logs -f mongodb

# Rebuild specific service
docker compose up --build backend

# Execute commands in container
docker compose exec backend bash
docker compose exec mongodb mongosh

# Check status
docker compose ps
docker ps -a
```

### Docker Images (skipy - GHCR)

```bash
# Login to GitHub Container Registry
echo $GITHUB_TOKEN | docker login ghcr.io -u USERNAME --password-stdin

# Pull latest images
docker pull ghcr.io/username/skipy-api:latest
docker pull ghcr.io/username/skipy-client:latest

# Check image versions
docker images | grep skipy

# Remove old images
docker image prune -a
```

## systemd Service Management (skipy)

### Service Commands

```bash
# Check service status
systemctl status skipy-api
systemctl status skipy-client
systemctl status skipy-admin
systemctl status skipy-manager
systemctl status caddy

# Restart services (after deployment)
sudo systemctl restart skipy-api
sudo systemctl restart skipy-client

# View logs
journalctl -u skipy-api -f           # Follow logs
journalctl -u skipy-api --since "1 hour ago"
journalctl -u skipy-api -n 100       # Last 100 lines

# Enable/disable services
sudo systemctl enable skipy-api      # Start on boot
sudo systemctl disable skipy-api     # Don't start on boot

# Check all skipy services
systemctl list-units | grep skipy
```

### Service File Locations
- `/etc/systemd/system/skipy-api.service`
- `/etc/systemd/system/skipy-client.service`
- `/etc/systemd/system/skipy-admin.service`
- `/etc/systemd/system/skipy-manager.service`

After editing service files:
```bash
sudo systemctl daemon-reload
sudo systemctl restart service-name
```

## Deployment Workflow

### hiddenbeer Deployment

1. **Build and test locally**
   ```bash
   make test
   make lint
   git push origin main
   ```

2. **Wait for GitHub Actions CI** (check passes)

3. **Deploy to VPS**
   ```bash
   ssh user@vps
   cd /path/to/hiddenbeer
   git pull origin main
   docker compose down
   docker compose up --build -d
   docker compose logs -f
   ```

4. **Verify deployment**
   ```bash
   curl https://hiddenbeer-domain.com/health
   docker compose ps
   ```

### skipy Deployment

1. **Build and push Docker images** (GitHub Actions or manual)
   ```bash
   docker build -t ghcr.io/username/skipy-api:latest .
   docker push ghcr.io/username/skipy-api:latest
   ```

2. **Deploy to VPS**
   ```bash
   ssh user@skipy-vps
   cd /opt/skipy
   docker pull ghcr.io/username/skipy-api:latest
   sudo systemctl restart skipy-api
   ```

3. **Check deployment**
   ```bash
   systemctl status skipy-api
   journalctl -u skipy-api -n 50
   curl https://skipy.online/api/health
   ```

## Environment Management

### Environment Files

Both projects use environment-specific `.env` files:

- `.env.example` - Template (committed to git)
- `.env` - Local development (gitignored)
- `.env.be` - Belgium production (on VPS, not in git)
- `.env.br` - Brazil production (on VPS, not in git)

**Never commit production secrets!**

### Updating Environment Variables

```bash
# On VPS
ssh user@vps
cd /path/to/project
nano .env                    # Edit variables

# If using Docker Compose (hiddenbeer)
docker compose down
docker compose up -d         # Reload with new env

# If using systemd (skipy)
sudo systemctl restart skipy-api    # Reload service
```

## Security

### Fail2Ban (Rate Limiting)

```bash
# Check status
sudo fail2ban-client status

# Check specific jail
sudo fail2ban-client status sshd

# Unban IP
sudo fail2ban-client set sshd unbanip 1.2.3.4

# View logs
sudo tail -f /var/log/fail2ban.log
```

### UFW Firewall

```bash
# Check status
sudo ufw status verbose

# Allow specific ports
sudo ufw allow 443/tcp       # HTTPS
sudo ufw allow 22/tcp        # SSH

# Deny/delete rules
sudo ufw deny 8080/tcp
sudo ufw delete allow 8080/tcp

# Enable/disable
sudo ufw enable
sudo ufw disable
```

### HTTPS with Caddy (skipy)

Caddy auto-renews Let's Encrypt certificates. Check:

```bash
# Check Caddy status
systemctl status caddy

# View Caddy logs
journalctl -u caddy -f

# Test Caddy config
sudo caddy validate --config /etc/caddy/Caddyfile

# Reload Caddy config
sudo systemctl reload caddy
```

## GitHub Actions CI/CD

### Workflows Located In
- `.github/workflows/ci.yml` - Build, test, lint
- `.github/workflows/deploy.yml` - Docker build + push

### Common CI Tasks
- Lint: flake8, ESLint, mypy
- Test: pytest, Jest
- Build: Docker images
- Security: CodeQL scanning (some projects)
- Deploy: Push to GHCR, trigger VPS updates

### Checking CI Status
```bash
gh workflow list              # List workflows
gh run list                   # Recent runs
gh run view RUN_ID            # View specific run
gh run watch                  # Watch current run
```

## Monitoring & Health Checks

### Health Endpoints
- FastAPI: `/health` or `/api/health`
- Spring Boot: `/actuator/health`
- Next.js: Custom health endpoint

```bash
# Check backend health
curl https://api.domain.com/health

# Check all services
curl -I https://domain.com      # Frontend
curl https://domain.com/api/health    # Backend
```

### MongoDB Health

```bash
# Connect to MongoDB
docker compose exec mongodb mongosh   # Docker
mongosh                               # Local

# Check status
db.adminCommand({ serverStatus: 1 })

# Check replica set
rs.status()

# Database stats
db.stats()
```

### Resource Monitoring

```bash
# CPU and memory
htop
top

# Disk space
df -h
du -sh /var/lib/docker

# Docker stats
docker stats
docker system df

# systemd resource usage
systemctl status skipy-api | grep Memory
```

## Troubleshooting

### Service Won't Start

1. Check logs: `journalctl -u service-name -n 100`
2. Check port conflicts: `sudo lsof -i :8100`
3. Check environment: `systemctl cat service-name` (view env vars)
4. Check permissions: File ownership, Docker socket access

### Database Connection Issues

1. Check MongoDB running: `docker ps | grep mongo` or `systemctl status mongodb`
2. Check connection string in `.env`
3. Check network: `docker network ls` (Docker Compose)
4. Test connection: `mongosh "connection-string"`

### HTTPS/Certificate Issues

1. Check Caddy: `journalctl -u caddy -n 50`
2. Test certificate: `curl -vI https://domain.com`
3. Check DNS: `dig domain.com`
4. Renew manually: Caddy auto-renews, but check logs for errors

### High Memory/CPU

1. Check Docker stats: `docker stats`
2. Restart services: `systemctl restart service-name`
3. Check for memory leaks in logs
4. Scale down if needed (reduce workers, containers)

## Backup & Recovery

### MongoDB Backups

```bash
# Dump database
docker compose exec mongodb mongodump --out /backup
mongodump --uri="mongodb://..." --out backup/

# Restore database
docker compose exec mongodb mongorestore /backup
mongorestore --uri="mongodb://..." backup/
```

### Code Backups
- All code in git repositories
- VPS snapshots (provider-specific)
- Environment files backed up separately (encrypted)

## Quick Reference

```bash
# Deploy checklist
1. make test && make lint           # Local tests pass
2. git push                         # Push to GitHub
3. Wait for CI ✅                   # GitHub Actions pass
4. ssh to VPS                       # Connect to server
5. git pull / docker pull           # Get latest code/images
6. Restart services                 # docker compose / systemctl
7. Check logs                       # Verify deployment
8. Test endpoints                   # curl health checks

# Emergency rollback
git revert HEAD                     # Revert commit
git push                            # Push revert
# Then deploy previous version
```
