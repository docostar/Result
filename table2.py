from fpdf import FPDF

TABLE_DATA = (
    ("First name", "Last name", "Age", "City"),
    ("Jules", "Smith", "34", "San Juan"),
    ("Mary", "Ramos", "45", "Orlando"),
    ("Carlson", "Banks", "19", "Los Angeles"),
    ("Lucas", "Cimon", "31", "Saint-Mathurin-sur-Loire"),
)
pdf = FPDF()
pdf.add_page()
pdf.set_font("Times", size=16)


with pdf.table(text_align="CENTER") as table:
    row = table.row()
    row.cell("A1", colspan=2, rowspan=3)
    row.cell("C1", colspan=2)

    row = table.row()
    row.cell("C2", colspan=2, rowspan=2)

    row = table.row()
    # all columns of this row are spanned by previous rows

    row = table.row()
    row.cell("A4", colspan=4)

    row = table.row()
    row.cell("A5", colspan=2)
    row.cell("C5")
    row.cell("D5")

    row = table.row()
    row.cell("A6")
    row.cell("B6", colspan=2, rowspan=2)
    row.cell("D6", rowspan=2)

    row = table.row()
    row.cell("A7")

pdf.output('table2.pdf')