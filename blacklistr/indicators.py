import re


URL_PATTERN = r'https?://[^\s]+'
IP_PATTERN = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
EMAIL_PATTERN = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
DOMAIN_PATTERN = r'\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b'


def extract_indicators(text):
    urls = re.findall(URL_PATTERN, text)
    ips = re.findall(IP_PATTERN, text)
    emails = re.findall(EMAIL_PATTERN, text)
    domains = re.findall(DOMAIN_PATTERN, text)

    return {
        "urls": sorted(set(urls)),
        "ips": sorted(set(ips)),
        "emails": sorted(set(emails)),
        "domains": sorted(set(domains)),
    }
