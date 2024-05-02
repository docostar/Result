import openpyxl
 
# Give the location of the file
file_Name = "marks_7.xlsx"
 
# To open the workbook 
# workbook object is created
wb = openpyxl.load_workbook(file_Name)

sheet = wb["Sheet1"]
name=sheet["C5"].value

print(name)