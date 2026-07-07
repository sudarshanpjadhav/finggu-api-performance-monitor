# API Performance Monitor

## Overview
This project provides real-time monitoring and analysis of API performance metrics.

## Features
- Dashboard for real-time performance metrics
- Automated alerting for performance degradation
- Detailed API call logs and trends analysis
- Integration with popular CI/CD tools for seamless deployment

## Installation
1. Clone the repository.
2. Set up your environment variables for database and email configuration.
3. Run `docker build -t finggu-api-performance-monitor .`
4. Run `docker run -p 5000:5000 finggu-api-performance-monitor`

## Usage
Access the dashboard at `http://localhost:5000`.