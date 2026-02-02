---
name: infrastructure-as-code
description: Create Infrastructure as Code templates using Terraform, CloudFormation, or Pulumi
---

# Infrastructure as Code Skill

## When to Use This Skill

- Provisioning cloud infrastructure
- Creating reproducible environments
- Managing multi-region deployments
- Disaster recovery planning
- Cost tracking and optimization

## Quick Start

```
/infrastructure-as-code <cloud_provider_and_resources>
```

## Terraform Example

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# VPC
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
}

# Security Group
resource "aws_security_group" "web" {
  vpc_id = aws_vpc.main.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# EC2 Instance
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"
  key_name      = "my-key"

  vpc_security_group_ids = [aws_security_group.web.id]

  tags = {
    Name = "WebServer"
  }
}

# RDS Database
resource "aws_db_instance" "main" {
  allocated_storage    = 20
  db_name              = "mydb"
  engine               = "postgres"
  engine_version       = "15"
  instance_class       = "db.t3.micro"
  username             = "admin"
  password             = random_password.db.result
  skip_final_snapshot  = true
}

output "instance_public_ip" {
  value = aws_instance.web.public_ip
}
```

## Integration with Other Skills

- **`cicd-pipeline-setup`**: Provision in CI/CD
- **`monitoring-setup`**: Infrastructure monitoring
- **`security-scanning`**: Security scanning IaC

