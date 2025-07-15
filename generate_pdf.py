from xhtml2pdf import pisa
from flask import render_template
from utils.pdf_report import count_vulns
import os

def generate_pdf_from_results(results, output_path="report.pdf"):     
    counts = count_vulns(results)  
    html = render_template("pdf_template.html", results=results, counts=counts)


    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        with open(output_path, "w+b") as pdf_file:
            pisa_status = pisa.CreatePDF(html, dest=pdf_file)
        return pisa_status.err == 0
    except Exception as e:
        print(f"[ERROR] Failed to create PDF: {e}")
        return False
