from fpdf import FPDF

pdf = FPDF(orientation="L",format="A4")
pdf.add_page()
pdf.set_font("Times", size=16)

subject = ['English','English Gramer', 'Mathemetics','Science','General Knowledge', 'Moral Science', 'Computer', 'Gujarati','Hindi','social Science', 'Sanskrit','Drawing','P.T.']

pdf.set_font("helvetica", "B", 14)

with pdf.table() as table:
    row = table.row()
    row.cell("<<Name>>")
    row.cell("0",colspan=5)
    
    row = table.row()
    row.cell("Standard:")
    row.cell("<<std>>")
    row.cell("GR NO:")
    row.cell("<<grno>>")
    row.cell("Roll No:")
    row.cell("<<rollno>>")

#pdf.ln(10)

pdf.set_font("helvetica", "B", 13)
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
        pdf.set_font("helvetica", "B", 12)
        row.cell(sub)
        pdf.set_font("helvetica", "", 11)
        row.cell("<<eng_sem1>>",align="C")
        row.cell("<<eng_sem2>>",align="C")
        row.cell("<<Annual>>",align="C")
        row.cell("<<grade1>>",align="C")



pdf.output('tablereult.pdf')