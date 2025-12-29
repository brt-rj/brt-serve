# Contributing to BRT Dashboard Hub

Thank you for contributing to the BRT Dashboard Hub! This guide will help you integrate your project's dashboard and documentation into the platform.

## 🎯 Overview

Since project repositories remain **private**, you'll use GitHub Actions in your private repo to automatically push dashboard artifacts and documentation to this public `brt-view` repository.

## 🔐 Setup: Personal Access Token (PAT) Approach

### Step 1: Create a Fine-Grained Personal Access Token

1. Go to GitHub Settings → Developer settings → Personal access tokens → Fine-grained tokens
2. Click "Generate new token"
3. Configure the token:
   - **Name**: `brt-view-deploy-{your-project-name}`
   - **Expiration**: 1 year (or custom)
   - **Repository access**: "Only select repositories" → Choose `brt-rj/brt-view`
   - **Permissions**:
     - Repository permissions → Contents: **Read and write**
     - Repository permissions → Metadata: **Read-only** (auto-selected)
4. Click "Generate token" and **copy the token** (you won't see it again!)

### Step 2: Add Token as Secret in Your Private Repository

1. Go to your private repository → Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Name: `BRT_VIEW_PAT`
4. Value: Paste the token you copied
5. Click "Add secret"

### Step 3: Create Deployment Workflow in Your Private Repo

Create `.github/workflows/deploy-dashboard.yml` in your private repository:

```yaml
name: Deploy Dashboard to brt-view

on:
  push:
    branches: [main]
    paths:
      - 'dashboard/**'
      - 'PROJECT_DETAILS.md'
  workflow_dispatch:

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout private repo
        uses: actions/checkout@v3
      
      - name: Build Dashboard
        run: |
          # Build/export your dashboard based on type
          
          # For Streamlit (example):
          # pip install streamlit streamlit-static-export
          # streamlit run app.py --export static --output dashboard/build
          
          # For Evidence (example):
          # npm install
          # npm run build
          
          # For Superset/Looker/Rill (iframe only):
          # No build step needed - just update metadata
          
          echo "Dashboard build completed"
      
      - name: Prepare deployment artifacts
        run: |
          mkdir -p deploy
          
          # Copy dashboard files (adjust paths as needed)
          # cp -r dashboard/build/* deploy/
          
          # Copy project details
          cp PROJECT_DETAILS.md deploy/ || echo "PROJECT_DETAILS.md not found"
          
          # Create metadata
          echo "last_updated: $(date -u +%Y-%m-%d)" > deploy/last_updated.txt
      
      - name: Clone brt-view repository
        env:
          GH_TOKEN: ${{ secrets.BRT_VIEW_PAT }}
        run: |
          git config --global user.name "Dashboard Bot"
          git config --global user.email "dashboard-bot@brt-rj.github.io"
          git clone https://x-access-token:${GH_TOKEN}@github.com/brt-rj/brt-view.git
      
      - name: Update project in brt-view
        run: |
          # CHANGE THIS: Replace 'your-project-slug' with your actual project slug
          PROJECT_SLUG="your-project-slug"
          PROJECT_DIR="brt-view/projects/${PROJECT_SLUG}"
          
          mkdir -p "$PROJECT_DIR"
          
          # Copy dashboard files
          # cp -r deploy/* "$PROJECT_DIR/"
          
          # Copy project details
          cp deploy/PROJECT_DETAILS.md "$PROJECT_DIR/" || true
          
          # Update timestamp
          cp deploy/last_updated.txt "$PROJECT_DIR/" || true
      
      - name: Commit and push changes
        env:
          GH_TOKEN: ${{ secrets.BRT_VIEW_PAT }}
        run: |
          cd brt-view
          
          git add projects/
          
          if git diff --staged --quiet; then
            echo "No changes to commit"
          else
            git commit -m "Update PROJECT_SLUG dashboard [automated]"
            git push https://x-access-token:${GH_TOKEN}@github.com/brt-rj/brt-view.git main
            echo "Dashboard updated successfully!"
          fi
```

### Step 4: Customize the Workflow

**Important**: Update the following in the workflow:

1. **`PROJECT_SLUG`**: Change `your-project-slug` to match your project's slug in `_data/projects.yml`
2. **Build step**: Uncomment and adjust the build commands for your dashboard type
3. **Copy commands**: Update paths to match your project structure

## 📊 Dashboard Type-Specific Instructions

### Streamlit

```bash
# Install dependencies
pip install streamlit

# For static export (if supported):
# Use stlite or streamlit-static-export
# Or host on Streamlit Cloud and use iframe

# Update index.md front matter:
dashboard_iframe: true
dashboard_url: "https://your-streamlit-app.streamlit.app"
```

### Evidence

```bash
# Build Evidence dashboard
npm install
npm run build

# Copy build output
cp -r build/* deploy/
```

### Looker Studio / Superset / Rill

For iframe-based dashboards:

1. Get the embed URL from your dashboard platform
2. Update your project's `index.md` with:

```yaml
---
dashboard_iframe: true
dashboard_url: "https://your-dashboard-url.com/embed/..."
---
```

3. No file copying needed - just push the updated `index.md`

## 📝 Adding a New Project

### Method 1: Manual Setup

1. **Fork this repository** (or ask for collaborator access)

2. **Create project directory**:
   ```bash
   mkdir -p projects/your-project-slug
   ```

3. **Copy template files**:
   ```bash
   cp -r templates/project-template/* projects/your-project-slug/
   ```

4. **Update `_data/projects.yml`**:
   ```yaml
   - slug: your-project-slug
     name: "Your Project Name"
     description: "Brief project description"
     dashboard_type: "streamlit"  # or evidence, looker, rill, superset
     dashboard_url: ""
     github_url: "https://github.com/brt-rj/your-repo"
     status: active
   ```

5. **Customize project files**:
   - Edit `projects/your-project-slug/index.md` with your project details
   - Add dashboard files to the directory
   - Update `PROJECT_DETAILS.md`

6. **Submit a Pull Request**

### Method 2: Request Collaborator Access

Contact the repository maintainer to request direct push access. This allows your automated workflow to push directly without PRs.

## 🔄 Updating Your Dashboard

Once set up, updates are automatic:

1. **Push changes** to your private repo (to `dashboard/**` or `PROJECT_DETAILS.md`)
2. **GitHub Actions** automatically triggers
3. **Dashboard deploys** to brt-view
4. **GitHub Pages** rebuilds and publishes (usually within 2-3 minutes)

### Manual Trigger

You can also manually trigger deployment:

1. Go to your private repo → Actions tab
2. Select "Deploy Dashboard to brt-view" workflow
3. Click "Run workflow"

## 📋 Project Structure Requirements

Your project in `brt-view` should have:

```
projects/your-project-slug/
├── index.md              # Required: Project page (uses front matter)
├── dashboard.html        # Optional: Static dashboard or iframe embed
├── PROJECT_DETAILS.md    # Required: Full project documentation
└── last_updated.txt      # Auto-generated: Last update timestamp
```

### `index.md` Front Matter Example

```yaml
---
layout: project
title: "Your Project Name"
description: "Brief description"
dashboard_type: "streamlit"
dashboard_iframe: true
dashboard_url: "https://your-dashboard.com"
dashboard_static: false
github_url: "https://github.com/brt-rj/your-repo"
status: active
---

# Project Overview

Your project details here (or include from PROJECT_DETAILS.md)...
```

## 🆘 Troubleshooting

### Issue: Workflow fails with "Permission denied"

- Verify your PAT has "Contents: Read and write" permission
- Check that the token hasn't expired
- Ensure the secret name matches (`BRT_VIEW_PAT`)

### Issue: Dashboard not showing up

- Check that `_data/projects.yml` includes your project
- Verify the `slug` matches your directory name exactly
- Clear browser cache and check again after 5 minutes

### Issue: Build fails

- Check the workflow logs in your private repo's Actions tab
- Verify your build commands are correct for your dashboard type
- Test the build locally first

## 📞 Support

For questions or issues:

1. Check existing project workflows in this repository
2. Review the [implementation plan](docs/implementation-plan.md)
3. Open an issue in this repository
4. Contact the repository maintainer

## ✅ Checklist for New Projects

- [ ] Created fine-grained PAT with correct permissions
- [ ] Added PAT as `BRT_VIEW_PAT` secret in private repo
- [ ] Created `.github/workflows/deploy-dashboard.yml` in private repo
- [ ] Updated `PROJECT_SLUG` in workflow
- [ ] Customized build steps for dashboard type
- [ ] Added project to `_data/projects.yml` (via PR or direct push)
- [ ] Created project directory with `index.md`
- [ ] Tested workflow with manual trigger
- [ ] Verified dashboard appears on live site

---

**Happy Dashboard Building! 📊**
