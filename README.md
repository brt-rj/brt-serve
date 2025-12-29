# BRT Dashboard Hub

Centralized dashboard hosting platform for BRT research projects focused on sustainability, technology, and environmental impact.

## 🎯 Purpose

This repository serves as a unified platform to host interactive dashboards and comprehensive documentation for ongoing research initiatives. It supports multiple dashboard technologies including:

- **Evidence** - Data-driven reporting
- **Looker Studio** - Google's business intelligence platform  
- **Streamlit** - Python-based data apps
- **Rill** - Fast, interactive analytics
- **Apache Superset** - Modern data exploration

## 📊 Hosted Projects

This platform currently hosts dashboards for the following projects:

1. **[No Flab Brief](projects/no-flab-brief/)** - Concise, fact-checked news aggregation and analysis
2. **[Sub-Interceptor](projects/sub-interceptor/)** - Sustainable submarine cable monitoring
3. **[Mari](projects/mari/)** - Maritime resource intelligence and tracking
4. **[Scope2Emission](projects/scope2emission/)** - Scope 2 emissions tracking and analysis
5. **[Con-Eco](projects/con-eco/)** - Construction ecology and sustainability assessment
6. **[NVCM](projects/nvcm/)** - Natural Voluntary Carbon Market analysis
7. **[RAP-Scout](projects/rap-scout/)** - Renewable energy project assessment
8. **[GreenOps-Sidecar](projects/greenops-sidecar/)** - Green operations monitoring
9. **[HypeCheck](projects/hypecheck/)** - Technology hype cycle validation
10. **[Unified EcoRisk Engine](projects/unified-ecorisk-engine/)** - Ecological risk assessment
11. **[OpenSustain AI Engine](projects/opensustain-ai-engine/)** - AI-powered sustainability analysis

## 🚀 Quick Start

### Viewing Dashboards

Visit the [live site](https://brt-rj.github.io/brt-view/) to explore all dashboards, or navigate directly to project pages using the links above.

### Local Development

```bash
# Install dependencies
bundle install

# Serve locally
bundle exec jekyll serve

# Build for production
bundle exec jekyll build
```

The site will be available at `http://localhost:4000/brt-view/`

## 🤝 Contributing

Project teams can push their dashboards and documentation to this platform. See our **[Contributing Guide](CONTRIBUTING.md)** for detailed instructions on:

- Setting up automated deployment from private repositories
- Configuring Personal Access Tokens (PAT)
- Adding new projects
- Updating dashboards and documentation

## 📁 Repository Structure

```
brt-view/
├── _config.yml              # Jekyll configuration
├── _data/
│   └── projects.yml         # Central project registry
├── _layouts/
│   ├── default.html         # Base layout
│   └── project.html         # Project page layout
├── assets/
│   └── css/
│       └── style.css        # Site styling
├── projects/
│   ├── no-flab-brief/       # Example project
│   │   ├── index.md         # Project page
│   │   ├── dashboard.html   # Dashboard embed/static
│   │   └── PROJECT_DETAILS.md
│   └── ...                  # Other projects
├── templates/               # Templates for new projects
└── docs/                    # Additional documentation
```

## 🔧 Technology Stack

- **Jekyll** - Static site generator
- **GitHub Pages** - Hosting platform
- **GitHub Actions** - CI/CD automation
- **Markdown** - Content authoring

## 📝 License

This repository is maintained by BRT Research. Individual projects may have their own licenses - please refer to their respective repositories.

## 🔗 Links

- [Live Dashboard Hub](https://brt-rj.github.io/brt-view/)
- [BRT GitHub Organization](https://github.com/brt-rj)
- [Contributing Guide](CONTRIBUTING.md)

---

**Last Updated:** December 2025
