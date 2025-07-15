from flask import render_template
from xhtml2pdf import pisa
from datetime import datetime


def count_vulns(results):
    counts = {"xss": 0, "sqli": 0, "csrf": 0}
    for r in results:
        key = r["type"].lower()
        if key in counts:
            counts[key] += 1
    return counts

def create_pdf_report(results, output_path="report.pdf"):
    with open("static/pdf_styles.css", "r") as f:
        css = f.read()

    html = render_template(
        "pdf_template.html",
        results=results,
        counts=count_vulns(results),
        pdf_css=css,
        now=datetime.now()  # Pass the current datetime
    )

    with open(output_path, "w+b") as f:
        pisa.CreatePDF(html, dest=f)
