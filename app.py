
from flask import Flask, render_template, request, send_file
from payloads import XSS_PAYLOADS, SQLI_PAYLOADS
import json
import os
from scanner import scan_xss, scan_sqli, scan_csrf
from generate_pdf import generate_pdf_from_results
from utils.pdf_report import create_pdf_report

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            xss_results = scan_xss(url, XSS_PAYLOADS)
            csrf_results = scan_csrf(url)
            sqli_results = scan_sqli(url, SQLI_PAYLOADS)
            results = xss_results + sqli_results + csrf_results
            with open("report.json", "w") as f:
                json.dump(results, f, indent=4)
    return render_template("index.html", results=results)

@app.route("/generate_pdf")
def generate_pdf():
    scan_results = [
        {"type": "XSS", "url": "http://example.com", "payload": "<script>", "evidence": "found", "severity": "High"},
        {"type": "SQLi", "url": "http://example.com?id=1'", "payload": "' OR 1=1 --", "evidence": "SQL error", "severity": "Medium"},
    ]
    create_pdf_report(scan_results)
    return "PDF generated!"

@app.route("/download-report")
def download_report():
    with open("report.json") as f:
        results = json.load(f)

    pdf_path = os.path.join(os.getcwd(), "report.pdf")
    pdf_created = generate_pdf_from_results(results, pdf_path)

    if pdf_created and os.path.exists(pdf_path):
        return send_file(pdf_path, as_attachment=True)
    return "Failed to generate PDF", 500

if __name__ == "__main__":
    app.run(debug=True)
