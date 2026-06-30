from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import io

def generate_invoice_pdf(invoice_data: dict) -> io.BytesIO:
   
    buffer = io.BytesIO()
    
    p = canvas.Canvas(buffer, pagesize=A4)
    p.setFont("Helvetica-Bold", 20)
    p.drawString(50, 800, "SmartERP TAX INVOICE")
    
    p.setFont("Helvetica", 12)
    p.drawString(50, 760, f"Invoice Number: {invoice_data.get('invoice_number')}")
    p.drawString(50, 740, f"Customer: {invoice_data.get('customer_name')}")
    p.drawString(50, 720, f"Total Amount: INR {invoice_data.get('total_amount')}")
    
    p.showPage()
    p.save()
    
    buffer.seek(0)
    return buffer