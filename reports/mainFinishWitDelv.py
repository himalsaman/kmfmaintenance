import os
import subprocess
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.platypus import (Flowable, Paragraph,
								SimpleDocTemplate, Spacer)
from reportlab.platypus import Image
from reportlab.platypus import Table
from reportlab.platypus import TableStyle

from Control.maintenanceLogic import getMaintenanceWaitingDelevary


class MCLine(Flowable):
	def __init__(self, start, width, height=0):
		Flowable.__init__(self)
		self.width = width
		self.height = height
		self.start = start

	def __repr__(self):
		return "Line(w=%s)" % self.width

	def draw(self):
		"""
		draw the line
		"""
		self.canv.line(self.start, self.height, self.width, self.height)


class CreateMaintFinishWaitDelvReport(object):
	def __init__(self):
		"""Constructor"""
		self.width, self.height = A4
		self.styles = getSampleStyleSheet()

		pdfname = 'maintfinishwaitdelv.pdf'
		self.refile = os.path.join(os.path.expanduser("~"), "Documents/", pdfname)

	def coord(self, x, y, unit=1):
		"""
		http://stackoverflow.com/questions/4726011/wrap-text-in-a-table-reportlab
		Helper class to help position flowables in Canvas objects
		"""
		x, y = x * unit, self.height - y * unit
		return x, y

	def createDocument(self, canvas, doc):
		"""
		Create the document
		"""
		self.c = canvas
		normal = self.styles["Normal"]
		centered = ParagraphStyle(name="centered", alignment=TA_CENTER)

		logo = "D:\himalsaman\dev\pyworkspace\maintenance\images\khatemalogo.jpg"
		img = Image(logo, 50, 50)
		img.wrapOn(self.c, self.width, self.height)
		img.drawOn(self.c, *self.coord(10, 20, mm))

		header_text = "<font size=12><b>Khatmah Medical Factory</b></font>"
		p = Paragraph(header_text, normal)
		p.wrapOn(self.c, self.width, self.height)
		p.drawOn(self.c, *self.coord(30, 8, mm))

		ptext = "<font size=7><a>For the manufacture and maintenance of </a></font>"
		p = Paragraph(ptext, normal)
		p.wrapOn(self.c, self.width, self.height)
		p.drawOn(self.c, *self.coord(30, 13, mm))

		ptext = "<font size=7><a>tools support for people with special needs</a></font>"
		p = Paragraph(ptext, style=normal)
		p.wrapOn(self.c, self.width, self.height)
		p.drawOn(self.c, *self.coord(30, 16, mm))

		ptext = "<font size=8><a><b>First factory is specialized in the Gulf region</b></a></font>"
		p = Paragraph(ptext, style=normal)
		p.wrapOn(self.c, self.width, self.height)
		p.drawOn(self.c, *self.coord(30, 22, mm))

		ptext = "<font size=9><a><b>A Great Hope & Unlimited Ambition</b></a></font>"
		p = Paragraph(ptext, style=normal)
		p.wrapOn(self.c, self.width, self.height)
		p.drawOn(self.c, *self.coord(148, 22, mm))

		self.c.line(*self.coord(10, 22, mm), *self.coord(202, 22, mm))

		ptext = "<font size=10><u><b>Maintenance's Finish and Waiting Delivering </b></u></font>"
		p = Paragraph(ptext, style=normal)
		p.wrapOn(self.c, self.width, self.height)
		p.drawOn(self.c, *self.coord(12, 30, mm))

		datetimestr = datetime.now()
		timestampstr = datetimestr.strftime('%Y-%m-%d %H:%M:%S')
		ptext = "<font size=6><a>{} - </a></font>".format(self.refile) + "<font size=6><a>{} </a></font>".format(
			timestampstr)
		p = Paragraph(ptext, style=normal)
		p.wrapOn(self.c, self.width, self.height)
		p.drawOn(self.c, *self.coord(10, 286, mm))

		self.c.line(*self.coord(10, 285, mm), *self.coord(202, 285, mm))
		ptext = '<font size=10><p>CR:1010421226 - PC: 13217 - Wasel : 7966 - Tel & Fax: 014151557 - Mob: 0505721609 <br/>Website: www.khatmahfactory.com - E-mail : info@khatmahfactory.com - 3rd Industrial Area - Riyadh - Saudi Arabia </p></font>'
		p = Paragraph(ptext, centered)
		p.wrapOn(self.c, self.width, self.height)
		p.drawOn(self.c, *self.coord(0, 295, mm))

	def create_pdf(self):
		"""
		Create a pdf
		"""
		story = []

		doc = SimpleDocTemplate(self.refile, pagesize=A4)
		styles = getSampleStyleSheet()

		spacer = Spacer(0, 0.07 * inch)

		story.append(spacer)
		story.append(spacer)

		line = MCLine(-30, 470)
		story.append(line)
		story.append(spacer)

		text_data = ["#", "Maint. Code", "Cust. Name", "Maint. Product", "Created Date", "Cost"]
		d = []
		font_size = 8
		centered = ParagraphStyle(name="centered", alignment=TA_CENTER)
		for text in text_data:
			ptext = "<font size=%s><b>%s</b></font>" % (font_size, text)
			p = Paragraph(ptext, centered)
			d.append(p)

		data = [d]

		line_num = 1

		formatted_line_data = []

		for idx, val in enumerate(getMaintenanceWaitingDelevary()):
			cost = val.cost_of_bill_of_material + val.cost_of_labor
			line_data = [str(line_num), val.m_code, val.customers.name,
						 val.product_of_maintenance, val.created_at, cost]

			for item in line_data:
				ptext = "<font size=%s>%s</font>" % (font_size - 1, item)
				p = Paragraph(ptext, centered)
				formatted_line_data.append(p)
			data.append(formatted_line_data)
			formatted_line_data = []
			line_num += 1

		table = Table(data, colWidths=[20, 80, 160, 130, 80, 50], rowHeights=20
					  , style=[('GRID', (0, 0), (-1, -1), 0.5, colors.black)])
		story.append(table)
		story.append(spacer)
		#########################################################################################
		simplelistFN = []
		# mainlist = select_All_maintenance_customer(self.custo.id)
		for idx, val in enumerate(getMaintenanceWaitingDelevary()):
			simplelistFN.append(val.cost_of_bill_of_material + val.cost_of_labor)

		totxt = '<font size=9><p><b>Total</b></p></font>'
		ptotxt = Paragraph(totxt, styles["Normal"])

		totxtnum = '<p>{}</p>'.format(sum(simplelistFN))
		ptotxtnum = Paragraph(totxtnum, styles["Normal"])
		data = [['', '', '', ptotxt, ptotxtnum]]
		t = Table(data, colWidths=[5, 5, 400, 50, 60], rowHeights=15)
		t.setStyle(TableStyle([('LINEABOVE', (3, 2), (-1, -1), 0.25, colors.black)]))
		story.append(t)
		for x in range(10):
			story.append(spacer)
		#
		# #########################################################################################
		actxt = '<font size=11><p><u>Accountant</u><br/>Rani Mohamed</p></font>'
		pactxt = Paragraph(actxt, centered)

		matxtnum = '<font size=11><p><u>Manager</u><br/>Mohamed Althubiti</p></font>'
		pmatxtnum = Paragraph(matxtnum, centered)
		data = [[pactxt, '', '', '', pmatxtnum]]
		t = Table(data, colWidths=[150, 5, 250, 5, 150])
		t.setStyle(TableStyle([('LINEABOVE', (3, 2), (-1, -1), 0.25, colors.black)]))
		story.append(t)
		#########################################################################################

		story.append(spacer)

		doc.build(story, self.createDocument)

		subprocess.Popen([self.refile], shell=True)

	# ----------------------------------------------------------------------
	# if __name__ == "__main__":
	# create_pdf()
	# CreateMaintFinishWaitDelvReport().create_pdf()
