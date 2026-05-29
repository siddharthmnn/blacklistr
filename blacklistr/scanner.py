import ipaddress
import re
from urllib.parse import urlparse


SUSPICIOUS_TLDS = {
    "xyz", "top", "click", "info", "work", "zip", "quest", "icu", "tk", "pw"
}


def classify_target(target: str) -> str:
    target = target.strip()

    if target.startswith(("http://", "https://")):
        return "url"

    if is_ip(target):
        return "ip"

    if is_domain(target):
        return "domain"

    return "unknown"


def is_ip(value: str) -> bool:
    try:
        ipaddress.ip_address(value)
        return True
    except ValueError:
        return False


def is_domain(value: str) -> bool:
    value = value.lower().strip()

    if "/" in value or " " in value:
        return False

    # basic domain pattern: example.com, sub.example.com
    domain_pattern = r"^(?:[a-z0-9-]+\.)+[a-z]{2,}$"
    if not re.match(domain_pattern, value):
        return False

    tld = value.split(".")[-1]
    if tld in SUSPICIOUS_TLDS:
        return True

    return True


def normalize_url(target: str) -> str:
    if target.startswith(("http://", "https://")):
        return target
    return "http://" + target


def parse_url(target: str) -> dict:
    url = normalize_url(target)
    parsed = urlparse(url)

    return {
        "scheme": parsed.scheme,
        "netloc": parsed.netloc,
        "path": parsed.path,
        "query": parsed.query,
        "hostname": parsed.hostname,
    }
