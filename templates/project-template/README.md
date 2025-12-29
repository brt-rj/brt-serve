# Project Template

This directory contains template files for adding new projects to the BRT Dashboard Hub.

## Files

- **`index.md.template`**: Main project page with front matter configuration
- **`PROJECT_DETAILS.md.template`**: Comprehensive project documentation template
- **`metadata.yml.template`**: Project metadata configuration
- **`dashboard.html.template`**: Placeholder for static dashboard content

## Usage

1. Copy all template files to a new project directory:
   ```bash
   cp -r templates/project-template/* projects/your-project-slug/
   ```

2. Rename files by removing `.template` extension:
   ```bash
   cd projects/your-project-slug/
   mv index.md.template index.md
   mv PROJECT_DETAILS.md.template PROJECT_DETAILS.md
   mv metadata.yml.template metadata.yml
   mv dashboard.html.template dashboard.html
   ```

3. Update placeholders in all files:
   - Replace `PROJECT_NAME` with your project name
   - Replace `YOUR_REPO` with your repository name
   - Replace `project-slug` with your URL-friendly project identifier
   - Fill in all required metadata fields

4. Add your project to `_data/projects.yml`:
   ```yaml
   - slug: your-project-slug
     name: "Your Project Name"
     # ... other fields
   ```

5. Commit and push your changes

## Dashboard Types

Choose the appropriate dashboard configuration:

### Iframe Embed (Recommended for hosted dashboards)
- Set `dashboard_iframe: true` in `index.md`
- Provide `dashboard_url` with the embed URL
- Delete or ignore `dashboard.html`

### Static HTML (For self-hosted dashboards)
- Set `dashboard_static: true` in `index.md`- Place your built dashboard files in the project directory
- Reference them in `dashboard.html`

## See Also

- [Contributing Guide](../../CONTRIBUTING.md)
- [Main README](../../README.md)
