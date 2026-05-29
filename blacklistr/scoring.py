from urllib.parse import urlparse
import ipaddress


SUSPICIOUS_KEYWORDS = [
    "login",
    "verify",
    "secure",
    "update",
    "password",
    "bank",
    "paypal",
    "wallet",
    "signin",
    "account",
]


def calculate_risk(target: str):
    score = 0
    reasons = []

    lower_target = target.lower()

    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in lower_target:
            score += 15
            reasons.append(f"Suspicious keyword: {keyword}")

    if target.startswith(("http://", "https://")):

        parsed = urlparse(target)
        host = parsed.hostname or ""

        host_is_ip = False

        try:
            ipaddress.ip_address(host)
            host_is_ip = True

            score += 25
            reasons.append("URL uses raw IP address")

        except ValueError:
            pass

        if not host_is_ip:
            if host.count(".") >= 3:
                score += 15
                reasons.append("Excessive subdomains")

        if len(target) > 75:
            score += 10
            reasons.append("Unusually long URL")

        shorteners = [
            "bit.ly",
            "tinyurl.com",
            "t.co",
            "goo.gl",
        ]

        if host in shorteners:
            score += 20
            reasons.append("URL shortener detected")

    score = min(score, 100)

    if score >= 70:
        severity = "HIGH"
    elif score >= 40:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    return {
        "score": score,
        "severity": severity,
        "reasons": reasons,
    }
