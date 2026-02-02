# SSH Key Management Skill

**Master SSH key generation, authentication, GitHub setup, certificates, and security best practices.**

## Overview

SSH keys are essential for secure authentication. This skill covers key generation, management, and security.

**What it does:**
- Generates SSH key pairs
- Configures SSH authentication
- Sets up GitHub SSH access
- Manages multiple keys
- Implements SSH certificates
- Configures SSH agents
- Manages key permissions
- Rotates and revokes keys

**Perfect for:**
- GitHub and Git authentication
- Server access management
- Automated deployments
- Team credential management
- Secure CI/CD pipelines

---

## When to Use This Skill

Use SSH Key Management when you need to:

- **Generate SSH key pairs** for authentication
- **Set up GitHub SSH access** without passwords
- **Manage multiple SSH keys** for different hosts
- **Configure SSH agents** for convenience
- **Implement SSH certificates** for compliance
- **Secure deployment keys** in CI/CD
- **Manage team SSH keys** centrally
- **Audit SSH access** and usage

---

## Quick Start (10 Minutes)

### 1. Generate SSH Key Pair

```bash
# Generate Ed25519 key (recommended, modern)
ssh-keygen -t ed25519 -C "wallace@example.com" -f ~/.ssh/id_ed25519

# Generate RSA key (compatible with older systems)
ssh-keygen -t rsa -b 4096 -C "wallace@example.com" -f ~/.ssh/id_rsa

# When prompted, enter passphrase (or leave blank for no passphrase)
# Private key: ~/.ssh/id_ed25519
# Public key: ~/.ssh/id_ed25519.pub
```

### 2. Add to SSH Agent

```bash
# Start SSH agent (on macOS/Linux)
eval "$(ssh-agent -s)"

# Add key
ssh-add ~/.ssh/id_ed25519

# Verify added
ssh-add -l
```

### 3. Add Public Key to GitHub

```bash
# Copy public key
cat ~/.ssh/id_ed25519.pub | pbcopy  # macOS
cat ~/.ssh/id_ed25519.pub | xclip  # Linux

# Or view and copy manually
cat ~/.ssh/id_ed25519.pub
```

GitHub → Settings → SSH and GPG keys → New SSH key → Paste

### 4. Test Connection

```bash
ssh -T git@github.com
# Hi username! You've successfully authenticated...
```

### 5. Configure Git to Use SSH

```bash
# Global configuration
git config --global url."git@github.com:".insteadOf "https://github.com/"

# Or per-repository
cd my-repo
git config url."git@github.com:".insteadOf "https://github.com/"
```

---

## How It Works

### 1. SSH Key Types

**Ed25519 (Modern, Recommended):**

```bash
ssh-keygen -t ed25519 -C "email@example.com"
# Smaller key, faster, secure
# Best for: All modern systems
```

**RSA (Traditional, Compatible):**

```bash
ssh-keygen -t rsa -b 4096 -C "email@example.com"
# Larger key, universally supported
# Best for: Legacy systems
```

**ECDSA (Balanced):**

```bash
ssh-keygen -t ecdsa -b 521 -C "email@example.com"
# Medium key size, good speed/security
# Best for: Systems that don't support Ed25519
```

### 2. Key Management

**Multiple Keys:**

```bash
# Create separate keys for different purposes
ssh-keygen -t ed25519 -f ~/.ssh/id_github -C "github@example.com"
ssh-keygen -t ed25519 -f ~/.ssh/id_work -C "work@example.com"
ssh-keygen -t ed25519 -f ~/.ssh/id_personal -C "personal@example.com"

# Configure in ~/.ssh/config:
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_github

Host work-server.com
  HostName work-server.com
  User deploy
  IdentityFile ~/.ssh/id_work
```

**SSH Config Organization:**

```bash
# ~/.ssh/config

# GitHub
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_github
  AddKeysToAgent yes
  IdentitiesOnly yes

# Work Server
Host work-server
  HostName work-server.com
  User deploy
  IdentityFile ~/.ssh/id_work
  Port 2222
  ServerAliveInterval 60

# Personal Server
Host personal
  HostName personal.com
  User wallace
  IdentityFile ~/.ssh/id_personal
```

### 3. SSH Agent

**Starting SSH Agent:**

```bash
# One-time
eval "$(ssh-agent -s)"

# Permanent (add to ~/.bashrc or ~/.zshrc)
if ! pgrep -x "ssh-agent" > /dev/null; then
  eval "$(ssh-agent -s)"
fi

# Or use macOS Keychain
# SSH agent is automatic on macOS
```

**Managing Keys:**

```bash
# Add key with passphrase stored
ssh-add ~/.ssh/id_ed25519

# Add with specific lifetime (3600 seconds = 1 hour)
ssh-add -t 3600 ~/.ssh/id_ed25519

# Add key permanently (macOS)
ssh-add --apple-use-keychain ~/.ssh/id_ed25519

# List loaded keys
ssh-add -l

# Remove specific key
ssh-add -d ~/.ssh/id_ed25519

# Remove all keys
ssh-add -D

# Test connection
ssh -T git@github.com
```

### 4. Key Permissions

**Correct Permissions (Critical):**

```bash
# Set correct permissions
chmod 700 ~/.ssh          # Directory: 700
chmod 600 ~/.ssh/id_*     # Private keys: 600
chmod 644 ~/.ssh/*.pub    # Public keys: 644
chmod 644 ~/.ssh/config   # Config: 644

# Verify
ls -la ~/.ssh/
# Example output:
# drwx------  wallace  staff   ~/.ssh
# -rw-------  wallace  staff   id_ed25519
# -rw-r--r--  wallace  staff   id_ed25519.pub
```

### 5. GitHub SSH Configuration

**Add Key to GitHub:**

1. Copy public key: `cat ~/.ssh/id_ed25519.pub`
2. GitHub Settings → SSH and GPG keys → New SSH key
3. Paste key with title

**Verify Connection:**

```bash
ssh -T git@github.com
# Expected: Hi username! You've successfully authenticated...
```

**Configure Git:**

```bash
# Use SSH instead of HTTPS
git config --global url."git@github.com:".insteadOf "https://github.com/"

# Or per-repo
cd my-repo
git remote set-url origin git@github.com:owner/repo.git
```

### 6. Key Rotation

**Generate New Key:**

```bash
# Create new key with same name (backup old one first)
cp ~/.ssh/id_ed25519 ~/.ssh/id_ed25519.old

# Generate new key
ssh-keygen -t ed25519 -C "email@example.com" -f ~/.ssh/id_ed25519

# Add to GitHub (replaces old key)
# Add new public key to GitHub, remove old key
```

**Rotate Regularly:**

```bash
# Every 1-2 years or after suspected compromise
# Document rotation in team wiki
```

### 7. SSH Certificates

**Generate Certificate:**

```bash
# Generate certificate from public key
ssh-keygen -s ~/.ssh/ca_key \
  -I "username" \
  -n "username" \
  -V +52w \
  ~/.ssh/id_ed25519.pub

# Creates: ~/.ssh/id_ed25519-cert.pub
# Valid for 52 weeks

# Use certificate
ssh -i ~/.ssh/id_ed25519-cert.pub user@host.com
```

**Certificate Configuration:**

```bash
# ~/.ssh/config
Host myhost
  HostName myhost.com
  User wallace
  IdentityFile ~/.ssh/id_ed25519
  CertificateFile ~/.ssh/id_ed25519-cert.pub
```

### 8. Secure Deployment

**CI/CD Deploy Keys:**

```bash
# Generate deployment key
ssh-keygen -t ed25519 -f ~/.ssh/deploy -C "deploy@example.com"

# Add to repository (GitHub → Settings → Deploy keys)
# Read-only: Don't commit code
# Read-write: For deployments that need to push

# Use in GitHub Actions
env:
  SSH_KEY: ${{ secrets.DEPLOY_KEY }}
  SSH_HOST: deploy.example.com
```

**Temporary Access:**

```bash
# Generate time-limited key
ssh-keygen -t ed25519-cert -f ~/.ssh/temp -V -1d +1d

# Key valid for 1 day from creation
# Automatically expires
```

---

## Configuration

### SSH Config Template

`~/.ssh/config`:

```
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_github
  AddKeysToAgent yes
  IdentitiesOnly yes
  StrictHostKeyChecking no
  UserKnownHostsFile /dev/null

Host work-*.example.com
  User deploy
  IdentityFile ~/.ssh/id_work
  Port 2222
  ServerAliveInterval 60
  ServerAliveCountMax 3

Host personal
  HostName personal.example.com
  User wallace
  IdentityFile ~/.ssh/id_personal
  LocalForward 3000 localhost:3000

Host *
  AddKeysToAgent yes
  IgnoreUnknown UseKeychain
  UseKeychain yes  # macOS Keychain
  IdentitiesOnly yes
```

### Git Configuration

```bash
# Use SSH for GitHub
git config --global url."git@github.com:".insteadOf "https://github.com/"

# Use SSH for GitLab
git config --global url."git@gitlab.com:".insteadOf "https://gitlab.com/"

# Verify
git config --global --list | grep url
```

---

## Examples

### Example 1: Generate and Setup

```bash
#!/bin/bash

# Generate SSH key
ssh-keygen -t ed25519 -C "wallace@example.com" -f ~/.ssh/id_ed25519 -N ""

# Set correct permissions
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub

# Add to SSH agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Copy to GitHub
echo "Add this key to GitHub:"
cat ~/.ssh/id_ed25519.pub

# Test
ssh -T git@github.com
```

### Example 2: Multiple Keys

```bash
# Create personal key
ssh-keygen -t ed25519 -f ~/.ssh/id_personal

# Create work key
ssh-keygen -t ed25519 -f ~/.ssh/id_work

# Create ~/.ssh/config
cat > ~/.ssh/config << 'EOF'
Host github-personal
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_personal

Host github-work
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_work
EOF

# Clone with different key
git clone git@github-personal:personal/repo.git
git clone git@github-work:work/repo.git
```

### Example 3: Key Rotation Script

```bash
#!/bin/bash

# Backup old key
mv ~/.ssh/id_ed25519 ~/.ssh/id_ed25519.$(date +%s).bak

# Generate new key
ssh-keygen -t ed25519 -C "wallace@example.com" -f ~/.ssh/id_ed25519 -N ""

# Set permissions
chmod 600 ~/.ssh/id_ed25519

# Add to agent
ssh-add ~/.ssh/id_ed25519

# Instructions for GitHub update
echo "Update GitHub SSH key:"
cat ~/.ssh/id_ed25519.pub
echo ""
echo "1. Go to GitHub Settings → SSH Keys"
echo "2. Add new key"
echo "3. Remove old key"
echo "4. Verify: ssh -T git@github.com"
```

### Example 4: CI/CD Deploy Key

```yaml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Deploy with SSH
        env:
          SSH_KEY: ${{ secrets.DEPLOY_KEY }}
          SSH_HOST: deploy.example.com
          SSH_USER: deploy
        run: |
          mkdir -p ~/.ssh
          echo "$SSH_KEY" > ~/.ssh/deploy_key
          chmod 600 ~/.ssh/deploy_key
          ssh-keyscan -H $SSH_HOST >> ~/.ssh/known_hosts
          ssh -i ~/.ssh/deploy_key $SSH_USER@$SSH_HOST << 'DEPLOY'
            cd /app
            git pull origin main
            npm install
            npm run build
            npm start
          DEPLOY
```

### Example 5: SSH Agent Forwarding

```bash
# ~/.ssh/config - Forward agent to remote server
Host deploy-server
  HostName deploy.example.com
  User deploy
  IdentityFile ~/.ssh/id_deploy
  ForwardAgent yes

# Now you can access GitHub from remote server
ssh deploy-server
git clone git@github.com:owner/repo.git  # Works from remote!
```

---

## Best Practices

### 1. Always Use Passphrases

```bash
# Don't leave blank - use strong passphrase
ssh-keygen -t ed25519 -C "email@example.com"
# Enter passphrase: [enter secure passphrase]

# SSH agent stores passphrase, so you don't re-type it
ssh-add ~/.ssh/id_ed25519
# Enter passphrase: [only once]
```

### 2. Use Ed25519 Keys

```bash
# Modern, secure, efficient
ssh-keygen -t ed25519

# Not:
ssh-keygen -t dsa    # Deprecated
ssh-keygen -t rsa    # Larger key
```

### 3. Rotate Keys Regularly

```bash
# Every 1-2 years
# After team member leaves
# After suspected compromise
```

### 4. Never Share Private Keys

```bash
# Private key stays on YOUR machine
# Only share public key (id_ed25519.pub)

# Bad: Committing private key
# DON'T: Add id_ed25519 to version control

# Good: Use deployment keys in CI/CD
# GitHub Actions use encrypted secrets
```

### 5. Secure Permissions Always

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_*
chmod 644 ~/.ssh/*.pub
chmod 644 ~/.ssh/config
```

---

## Integration with Other Skills

SSH Key Management integrates with:

- **github-security-scanning** - Detect exposed keys
- **secrets-management** - Manage deployment keys
- **github-cli-automation** - Git authentication
- **build-optimization** - Secure build access

---

## Complete Command Reference

```bash
# Key Generation
ssh-keygen -t ed25519 -C "email" -f ~/.ssh/id_ed25519

# SSH Agent
ssh-agent
ssh-add ~/.ssh/id_ed25519
ssh-add -l
ssh-add -d ~/.ssh/id_ed25519
ssh-add -D

# Testing
ssh -T git@github.com
ssh -vvv git@github.com  # Verbose debugging

# Key Management
ssh-keygen -p -f ~/.ssh/id_ed25519  # Change passphrase
ssh-keygen -l -f ~/.ssh/id_ed25519  # Show fingerprint
ssh-keygen -R hostname              # Remove from known_hosts
```

---

*Last Updated: 2026-02-02*
*Part of: AI Agents & Skills Repository*
