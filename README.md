# Blacklistr

CLI-based cybersecurity threat triage toolkit for analyzing suspicious URLs, domains, IP addresses, and investigation notes.

Blacklistr was built as a cybersecurity learning project to simulate basic analyst workflows. It performs lightweight risk analysis, extracts indicators of compromise (IOCs), stores investigation cases, and generates reports.

## Features

- URL, domain, and IP classification
- Suspicious keyword detection
- Risk scoring engine
- IOC extraction from notes and logs
- JSON case storage
- Markdown report generation
- Fully offline operation
- Simple command-line interface

## Example Usage

### Analyze a URL

```bash
python3 -m blacklistr.main scan https://paypal-login-secure-update.xyz
Extract Indicators
python3 -m blacklistr.main extract samples/sample_notes.txt
Workflow
Input
  ↓
Classification
  ↓
Risk Analysis
  ↓
IOC Extraction
  ↓
Case Storage
  ↓
Report Generation
Why I Built It

While learning cybersecurity, I wanted a simple tool that could help triage suspicious indicators without relying on multiple websites or services. Blacklistr combines several basic analyst tasks into a single workflow and serves as a practical learning project.

Future Improvements
WHOIS enrichment
Passive DNS lookups
Threat intelligence integrations
VirusTotal integration
Case history command
Improved domain analysis
License

MIT License
