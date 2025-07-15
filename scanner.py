
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_all_forms(url):
    """Returns all form tags from a URL."""
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    """Extracts form details like action, method, and inputs."""
    details = {}
    action = form.attrs.get("action", "").strip()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        if input_name:
            inputs.append({"type": input_type, "name": input_name})
    details['action'] = action
    details['method'] = method
    details['inputs'] = inputs
    return details

def submit_form(form_details, url, payload):
    """Submits a form with a given payload and returns the response."""
    target_url = urljoin(url, form_details["action"])
    data = {}

    for input in form_details["inputs"]:
        if input["type"] != "submit":
            data[input["name"]] = payload

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    return requests.get(target_url, params=data)

def scan_xss(url, payloads):
    """Scans for XSS vulnerabilities and returns a list of findings."""
    findings = []
    forms = get_all_forms(url)

    for form in forms:
        form_details = get_form_details(form)
        for payload in payloads:
            response = submit_form(form_details, url, payload)
            if payload in response.text:
                findings.append({
                    "type": "XSS",
                    "url": url,
                    "payload": payload,
                    "evidence": payload,
                    "severity": "High"
                })
    return findings

def scan_sqli(url, payloads):
    """Scans for SQL Injection vulnerabilities and returns a list of findings."""
    findings = []
    forms = get_all_forms(url)

    for form in forms:
        form_details = get_form_details(form)
        for payload in payloads:
            response = submit_form(form_details, url, payload)
            errors = ["you have an error in your sql syntax", "sql syntax", "mysql_fetch", "syntax error"]
            for error in errors:
                if error.lower() in response.text.lower():
                    findings.append({
                        "type": "SQL Injection",
                        "url": url,
                        "payload": payload,
                        "evidence": error,
                        "severity": "High"
                    })
    return findings

def scan_csrf(url):
    """Scans for missing anti-CSRF tokens in POST forms."""
    findings = []
    forms = get_all_forms(url)

    for form in forms:
        form_details = get_form_details(form)
        if form_details["method"] == "post":
            has_token = False
            for input in form_details["inputs"]:
                name = input["name"].lower() if input["name"] else ""
                # Common CSRF token names
                if "csrf" in name or "token" in name or "authenticity_token" in name:
                    has_token = True
                    break
            if not has_token:
                findings.append({
                    "type": "CSRF",
                    "url": url,
                    "payload": None,
                    "evidence": "POST form with no CSRF token",
                    "severity": "Medium"
                })
    return findings
