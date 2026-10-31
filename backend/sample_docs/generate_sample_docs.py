import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def create_synthetic_docs():
    output_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(output_dir, exist_ok=True)
    
    styles = getSampleStyleSheet()
    
    # Custom Styles
    header_style = ParagraphStyle(
        'GovHeader',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        alignment=1, # Center
        textColor=colors.HexColor('#002147')
    )
    sub_header_style = ParagraphStyle(
        'GovSubHeader',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        alignment=1,
        textColor=colors.HexColor('#333333')
    )
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        alignment=1,
        textColor=colors.HexColor('#8B0000')
    )
    body_style = ParagraphStyle(
        'DocBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#1f2937')
    )
    disclaimer_style = ParagraphStyle(
        'Disclaimer',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        alignment=1,
        textColor=colors.HexColor('#dc2626')
    )
    
    # ==========================================
    # 1. DOCUMENT A: CORRECT EOA
    # ==========================================
    doc_a_path = os.path.join(output_dir, "Doc_A_Correct_EoA.pdf")
    doc_a = SimpleDocTemplate(doc_a_path, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
    story_a = []
    
    story_a.append(Paragraph("ALL INDIA COUNCIL FOR TECHNICAL EDUCATION", header_style))
    story_a.append(Paragraph("(A Statutory Body of the Government of India)", sub_header_style))
    story_a.append(Paragraph("Nelson Mandela Marg, Vasant Kunj, New Delhi - 110070", sub_header_style))
    story_a.append(Spacer(1, 6))
    story_a.append(Paragraph("*** SYNTHETIC DEMONSTRATION DOCUMENT — NOT A REAL APPROVAL LETTER ***", disclaimer_style))
    story_a.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#002147'), spaceAfter=8))
    
    story_a.append(Paragraph("<b>APPROVAL PROCESS 2026-27</b><br/><b>EXTENSION OF APPROVAL (EoA)</b>", title_style))
    story_a.append(Spacer(1, 6))
    
    meta_table_a = [
        [Paragraph("<b>Application ID:</b> APP-DEMO-001", body_style), Paragraph("<b>Permanent Institute ID:</b> 1-1234567890", body_style)],
        [Paragraph("<b>Academic Year:</b> 2026-27", body_style), Paragraph("<b>Date of Issue:</b> 15/06/2026", body_style)],
        [Paragraph("<b>Institution Name:</b> ABC Institute of Technology", body_style), Paragraph("<b>Approval Status:</b> Approved", body_style)],
        [Paragraph("<b>Address:</b> Sector 24, Pradhikaran, Pune, Maharashtra", body_style), Paragraph("<b>Affiliating Body:</b> Savitribai Phule Pune University", body_style)]
    ]
    t_meta_a = Table(meta_table_a, colWidths=[270, 270])
    t_meta_a.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story_a.append(t_meta_a)
    story_a.append(Spacer(1, 10))
    
    story_a.append(Paragraph("<b>Approved Programmes and Intake Summary:</b>", body_style))
    story_a.append(Spacer(1, 4))
    
    courses_a = [
        ["Sr.", "Programme", "Level", "Course Name", "Affiliating Body", "Approved Intake 2026-27"],
        ["1", "ENGINEERING AND TECHNOLOGY", "UG", "COMPUTER ENGINEERING", "Pune University", "120"],
        ["2", "ENGINEERING AND TECHNOLOGY", "UG", "ARTIFICIAL INTELLIGENCE AND DATA SCIENCE", "Pune University", "60"]
    ]
    t_courses_a = Table(courses_a, colWidths=[25, 150, 45, 180, 85, 55])
    t_courses_a.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#002147')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 8),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#94A3B8')),
        ('FONTSIZE', (0,1), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story_a.append(t_courses_a)
    story_a.append(Spacer(1, 12))
    
    story_a.append(Paragraph("<b>Terms & Conditions:</b><br/>"
                             "1. The institution shall adhere to all regulations, guidelines, and standards prescribed by AICTE.<br/>"
                             "2. Strict compliance with anti-ragging regulations, faculty cadre ratios, and barrier-free environment norms.<br/>"
                             "3. Security Certificate Verification Ref: <b>CERT-DEMO-101</b>.", body_style))
    story_a.append(Spacer(1, 25))
    story_a.append(Paragraph("<b>Member Secretary, AICTE (Digital Signature Verified)</b>", ParagraphStyle('Sign', parent=body_style, alignment=2)))
    doc_a.build(story_a)
    print(f"Generated Doc A: {doc_a_path}")

    # ==========================================
    # 2. DOCUMENT B: INCORRECT EOA (INTAKE MISMATCH & MISSING COURSE)
    # ==========================================
    doc_b_path = os.path.join(output_dir, "Doc_B_Incorrect_EoA.pdf")
    doc_b = SimpleDocTemplate(doc_b_path, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
    story_b = []
    story_b.append(Paragraph("ALL INDIA COUNCIL FOR TECHNICAL EDUCATION", header_style))
    story_b.append(Paragraph("(A Statutory Body of the Government of India)", sub_header_style))
    story_b.append(Spacer(1, 6))
    story_b.append(Paragraph("*** SYNTHETIC DEMONSTRATION DOCUMENT (TEST CASE B: INTAKE MISMATCH & MISSING AI&DS) ***", disclaimer_style))
    story_b.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#002147'), spaceAfter=8))
    story_b.append(Paragraph("<b>APPROVAL PROCESS 2026-27</b><br/><b>EXTENSION OF APPROVAL (EoA)</b>", title_style))
    story_b.append(Spacer(1, 6))
    
    meta_table_b = [
        [Paragraph("<b>Application ID:</b> APP-DEMO-001", body_style), Paragraph("<b>Permanent Institute ID:</b> 1-1234567890", body_style)],
        [Paragraph("<b>Academic Year:</b> 2026-27", body_style), Paragraph("<b>Date of Issue:</b> 15/06/2026", body_style)],
        [Paragraph("<b>Institution Name:</b> ABC Institute of Technology", body_style), Paragraph("<b>Approval Status:</b> Approved", body_style)],
        [Paragraph("<b>Address:</b> Sector 24, Pradhikaran, Pune, Maharashtra", body_style), Paragraph("<b>Affiliating Body:</b> Savitribai Phule Pune University", body_style)]
    ]
    t_meta_b = Table(meta_table_b, colWidths=[270, 270])
    t_meta_b.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FEF2F2')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#F87171')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#FECACA')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story_b.append(t_meta_b)
    story_b.append(Spacer(1, 10))
    story_b.append(Paragraph("<b>Approved Programmes and Intake Summary (Discrepancy Present):</b>", body_style))
    story_b.append(Spacer(1, 4))
    
    courses_b = [
        ["Sr.", "Programme", "Level", "Course Name", "Affiliating Body", "Approved Intake 2026-27"],
        ["1", "ENGINEERING AND TECHNOLOGY", "UG", "COMPUTER ENGINEERING", "Pune University", "180"] # Mismatch: 180 instead of 120, and AI&DS missing!
    ]
    t_courses_b = Table(courses_b, colWidths=[25, 150, 45, 180, 85, 55])
    t_courses_b.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#991B1B')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#F87171')),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
    ]))
    story_b.append(t_courses_b)
    story_b.append(Spacer(1, 12))
    story_b.append(Paragraph("<b>Notice of Discrepancy:</b> AI&DS Course missing and Computer Engineering intake listed as 180 instead of authorized 120.", body_style))
    story_b.append(Spacer(1, 20))
    story_b.append(Paragraph("<b>Member Secretary, AICTE</b>", ParagraphStyle('Sign', parent=body_style, alignment=2)))
    doc_b.build(story_b)
    print(f"Generated Doc B: {doc_b_path}")

    # ==========================================
    # 3. DOCUMENT C: INCOMPLETE EOA (MISSING IDS & INCOMPLETE SECTIONS)
    # ==========================================
    doc_c_path = os.path.join(output_dir, "Doc_C_Incomplete_EoA.pdf")
    doc_c = SimpleDocTemplate(doc_c_path, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
    story_c = []
    story_c.append(Paragraph("ALL INDIA COUNCIL FOR TECHNICAL EDUCATION", header_style))
    story_c.append(Spacer(1, 6))
    story_c.append(Paragraph("*** SYNTHETIC DEMONSTRATION DOCUMENT (TEST CASE C: INCOMPLETE / MISSING SECTIONS) ***", disclaimer_style))
    story_c.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#DC2626'), spaceAfter=8))
    story_c.append(Paragraph("<b>PROVISIONAL APPLICATION SUMMARY</b>", title_style))
    story_c.append(Spacer(1, 8))
    
    meta_table_c = [
        [Paragraph("<b>Application ID:</b> [MISSING / UNREADABLE]", body_style), Paragraph("<b>Permanent Institute ID:</b> [NOT PROVIDED]", body_style)],
        [Paragraph("<b>Academic Year:</b> 2026-27", body_style), Paragraph("<b>Date of Issue:</b> UNKNOWN", body_style)],
        [Paragraph("<b>Institution Name:</b> ABC Institute of Technology", body_style), Paragraph("<b>Approval Status:</b> PENDING", body_style)]
    ]
    t_meta_c = Table(meta_table_c, colWidths=[270, 270])
    t_meta_c.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFFBEB')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#F59E0B')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#FDE68A')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story_c.append(t_meta_c)
    story_c.append(Spacer(1, 10))
    story_c.append(Paragraph("<b>Note: Course Intake Table Section is blank or missing.</b>", body_style))
    story_c.append(Spacer(1, 30))
    story_c.append(Paragraph("<i>[Signature Page Missing / Unauthenticated]</i>", ParagraphStyle('Sign', parent=body_style, alignment=1, textColor=colors.HexColor('#B91C1C'))))
    doc_c.build(story_c)
    print(f"Generated Doc C: {doc_c_path}")

    # ==========================================
    # 4. SUPPORTING CERTIFICATE (CERT-DEMO-101 for mock issuer check)
    # ==========================================
    doc_cert_path = os.path.join(output_dir, "Fire_Safety_Certificate_CERT-DEMO-101.pdf")
    doc_cert = SimpleDocTemplate(doc_cert_path, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
    story_cert = []
    story_cert.append(Paragraph("MAHARASHTRA FIRE SERVICES DEPARTMENT", header_style))
    story_cert.append(Paragraph("GOVERNMENT OF MAHARASHTRA", sub_header_style))
    story_cert.append(Spacer(1, 6))
    story_cert.append(Paragraph("*** SYNTHETIC DEMO CERTIFICATE FOR ISSUER VERIFICATION WORKFLOW ***", disclaimer_style))
    story_cert.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#002147'), spaceAfter=8))
    story_cert.append(Paragraph("<b>FIRE SAFETY COMPLIANCE & NOC CERTIFICATE</b>", title_style))
    story_cert.append(Spacer(1, 10))
    
    cert_meta = [
        [Paragraph("<b>Certificate Ref No:</b> CERT-DEMO-101", body_style), Paragraph("<b>Issuing Authority:</b> Chief Fire Officer, Pune", body_style)],
        [Paragraph("<b>Issued To:</b> ABC Institute of Technology, Pune", body_style), Paragraph("<b>Issue Date:</b> 10/01/2026", body_style)],
        [Paragraph("<b>Valid Till:</b> 09/01/2027 (Active)", body_style), Paragraph("<b>Inspection Status:</b> Compliant - Type A Building", body_style)]
    ]
    t_cert = Table(cert_meta, colWidths=[270, 270])
    t_cert.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0FDF4')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#4ADE80')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#BBF7D0')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story_cert.append(t_cert)
    story_cert.append(Spacer(1, 20))
    story_cert.append(Paragraph("Certified that ABC Institute of Technology has installed fire safety measures as per National Building Code (NBC) Part IV.", body_style))
    doc_cert.build(story_cert)
    print(f"Generated Doc Cert: {doc_cert_path}")

if __name__ == "__main__":
    create_synthetic_docs()
