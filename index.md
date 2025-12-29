---
layout: default
title: Home
---

# BRT Dashboard Hub

Welcome to the centralized dashboard hosting platform for BRT research projects. This platform hosts interactive dashboards and comprehensive documentation for ongoing sustainability and technology research initiatives.

## Featured Projects

<div class="projects-grid">
{% for project_data in site.data.projects %}
  <div class="project-card">
    <h3>
      <a href="{{ site.baseurl }}/projects/{{ project_data.slug }}/">
        {{ project_data.name }}
      </a>
    </h3>
    <p class="project-description">{{ project_data.description }}</p>
    <div class="project-meta">
      <span class="badge badge-{{ project_data.dashboard_type }}">{{ project_data.dashboard_type }}</span>
      <span class="status status-{{ project_data.status }}">{{ project_data.status }}</span>
    </div>
    <div class="project-links">
      <a href="{{ site.baseurl }}/projects/{{ project_data.slug }}/" class="btn btn-primary">View Dashboard</a>
      {% if project_data.github_url %}
      <a href="{{ project_data.github_url }}" class="btn btn-secondary" target="_blank">GitHub</a>
      {% endif %}
    </div>
  </div>
{% endfor %}
</div>

## About

This platform supports multiple dashboard types:
- **Evidence** - Data-driven reporting
- **Looker Studio** - Google's business intelligence platform
- **Streamlit** - Python-based data apps
- **Rill** - Fast, interactive analytics
- **Apache Superset** - Modern data exploration

## Contributing

Project teams can push their dashboards and documentation to this platform. See our [Contributing Guide]({{ site.baseurl }}/CONTRIBUTING.html) for details on integrating your project.

---

*Last updated: {{ site.time | date: '%B %d, %Y' }}*
