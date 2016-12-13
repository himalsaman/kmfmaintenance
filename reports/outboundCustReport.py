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

from Control.ouboundControl import getOutbounEmployeeRow, getOutbounOneCustomerRow
from models.customersModel import select_customer_by_id
from reports.setting import imgPath


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


datetimestr = datetime.now()
timestampstr = datetimestr.strftime('%Y-%m-%d-%H:%M:%S')
timestampstr2 = datetimestr.strftime('%Y-%m-%d')


class CreateOutboundCustReport(object):
	def __init__(self, cust):
		"""Constructor"""
		self.width, self.height = A4
		self.styles = getSampleStyleSheet()
		self.cust = cust

		pdfname = 'outboundCust-{}'.format(timestampstr2) + '.pdf'
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

		logo = imgPath + "khatemalogo.jpg"
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

		ptext = '<font size=10><u><b>Outbound : {}</b></u></font>'.format(timestampstr)
		p = Paragraph(ptext, style=normal)
		p.wrapOn(self.c, self.width, self.height)
		p.drawOn(self.c, *self.coord(12, 30, mm))

		# datetimestr = datetime.now()
		# timestampstr = datetimestr.strftime('%Y-%m-%d %H:%M:%S')
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

		ptext = "<font size=10><a>Customer Name :{}</a></font>".format(self.cust.name)
		p = Paragraph(ptext, styles["Normal"])
		story.append(p)

		ptext = "<font size=10><a>Customer Mobile # :{}</a></font>".format(self.cust.mobile_number)
		p = Paragraph(ptext, styles["Normal"])
		story.append(p)
		story.append(spacer)
		story.append(spacer)
		"""
				Create the line items
				"""
		text_data = ["#", "Material Name", "Material Type", "QTY"]
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

		outlist = getOutbounOneCustomerRow(self.cust)
		for idx, val in enumerate(outlist):
			if val.rawMaterial:
				mname = val.rawMaterial.name
				typeName = "Raw Material"
			if val.spareParts:
				mname = val.spareParts.name
				typeName = "Spare Parts"
			if val.tools:
				mname = val.tools.name
				typeName = "Tools"
			if val.finishProducts:
				mname = val.finishProducts.name
				typeName = "Finish Product"
			line_data = [str(line_num), mname, typeName, val.req_qty]

			for item in line_data:
				ptext = "<font size=%s>%s</font>" % (font_size - 1, item)
				p = Paragraph(ptext, centered)
				formatted_line_data.append(p)
			data.append(formatted_line_data)
			formatted_line_data = []
			line_num += 1

		table = Table(data, colWidths=[30, 150, 150, 80, 80], rowHeights=20
					  , style=[('GRID', (0, 0), (-1, -1), 0.5, colors.black)])
		story.append(table)
		story.append(spacer)
		#########################################################################################
		actxt = '<font size=11><p><u>Accountant</u><br/>Rani Mohamed</p></font>'
		pactxt = Paragraph(actxt, centered)

		matxtnum = '<font size=11><p><u>Manager</u><br/>Mohamed Althubiti</p></font>'
		pmatxtnum = Paragraph(matxtnum, centered)
		data = [[pactxt, '', '', '', pmatxtnum]]
		t = Table(data, colWidths=[150, 5, 250, 5, 150])
		story.append(t)
		#########################################################################################

		story.append(spacer)

		doc.build(story, onFirstPage=self.createDocument, onLaterPages=self.createDocument)

		subprocess.Popen([self.refile], shell=True)

	# ----------------------------------------------------------------------

if __name__ == "__main__":
	CreateOutboundReport().create_pdf()
