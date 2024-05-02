subject = ['English','English Gramer', 'Mathemetics','Science','General Knowledge', 'Moral Science', 'Computer', 'Gujarati','Hindi','social Science', 'Sanskrit','Drawing','P.T.']
name_size=10
subject_size=9
font_size=8
reopen_date="13-06-2024"
issue_date="04-05-2024"

from fpdf import FPDF
class PDF(FPDF):
    def header(self):
        # Rendering logo:
        #self.image("../docs/fpdf2-logo.png", 10, 8, 33)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 15)
        # Moving cursor to the right:
        #self.cell(80)
        self.cell(250, 5, "Saint Mary School,Bagasara", align="C")
        # Performing a line break:
        self.ln(2)
        self.set_font("helvetica","I",11)
        self.cell(250,12,"Amreli Road, Bagasara - 365440, Dist. Amreli, Gujarat   Ph.:9428209955", align="C")
        self.ln(5)
        self.set_font("helvetica", "B", 13)
        self.cell(250, 15, "ANNUAL REPORT CARD: 2023-24", align="C")
        self.ln(7)

    
    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.ln(3)
        self.set_y(-25)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "B", 12)
        self.cell(250, 12, f"School Reopens on : {reopen_date}", align="L")
        self.ln(5)
        self.cell(250, 15, f"Issue Date : {issue_date}                            Signature of Class Teacher:                                    Signature of Principal:", align="L")
        self.ln(5)
        self.cell(250,20, "Grading System:    91-100 : A+    81-90: A    71-80 : B+      61-70: B    51-60 : C+      41-50: C    31-40: D+", align="L")
        

        # Printing page number:
        #self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")
    

# Instantiation of inherited class
pdf = PDF(orientation="L",format="A4")
pdf.add_page()



pdf.ln(5)

with pdf.table() as table:
    pdf.set_font("helvetica", "B", name_size)
    row = table.row()
    row.cell("Name")
    row.cell("<<Name>>",colspan=5)
    
    row = table.row()
    row.cell("Standard:")
    row.cell("<<std>>")
    row.cell("GR NO:")
    row.cell("<<grno>>")
    row.cell("Roll No:")
    row.cell("<<rollno>>")



pdf.set_font("helvetica", "B", subject_size)
with pdf.table() as table:
    row = table.row()

    row = table.row()
    row.cell("Subject", rowspan=2,align="C")
    row.cell("Semester-1",align="C")
    row.cell("Semester-2",align="C")
    row.cell("Annual",colspan=2,align="C")
    
    row = table.row()
    row.cell("Marks(100)",align="C")
    row.cell("Marks(100)",align="C")
    row.cell("Marks(200)",align="C")
    row.cell("Grade(Sem1+Sem2)",align="C")

    for sub in subject:
        row = table.row()
        pdf.set_font("helvetica", "B", subject_size)
        row.cell(sub)
        pdf.set_font("helvetica", "", font_size)
        row.cell("<<eng_sem1>>",align="C")
        row.cell("<<eng_sem2>>",align="C")
        row.cell("<<Annual>>",align="C")
        row.cell("<<grade1>>",align="C")
    
    row = table.row()
    pdf.set_font("helvetica", "B", subject_size)
    row.cell("Obtained Total Marks & Overall Grade :",align="L",colspan=3)
    row.cell("<<Total>>",align="C")
    row.cell("<<Grade>>",align="C")

    row = table.row()
    row.cell("Obtained Percentage :",align="L",colspan=4)
    row.cell("<<per>>",align="C")
    
    row = table.row()
    row.cell("Attendance :",align="L")
    row.cell("«Attend»",align="C")
    row.cell("Total Working Days :",align="C",colspan=2)
    row.cell("«day»",align="C")

    row = table.row()
    row.cell("Passed and Promoted to next Standard :",align="L",colspan=4)
    row.cell("",align="C")

    row = table.row()
    row.cell("Remarks :",align="L",colspan=5)

pdf.output("result.pdf")