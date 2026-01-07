#!/usr/bin/env python3
"""
GitHub Issues Generator for Bookless Project
=============================================

This script creates all 14 issues for the holk26/Bookless project using the GitHub API.

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
    """Create all 14 issues for the Bookless project."""
    
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
    
    # Define all 14 issues
    issues = [
        {
            "title": "Set up project structure and dependencies",
            "description": """## Description
Set up the initial project structure and install all required dependencies.

## Tasks
- [ ] Create project directory structure
- [ ] Initialize virtual environment
- [ ] Create requirements.txt with all dependencies
- [ ] Set up .gitignore file
- [ ] Initialize Git repository
- [ ] Create README.md with project overview""",
            "labels": ["setup", "documentation"]
        },
        {
            "title": "Design and implement database schema",
            "description": """## Description
Design the database schema for storing books, users, reading lists, and reviews.

## Tasks
- [ ] Define database structure
- [ ] Create migration files
- [ ] Implement ORM models
- [ ] Add database constraints and indexes
- [ ] Write database initialization script""",
            "labels": ["database", "backend"]
        },
        {
            "title": "Create user authentication system",
            "description": """## Description
Implement user registration, login, and authentication mechanisms.

## Tasks
- [ ] Create user model
- [ ] Implement registration endpoint
- [ ] Implement login endpoint
- [ ] Add JWT token generation
- [ ] Create password hashing mechanism
- [ ] Add authentication middleware""",
            "labels": ["authentication", "backend"]
        },
        {
            "title": "Build book catalog API endpoints",
            "description": """## Description
Develop API endpoints for browsing and searching books.

## Tasks
- [ ] Create GET /books endpoint
- [ ] Create GET /books/:id endpoint
- [ ] Implement search functionality
- [ ] Add filtering by genre, author, rating
- [ ] Implement pagination
- [ ] Add caching for frequently accessed books""",
            "labels": ["backend", "api"]
        },
        {
            "title": "Implement user reading lists feature",
            "description": """## Description
Create functionality for users to create and manage reading lists.

## Tasks
- [ ] Create reading list model
- [ ] Implement POST /reading-lists endpoint
- [ ] Implement GET /reading-lists/:id endpoint
- [ ] Implement PUT /reading-lists/:id endpoint
- [ ] Implement DELETE /reading-lists/:id endpoint
- [ ] Add books to reading list functionality""",
            "labels": ["backend", "api", "feature"]
        },
        {
            "title": "Build book review and rating system",
            "description": """## Description
Enable users to review books and provide ratings.

## Tasks
- [ ] Create review model
- [ ] Implement POST /books/:id/reviews endpoint
- [ ] Implement GET /books/:id/reviews endpoint
- [ ] Calculate average ratings
- [ ] Add review validation
- [ ] Implement review edit/delete functionality""",
            "labels": ["backend", "api", "feature"]
        },
        {
            "title": "Create frontend UI for book browsing",
            "description": """## Description
Develop the frontend interface for viewing and browsing books.

## Tasks
- [ ] Create book listing page
- [ ] Implement book detail page
- [ ] Add search bar component
- [ ] Implement filter sidebar
- [ ] Add pagination controls
- [ ] Style with responsive design""",
            "labels": ["frontend", "ui"]
        },
        {
            "title": "Build user dashboard page",
            "description": """## Description
Create a dashboard page for logged-in users.

## Tasks
- [ ] Design dashboard layout
- [ ] Display user reading lists
- [ ] Show reading progress
- [ ] Display recent reviews
- [ ] Add quick links to common actions
- [ ] Implement responsive design""",
            "labels": ["frontend", "ui", "feature"]
        },
        {
            "title": "Implement user profile management",
            "description": """## Description
Create pages and functionality for users to manage their profile.

## Tasks
- [ ] Create profile page
- [ ] Implement edit profile functionality
- [ ] Add profile picture upload
- [ ] Create account settings page
- [ ] Implement password change functionality
- [ ] Add account deletion option""",
            "labels": ["frontend", "backend", "feature"]
        },
        {
            "title": "Add comprehensive unit tests",
            "description": """## Description
Write unit tests for all critical functionality.

## Tasks
- [ ] Set up testing framework
- [ ] Write authentication tests
- [ ] Write API endpoint tests
- [ ] Write database model tests
- [ ] Achieve 80%+ code coverage
- [ ] Set up CI/CD pipeline for tests""",
            "labels": ["testing", "quality"]
        },
        {
            "title": "Implement error handling and logging",
            "description": """## Description
Add comprehensive error handling and logging throughout the application.

## Tasks
- [ ] Set up logging framework
- [ ] Add error handlers for common exceptions
- [ ] Implement API error responses
- [ ] Add database error handling
- [ ] Create error log files
- [ ] Add request/response logging""",
            "labels": ["backend", "quality"]
        },
        {
            "title": "Set up deployment and CI/CD pipeline",
            "description": """## Description
Configure deployment infrastructure and automated testing pipeline.

## Tasks
- [ ] Set up GitHub Actions workflows
- [ ] Configure production environment
- [ ] Set up database migrations
- [ ] Configure environment variables
- [ ] Set up SSL/TLS certificates
- [ ] Create deployment documentation""",
            "labels": ["devops", "deployment"]
        },
        {
            "title": "Optimize performance and caching",
            "description": """## Description
Improve application performance through caching and optimization.

## Tasks
- [ ] Implement Redis caching
- [ ] Optimize database queries
- [ ] Add response compression
- [ ] Implement lazy loading
- [ ] Optimize image assets
- [ ] Set up CDN for static files""",
            "labels": ["performance", "optimization"]
        },
        {
            "title": "Create comprehensive documentation",
            "description": """## Description
Write complete documentation for developers and users.

## Tasks
- [ ] Write API documentation
- [ ] Create setup guide
- [ ] Write contribution guidelines
- [ ] Create user manual
- [ ] Add code comments
- [ ] Create architecture documentation""",
            "labels": ["documentation"]
        }
    ]
    
    # Create all issues
    created_count = 0
    failed_count = 0
    
    for i, issue_data in enumerate(issues, 1):
        try:
            issue = repo.create_issue(
                title=issue_data["title"],
                body=issue_data["description"],
                labels=issue_data["labels"]
            )
            print(f"✓ [{i}/14] Created: {issue_data['title']}")
            print(f"  Issue #{issue.number}")
            created_count += 1
            
        except GithubException as e:
            print(f"✗ [{i}/14] Failed: {issue_data['title']}")
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
