#!/usr/bin/env python3
"""
Dashboard Health Check Script

Validates all dashboard links and checks accessibility of embedded dashboards.
"""

import yaml
import sys
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

def load_projects():
    """Load projects from _data/projects.yml"""
    try:
        with open('_data/projects.yml', 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"❌ Error loading projects.yml: {e}")
        sys.exit(1)

def check_url(url, timeout=10):
    """Check if a URL is accessible"""
    if not url:
        return None, "No URL provided"
    
    try:
        req = Request(url, headers={'User-Agent': 'BRT Dashboard Health Check'})
        response = urlopen(req, timeout=timeout)
        return response.getcode(), "OK"
    except HTTPError as e:
        return e.code, f"HTTP Error: {e.reason}"
    except URLError as e:
        return None, f"URL Error: {e.reason}"
    except Exception as e:
        return None, f"Error: {str(e)}"

def main():
    """Main health check function"""
    print("🔍 BRT Dashboard Health Check\n")
    print("=" * 60)
    
    projects = load_projects()
    
    if not projects:
        print("❌ No projects found in projects.yml")
        sys.exit(1)
    
    print(f"Found {len(projects)} projects to check\n")
    
    total = len(projects)
    checked = 0
    accessible = 0
    failed = []
    
    for project in projects:
        slug = project.get('slug', 'unknown')
        name = project.get('name', slug)
        dashboard_url = project.get('dashboard_url', '')
        github_url = project.get('github_url', '')
        
        print(f"\n📊 {name} ({slug})")
        print("-" * 60)
        
        # Check dashboard URL
        if dashboard_url:
            checked += 1
            code, message = check_url(dashboard_url)
            if code == 200:
                print(f"  ✅ Dashboard: {dashboard_url}")
                accessible += 1
            else:
                print(f"  ❌ Dashboard: {dashboard_url}")
                print(f"     Status: {code or 'N/A'} - {message}")
                failed.append({'project': name, 'url': dashboard_url, 'error': message})
        else:
            print(f"  ⚠️  Dashboard: No URL configured")
        
        # Check GitHub URL
        if github_url:
            code, message = check_url(github_url)
            if code == 200:
                print(f"  ✅ GitHub: {github_url}")
            else:
                print(f"  ⚠️  GitHub: {github_url} - {message}")
        else:
            print(f"  ⚠️  GitHub: No URL configured")
    
    # Summary
    print("\n" + "=" * 60)
    print("📈 SUMMARY")
    print("=" * 60)
    print(f"Total projects: {total}")
    print(f"Dashboards checked: {checked}")
    print(f"Accessible dashboards: {accessible}")
    print(f"Failed checks: {len(failed)}")
    
    if failed:
        print("\n❌ FAILED CHECKS:")
        for item in failed:
            print(f"  - {item['project']}: {item['error']}")
        sys.exit(1)
    else:
        print("\n✅ All dashboard checks passed!")
        sys.exit(0)

if __name__ == '__main__':
    main()
