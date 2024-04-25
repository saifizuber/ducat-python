from fpdf import FPDF

pdf = FPDF()

pdf.add_page()

pdf.set_font('Arial', size=15)

f=open("D:\grand.txt.txt",'r')

for x in f:
    pdf.cell(50,5,txt = x, ln = 3)

pdf.output('d://SAM.pdf')



'''
assignment
how delete data from the file


'''


f=open