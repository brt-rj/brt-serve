---
layout: project
title: "No Flab Brief"
description: "Concise, fact-checked news aggregation and analysis platform"
dashboard_type: "superset"
dashboard_iframe: true
dashboard_url: ""  # To be updated when dashboard is deployed
dashboard_static: false
github_url: "https://github.com/brt-rj/no-flab-brief"
status: active
last_updated: "2025-12-29"
---

# No Flab Brief

## Overview

No Flab Brief is an intelligent news aggregation and analysis platform that delivers concise, fact-checked news from multiple sources. The platform combines RSS feeds, GDELT data, social media monitoring, and professional journalism databases to provide comprehensive coverage across multiple beats and regions.

## Key Features

- **Multi-Source Aggregation**: Combines RSS feeds, GDELT, Hacker News, NewsData.io, and social media
- **Fact-Checking Integration**: Automatic verification using certified fact-checker feeds
- **Journalist Database**: Curated database of 320+ journalists across various beats and political leanings
- **Daily Curation**: Targeted daily volume of 100 articles (40 politics, 60 other beats)
- **Excel Outputs**: Separate files for RSS feeds and API sources with insert/update logic
- **Superset Dashboard**: Interactive analytics and visualization of news trends

## Methodology

### Data Collection

1. **RSS Feeds**: Aggregation from curated sources in `Source.md`
2. **GDELT Integration**: Top news based on Goldstein Scale and NumMentions rankings
3. **Social Media**: Twitter monitoring via Nitter for journalist handles
4. **YouTube**: Channel-specific RSS feeds for video content
5. **Fact-Checking**: Integration with certified fact-checker feeds

### Analysis Approach

- **Multi-Agent Reflexion (MAR)**: "Diligent Author" and "Ruthless Editor" personas
- **GDELT Ranking**: Based on Goldstein Scale and mention frequency
- **Verification Mechanism**: Cross-referencing with fact-checking databases
- **Objective Journalism Standards**: Comprehensive editorial checklist

### Data Storage

- **Archive.org Integration**: Long-term article preservation
- **Incremental Updates**: Insert/update logic to append new articles
- **Deduplication**: Automated script to prevent duplicate content
- **Schema Validation**: `article-schema.json` with CI validation

## Technology Stack

- **Python**: Data aggregation and processing
- **Apache Airflow**: Daily scheduling and automation
- **Apache Superset**: Dashboard and analytics
- **GitHub Actions**: CI/CD pipeline
- **Slack**: Deployment notifications

## Data Governance

### Retention Policy
- Raw HTML replaced with Archive.org links
- Metadata retained indefinitely
- Compliance with robots.txt directives

### Privacy
- No personal data collection
- Public sources only
- Transparent sourcing

## Dashboard Components

The Superset dashboard provides:

1. **Source Distribution**: Breakdown by news source and type
2. **Beat Coverage**: Articles by topic area (politics, technology, environment, etc.)
3. **Temporal Trends**: Article volume over time
4. **Fact-Check Status**: Verification status of articles
5. **Journalist Insights**: Coverage by journalist and publication

## Workflow

1. **Ingestion**: Automated daily collection (Airflow job)
2. **Processing**: Deduplication, classification, and ranking
3. **Verification**: Fact-checking and journalist verification
4. **Curation**: MAR-based editorial process
5. **Publication**: Excel exports and dashboard updates
6. **Archival**: Archive.org integration for long-term storage

## Future Development

- **Real-time Updates**: Move from daily to hourly ingestion
- **ML Classification**: Automated beat categorization
- **Sentiment Analysis**: Article tone and bias detection
- **API**: Public API for programmatic access
- **Mobile App**: Native mobile applications

## Contact

For questions or collaboration opportunities, please visit our [GitHub repository](https://github.com/brt-rj/no-flab-brief).

---

*This project is part of the BRT Research initiative focused on information integrity and media analysis.*
