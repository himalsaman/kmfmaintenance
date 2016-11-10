from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch,A5
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table
from reportlab.lib.styles import getSampleStyleSheet

from models.customersModel import select_all_customers

doc = SimpleDocTemplate("complex_cell_values.pdf", pagesize=A5)
elements = []
styleSheet = getSampleStyleSheet()

data= [['','','logoBanner',''],
   ['ID', 'Name', 'Mobile Number','City']

]
for x in select_all_customers():
    data.append([str(x.id), x.name, x.mobile_number, str(x.city_id)])
t=Table(data,style=[('BOX',(0,0),(-1,-1),2,colors.black),
                ('GRID',(0,1),(-1,-1),0.5,colors.black),
                ('SPAN',(0,0),(1,0)),
                ('SPAN',(3,0),(3,0)),
                ('ALIGN',(0,0),(3,-0),'CENTER')
                ])
t._argW[3]=0.7*inch
t._argW[2]=1.2*inch
t._argW[1]=1.5*inch
t._argW[0]=0.4*inch
elements.append(t)
doc.build(elements)