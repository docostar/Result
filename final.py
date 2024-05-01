from fpdf import FPDF
class PDF(FPDF):
    def header(self):
        # Rendering logo:
        #self.image("../docs/fpdf2-logo.png", 10, 8, 33)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "Saint Mary School,Bagasara", align="C")
        # Performing a line break:
        self.ln(5)
        self.set_font("helvetica","I",11)
        self.cell(180,12,"Amreli Road, Bagasara - 365440, Dist. Amreli, Gujarat   Ph.:9428209955", align="C")
        self.ln(5)
        self.set_font("helvetica", "B", 15)
        self.cell(180, 15, "ANNUAL REPORT CARD: 2023-24", align="C")
        self.ln(10)

    
    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.ln(5)
        self.set_y(-35)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "B", 12)
        self.cell(180, 12, "School Reopens on : 05-06-2023", align="C")
        self.ln(5)
        self.set_font("helvetica", "I", 10)
        self.cell(50, 15, "Issue Date : 29-04-2023                       Signature of Class Teacher:                          Signature of Principal:", align="L")
        self.ln(5)
        self.cell(150,20, "Grading System:    91-100 : A+    81-90: A    71-80 : B+      61-70: B    51-60 : C+      41-50: C    31-40: D+", align="L")
        #self.cell(50, 15, "Grading System :91 -100 : A+      81 -90 : A      71 -80 : B+     61 - 70 : B      51 – 60 : C+       41 - 50 : C     31 - 40 : D+",align="C")

        # Printing page number:
        #self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")
    

# Instantiation of inherited class
pdf = PDF()
pdf.add_page()
pdf.set_font("Times", size=12)
'''
for i in range(1, 20):
    #pdf.cell(0, 10, f"Printing line number {i}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 10, f"Printing line number {i}")
'''
pdf.add_page()
pdf.output("result.pdf")