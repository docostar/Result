from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Times", size=16)

pdf.set_font("helvetica", "B", 15)

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

pdf.ln(10)
with pdf.table() as table:
    row = table.row()
    row.cell("Subject", rowspan=2)
    row.cell("Semester-1")
    row.cell("Semester-2")
    row.cell("Annual",colspan=2)
    
    row = table.row()
    row.cell("Marks(100)")
    row.cell("Marks(100)")
    row.cell("Marks(200)")
    row.cell("Grade(Sem1+Sem2)")

    row = table.row()
    row.cell("English")
    row.cell("<<eng_sem1>>")
    row.cell("<<eng_sem2>>")
    row.cell("<<Annual>>")
    row.cell("<<grade1>>")

pdf.output('tablereult.pdf')