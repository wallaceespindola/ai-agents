---
name: security-scanning
description: Integrate security scanning tools for SAST, DAST, and dependency scanning
---

# Security Scanning Skill

## When to Use This Skill

- Static analysis (SAST) for code vulnerabilities
- Dynamic analysis (DAST) for runtime issues
- Dependency vulnerability scanning
- Container image scanning
- Secrets detection
- Infrastructure security scanning

## Quick Start

```
/security-scanning <application_type>
```

## SAST Tools

- **SonarQube**: Code quality and security
- **Snyk**: Developer-first security
- **Checkmarx**: Enterprise SAST
- **Semgrep**: Open-source pattern matching

## Dependency Scanning

```bash
# npm
npm audit
npm audit fix

# Python
pip-audit
safety check

# Java
snyk test --severity-threshold=high
```

## OWASP Dependency Check

```xml
<plugin>
  <groupId>org.owasp</groupId>
  <artifactId>dependency-check-maven</artifactId>
  <version>8.4.0</version>
  <configuration>
    <failBuildOnCVSS>7</failBuildOnCVSS>
  </configuration>
</plugin>
```

## GitHub Actions Security Scanning

```yaml
- name: Run Snyk Security Scan
  uses: snyk/actions/node@master
  env:
    SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}

- name: Run CodeQL
  uses: github/codeql-action/analyze@v2
```

## Secrets Detection

```bash
# Detect hardcoded secrets
git secrets --install
git secrets --register-aws

# TruffleHog for secret scanning
trufflehog filesystem . --json
```

## Integration with Other Skills

- **`cicd-pipeline-setup`**: Scan in CI/CD
- **`infrastructure-as-code`**: Scan IaC files
- **`docker-setup`**: Scan container images

