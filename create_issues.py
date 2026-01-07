#!/usr/bin/env python3
"""
GitHub Issues Generator for Bookless Project
=============================================

This script creates all 15 issues for the holk26/Bookless project using the GitHub API.

Requirements:
    - PyGithub library: pip install PyGithub
    - GitHub personal access token with 'repo' scope

Setup Instructions:
    1. Install PyGithub:
       pip install PyGithub

    2. Create a GitHub Personal Access Token:
       - Go to https://github.com/settings/tokens
       - Click "Generate new token"
       - Select 'repo' scope
       - Copy the token

    3. Set your token as an environment variable:
       export GITHUB_TOKEN="your_token_here"
       
       OR update the TOKEN variable in this script directly

    4. Run the script:
       python3 create_issues.py

    5. Verify issues were created:
       Check https://github.com/holk26/Bookless/issues
"""

import os
import sys
from github import Github
from github.GithubException import GithubException


def create_issues():
    """Create all 15 issues for the Bookless project."""
    
    # Get GitHub token from environment or ask user
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        token = input("Enter your GitHub personal access token: ").strip()
    
    if not token:
        print("Error: GitHub token is required")
        sys.exit(1)
    
    try:
        # Initialize GitHub API
        g = Github(token)
        repo = g.get_repo("holk26/Bookless")
        print(f"Connected to repository: {repo.full_name}")
        print("-" * 60)
        
    except GithubException as e:
        print(f"Error connecting to GitHub: {e}")
        sys.exit(1)
    
    # Define all issues for Bookless scheduling infrastructure
    issues = [
        {
            "title": "Implement API Key Authentication System",
            "description": """## Description
Create a secure API key authentication system with scoped permissions for multi-tenant access.

## Tasks
- [ ] Create API Key model with tenant relationship
- [ ] Implement key generation and hashing mechanism
- [ ] Create API key management endpoints (create, list, revoke)
- [ ] Add authentication middleware for API key validation
- [ ] Implement scope-based permission checking
- [ ] Add rate limiting per API key
- [ ] Write tests for authentication flow

## Context
According to the README, access to the API must be secured using API keys with scoped permissions.""",
            "labels": ["authentication", "backend", "security"]
        },
        {
            "title": "Create Resource Model and API",
            "description": """## Description
Implement the Resource entity for managing bookable resources (rooms, people, equipment, etc.).

## Tasks
- [ ] Create Resource model with tenant_id relationship
- [ ] Add migration for resources table
- [ ] Implement POST /v1/tenants/:id/resources endpoint
- [ ] Implement GET /v1/tenants/:id/resources endpoint
- [ ] Implement GET /v1/tenants/:id/resources/:resource_id endpoint
- [ ] Implement PUT /v1/tenants/:id/resources/:resource_id endpoint
- [ ] Implement DELETE /v1/tenants/:id/resources/:resource_id endpoint
- [ ] Add validation and error handling
- [ ] Write tests for resource CRUD operations

## Context
Resources are the core entities that can be scheduled (e.g., conference rooms, consultants, equipment).""",
            "labels": ["backend", "api", "database"]
        },
        {
            "title": "Implement Availability Management System",
            "description": """## Description
Create the availability management system for defining when resources are available for booking.

## Tasks
- [ ] Create Availability model (resource_id, day_of_week, start_time, end_time, etc.)
- [ ] Add migration for availability table
- [ ] Implement POST /v1/resources/:id/availability endpoint
- [ ] Implement GET /v1/resources/:id/availability endpoint
- [ ] Implement PUT /v1/resources/:id/availability/:availability_id endpoint
- [ ] Implement DELETE /v1/resources/:id/availability/:availability_id endpoint
- [ ] Support recurring availability patterns (weekly schedules)
- [ ] Add timezone handling
- [ ] Write tests for availability logic

## Context
Availability management is one of the core features mentioned in the README.""",
            "labels": ["backend", "api", "feature"]
        },
        {
            "title": "Build Booking System Core Logic",
            "description": """## Description
Implement the core booking logic for scheduling appointments with conflict detection.

## Tasks
- [ ] Create Booking model (resource_id, start_time, end_time, status, metadata)
- [ ] Add migration for bookings table
- [ ] Implement POST /v1/resources/:id/bookings endpoint
- [ ] Implement GET /v1/resources/:id/bookings endpoint
- [ ] Implement GET /v1/bookings/:id endpoint
- [ ] Add conflict detection logic (no double-booking)
- [ ] Check against availability rules
- [ ] Support booking metadata (custom fields for client apps)
- [ ] Write tests for booking logic and conflict scenarios

## Context
Booking logic is the core feature of the scheduling infrastructure.""",
            "labels": ["backend", "api", "feature"]
        },
        {
            "title": "Implement Booking Status Management",
            "description": """## Description
Create a system for managing booking states (pending, confirmed, cancelled, completed).

## Tasks
- [ ] Add status field to Booking model
- [ ] Implement PUT /v1/bookings/:id/status endpoint
- [ ] Support status transitions (pending -> confirmed, etc.)
- [ ] Add validation for valid status transitions
- [ ] Implement cancellation logic with optional reason
- [ ] Add booking history tracking
- [ ] Write tests for status transitions

## Context
Booking status management is essential for a complete booking system.""",
            "labels": ["backend", "api", "feature"]
        },
        {
            "title": "Create Webhook System for Event Notifications",
            "description": """## Description
Implement an event-based webhook system for notifying client applications of booking events.

## Tasks
- [ ] Create Webhook model (tenant_id, url, events, secret)
- [ ] Implement webhook registration endpoints
- [ ] Create event system for booking lifecycle (created, updated, cancelled, completed)
- [ ] Implement webhook delivery mechanism with retries
- [ ] Add webhook signature for security (HMAC)
- [ ] Create webhook logs for debugging
- [ ] Implement webhook testing endpoint
- [ ] Write tests for webhook delivery

## Context
The README mentions "Event-based webhooks" as a key integration method.""",
            "labels": ["backend", "api", "integration"]
        },
        {
            "title": "Implement Availability Query Engine",
            "description": """## Description
Create an efficient query system for finding available time slots for resources.

## Tasks
- [ ] Implement GET /v1/resources/:id/slots endpoint
- [ ] Add date range filtering
- [ ] Calculate available slots based on availability rules and existing bookings
- [ ] Support duration-based slot finding
- [ ] Implement timezone conversion for queries
- [ ] Optimize query performance for large datasets
- [ ] Add caching for frequently queried slots
- [ ] Write tests for slot calculation logic

## Context
Finding available slots is a critical query operation for scheduling.""",
            "labels": ["backend", "api", "feature", "performance"]
        },
        {
            "title": "Add Comprehensive API Documentation (OpenAPI/Swagger)",
            "description": """## Description
Create comprehensive API documentation using FastAPI's built-in OpenAPI support.

## Tasks
- [ ] Add detailed docstrings to all endpoints
- [ ] Define Pydantic models for all request/response schemas
- [ ] Add example requests and responses
- [ ] Document authentication flow
- [ ] Add error response documentation
- [ ] Configure Swagger UI with branding
- [ ] Generate and publish OpenAPI spec
- [ ] Create integration guide for client developers

## Context
As an API-first infrastructure, comprehensive documentation is critical.""",
            "labels": ["documentation", "api"]
        },
        {
            "title": "Implement Multi-Tenant Data Isolation",
            "description": """## Description
Ensure complete data isolation between tenants with proper filtering and validation.

## Tasks
- [ ] Add tenant_id validation to all endpoints
- [ ] Implement database-level row filtering by tenant
- [ ] Create database dependency for automatic tenant injection
- [ ] Add integration tests for cross-tenant access prevention
- [ ] Implement tenant-scoped queries in all models
- [ ] Add tenant validation middleware
- [ ] Document multi-tenant architecture

## Context
The README emphasizes "Multi-tenant by default" and "No shared databases or business logic".""",
            "labels": ["backend", "security", "architecture"]
        },
        {
            "title": "Set Up Testing Infrastructure",
            "description": """## Description
Create comprehensive testing infrastructure for API, database, and business logic.

## Tasks
- [ ] Set up pytest with FastAPI test client
- [ ] Create test database fixtures
- [ ] Add factories for test data generation
- [ ] Write unit tests for models and business logic
- [ ] Write integration tests for API endpoints
- [ ] Add test coverage reporting (aim for 80%+)
- [ ] Create GitHub Actions workflow for automated testing
- [ ] Document testing practices

## Context
Quality assurance is essential for infrastructure that will be embedded in production systems.""",
            "labels": ["testing", "quality", "devops"]
        },
        {
            "title": "Implement Error Handling and Logging",
            "description": """## Description
Add comprehensive error handling, logging, and monitoring capabilities.

## Tasks
- [ ] Configure structured logging with context
- [ ] Add request ID tracking for request tracing
- [ ] Implement standardized error responses
- [ ] Add error handlers for common exceptions
- [ ] Configure log levels and rotation
- [ ] Add performance logging (slow queries, etc.)
- [ ] Implement health check endpoint with database status
- [ ] Add observability hooks for monitoring tools

## Context
Production-grade error handling and logging are essential for reliable infrastructure.""",
            "labels": ["backend", "quality", "observability"]
        },
        {
            "title": "Set Up Production Deployment Pipeline",
            "description": """## Description
Configure production deployment with CI/CD pipeline and database migrations.

## Tasks
- [ ] Create GitHub Actions workflow for CI/CD
- [ ] Set up database migration strategy for production
- [ ] Configure environment-based settings
- [ ] Create deployment documentation
- [ ] Set up container registry and versioning
- [ ] Configure Traefik labels for production
- [ ] Add health checks for container orchestration
- [ ] Document rollback procedures

## Context
The project includes Docker infrastructure for ARM64-compatible deployment.""",
            "labels": ["devops", "deployment", "infrastructure"]
        },
        {
            "title": "Add Rate Limiting and API Protection",
            "description": """## Description
Implement rate limiting and API protection mechanisms to prevent abuse.

## Tasks
- [ ] Implement rate limiting middleware (per API key)
- [ ] Add configurable rate limits by endpoint
- [ ] Implement IP-based rate limiting for public endpoints
- [ ] Add request throttling for expensive operations
- [ ] Create rate limit response headers (X-RateLimit-*)
- [ ] Add monitoring for rate limit violations
- [ ] Write tests for rate limiting

## Context
API protection is critical for infrastructure services exposed to multiple clients.""",
            "labels": ["backend", "security", "performance"]
        },
        {
            "title": "Create Sample Client Integration Examples",
            "description": """## Description
Develop example client integrations to demonstrate how to use the Bookless API.

## Tasks
- [ ] Create Python client example
- [ ] Create JavaScript/Node.js client example
- [ ] Create cURL examples for common workflows
- [ ] Document authentication setup
- [ ] Show webhook handling example
- [ ] Create booking workflow examples
- [ ] Add error handling examples
- [ ] Publish examples in documentation

## Context
As infrastructure meant to be embedded, clear integration examples are essential.""",
            "labels": ["documentation", "examples"]
        },
        {
            "title": "Implement Data Export and Backup Tools",
            "description": """## Description
Create tools for data export, backup, and tenant data portability.

## Tasks
- [ ] Implement GET /v1/tenants/:id/export endpoint
- [ ] Support multiple export formats (JSON, CSV)
- [ ] Create backup scripts for PostgreSQL
- [ ] Implement data import functionality
- [ ] Add data validation for imports
- [ ] Document backup and restore procedures
- [ ] Add GDPR-compliant data deletion endpoints

## Context
Data portability and backup are important for enterprise adoption.""",
            "labels": ["backend", "api", "data-management"]
        }
    ]
    
    # Create all issues
    created_count = 0
    failed_count = 0
    total_issues = len(issues)
    
    for i, issue_data in enumerate(issues, 1):
        try:
            issue = repo.create_issue(
                title=issue_data["title"],
                body=issue_data["description"],
                labels=issue_data["labels"]
            )
            print(f"✓ [{i}/{total_issues}] Created: {issue_data['title']}")
            print(f"  Issue #{issue.number}")
            created_count += 1
            
        except GithubException as e:
            print(f"✗ [{i}/{total_issues}] Failed: {issue_data['title']}")
            print(f"  Error: {e}")
            failed_count += 1
    
    # Summary
    print("-" * 60)
    print(f"\nSummary:")
    print(f"  Successfully created: {created_count} issues")
    if failed_count > 0:
        print(f"  Failed: {failed_count} issues")
    print(f"\nView issues at: https://github.com/holk26/Bookless/issues")
    
    return failed_count == 0


if __name__ == "__main__":
    success = create_issues()
    sys.exit(0 if success else 1)
