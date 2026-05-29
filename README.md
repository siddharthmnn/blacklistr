# Blacklistr

CLI-based cybersecurity threat triage toolkit for analyzing suspicious URLs, domains, IP addresses, and investigation notes.

Blacklistr was built as a cybersecurity learning project to simulate basic analyst workflows. It performs lightweight risk analysis, extracts indicators of compromise (IOCs), stores investigation cases, and generates reports.

---

## Features

* URL, domain, and IP classification
* Suspicious keyword detection
* Risk scoring engine
* IOC extraction from notes and logs
* JSON case storage
* Markdown report generation
* Fully offline operation
* Simple command-line interface

---

## Screenshots

### URL Analysis

![Scan Output](screenshots/scan.png)

### IOC Extraction

![IOC Extraction](screenshots/extract.png)

---

## Example Usage

### Analyze a URL

```bash
python3 -m blacklistr.main scan https://paypal-login-secure-update.xyz
```

### Extract Indicators from Notes

```bash
python3 -m blacklistr.main extract samples/sample_notes.txt
```

---

## Example Output

```text
=== BLACKLISTR REPORT ===

Target   : https://paypal-login-secure-update.xyz
Type     : url
Host     : paypal-login-secure-update.xyz

Risk Score : 60/100
Severity   : MEDIUM

Reasons:
 - Suspicious keyword: login
 - Suspicious keyword: secure
 - Suspicious keyword: update
 - Suspicious keyword: paypal
```

---

## Workflow

```text
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
```

---

## Project Structure

```text
blacklistr/
├── blacklistr/
│   ├── main.py
│   ├── scanner.py
│   ├── scoring.py
│   ├── indicators.py
│   ├── storage.py
│   └── reporter.py
├── cases/
├── reports/
├── samples/
├── screenshots/
└── README.md
```

---

## Why I Built It

While learning cybersecurity, I often found myself manually checking suspicious URLs, domains, and indicators across multiple tools.

Blacklistr started as a way to combine several small investigation tasks into a single workflow while helping me better understand how threat triage works. The goal was not to replace professional security tools, but to build something practical that I could use, improve, and explain in interviews.

---

## Future Improvements

* WHOIS enrichment
* Passive DNS lookups
* Threat intelligence feed integration
* VirusTotal integration
* Improved domain reputation analysis
* Log ingestion support
* Case history command
* Export reports in multiple formats

---

## License

MIT License
