#!/bin/bash

# Add New Project Script
# Usage: ./scripts/add-project.sh <project-slug> <project-name>

set -e

if [ $# -lt 2 ]; then
    echo "Usage: $0 <project-slug> <project-name>"
    echo "Example: $0 my-project \"My Awesome Project\""
    exit 1
fi

PROJECT_SLUG=$1
PROJECT_NAME=$2
PROJECT_DIR="projects/$PROJECT_SLUG"

echo "🚀 Adding new project: $PROJECT_NAME"
echo "   Slug: $PROJECT_SLUG"
echo ""

# Check if project already exists
if [ -d "$PROJECT_DIR" ]; then
    echo "❌ Error: Project directory already exists: $PROJECT_DIR"
    exit 1
fi

# Create project directory
echo "📁 Creating project directory..."
mkdir -p "$PROJECT_DIR"

# Copy template files
echo "📋 Copying template files..."
cp templates/project-template/index.md.template "$PROJECT_DIR/index.md"
cp templates/project-template/PROJECT_DETAILS.md.template "$PROJECT_DIR/PROJECT_DETAILS.md"
cp templates/project-template/dashboard.html.template "$PROJECT_DIR/dashboard.html"

# Replace placeholders in index.md
echo "✏️  Updating placeholders..."
sed -i.bak "s/PROJECT_NAME/$PROJECT_NAME/g" "$PROJECT_DIR/index.md"
sed -i.bak "s/YOUR_REPO/$PROJECT_SLUG/g" "$PROJECT_DIR/index.md"
rm "$PROJECT_DIR/index.md.bak"

# Replace placeholders in PROJECT_DETAILS.md
sed -i.bak "s/PROJECT_NAME/$PROJECT_NAME/g" "$PROJECT_DIR/PROJECT_DETAILS.md"
sed -i.bak "s/YOUR_REPO/$PROJECT_SLUG/g" "$PROJECT_DIR/PROJECT_DETAILS.md"
rm "$PROJECT_DIR/PROJECT_DETAILS.md.bak"

# Print next steps
echo ""
echo "✅ Project directory created successfully!"
echo ""
echo "📝 Next steps:"
echo "1. Edit $PROJECT_DIR/index.md and fill in project details"
echo "2. Edit $PROJECT_DIR/PROJECT_DETAILS.md with comprehensive documentation"
echo "3. Add your project to _data/projects.yml:"
echo ""
echo "   - slug: $PROJECT_SLUG"
echo "     name: \"$PROJECT_NAME\""
echo "     description: \"Brief project description\""
echo "     dashboard_type: \"\"  # evidence, looker, streamlit, rill, superset"
echo "     dashboard_url: \"\""
echo "     github_url: \"https://github.com/brt-rj/$PROJECT_SLUG\""
echo "     status: active"
echo ""
echo "4. Configure your dashboard (iframe or static)"
echo "5. Commit and push your changes"
echo ""
echo "📚 See CONTRIBUTING.md for detailed setup instructions"
