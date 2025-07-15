# WeScan – Vulnerability Scanner

## Project Title  
**WeScan: A Lightweight Web Application Vulnerability Scanner**

## Objective  
To develop a Python-based tool that scans web applications for common security vulnerabilities, including Cross-Site Scripting (XSS), SQL Injection (SQLi), and Cross-Site Request Forgery (CSRF). The goal is to identify exploitable weaknesses and present the results through an intuitive web interface and downloadable PDF reports.

## Detected Vulnerabilities

| Vulnerability | Description |
|---------------|-------------|
| XSS           | Scans input fields for reflected or stored script injections by submitting test payloads and observing output for unescaped content. |
| SQLi          | Attempts SQL payloads through query parameters and form inputs to test for unsafe database interactions. |
| CSRF          | Analyzes POST requests for the presence or absence of CSRF tokens, flagging endpoints that lack proper protection mechanisms. |

## Tools and Technologies

| Component        | Technology Used           |
|------------------|---------------------------|
| Programming      | Python                    |
| Web Framework    | Flask                     |
| HTTP Requests    | requests, BeautifulSoup   |
| PDF Generation   | xhtml2pdf                 |
| Frontend         | HTML, CSS (custom-built)  |
| UI Features      | Loading indicator, clean layout |

## How It Works

1. **Input** – User provides a target URL through the Flask web interface.
2. **Crawling** – The scanner extracts all accessible forms and input fields using BeautifulSoup.
3. **Injection** – Common payloads for XSS and SQLi are submitted to inputs and observed for vulnerability signatures in the response.
4. **CSRF Detection** – POST forms are evaluated to check for token presence and validation mechanisms.
5. **Result Display** – Vulnerabilities are displayed on-screen and can be downloaded as a styled PDF report.
6. **Summary** – Each report includes vulnerability counts, endpoint information, and evidence of issues found.

## Project Directory Structure

Vuln Scanner/
```
│
├── app.py # Main Flask app
├── scanner.py # Scanning logic
├── csrf.py # CSRF-specific checks
├── generate_pdf.py # PDF rendering script
│
├── templates/
│ ├── index.html # Main UI
│ ├── pdf_template.html # Template for PDF generation
│
├── static/
│ ├── styles.css # Custom stylesheet
│ └── loader.css # CSS for loading animation
│
├── requirements.txt # Python dependencies
├── Procfile # For deployment configuration
```
 
## Features

- Detection of three major vulnerability types: XSS, SQLi, and CSRF.
- Simple and responsive user interface without third-party libraries like Bootstrap.
- Inline vulnerability evidence shown in real-time.
- PDF report generation with structured summaries.
- Modular architecture for easy maintenance and expansion.

## Sample Report Summary

Summary of Findings:

XSS Vulnerabilities: 2

Found in login and search fields.
SQL Injection: 1

Detected in contact form endpoint.
CSRF: 1

Settings page form lacks CSRF token validation.


Each result includes:
- The specific endpoint URL
- Type of vulnerability detected
- Severity indication
- Sample payload or affected response snippet

## Learning Outcomes

- Gained practical experience in identifying and simulating web vulnerabilities.
- Developed a modular Flask application from backend to frontend.
- Learned PDF rendering with HTML and custom CSS styling.
- Understood principles of web security based on OWASP Top 10.
- Explored deployment on platforms like Railway and encountered real-world constraints.

## Future Improvements
 
- Support for additional vulnerabilities such as open redirects, IDOR, or clickjacking.
- Database integration for saving historical scan results.
- Authentication support and session management.
- Improved UI/UX with detailed logging and request tracing.
- Containerization for scalable deployment.


