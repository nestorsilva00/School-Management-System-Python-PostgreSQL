from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Table, SimpleDocTemplate, Paragraph, Spacer
from reportlab.graphics.shapes import Drawing, Line
from service.Baja_Service import Baja_Service
from PyQt5.QtWidgets import QMessageBox
import os

def report_bajas_por_grupo(curso, anno, grupo):
    rows = Baja_Service.read_bajas_por_grupo(Baja_Service, curso, anno, grupo)
    w, h = A4
    doc = SimpleDocTemplate("Escalafon_grupo_"+str(grupo)+"_curso_"+str(curso)+".pdf", pagesize=A4)
    story = []
    d = Drawing(100, -30)
    d.add(Line(0, 0, 435, 0))
    story.append(d)
    story.append(Paragraph("Bajas, Grupo: "+str(grupo)+", Curso:"+str(curso)+" Año: "+str(anno), ParagraphStyle('default', fontSize=21, alignment=1, font = "Helvetica-Bold")))
    c = Drawing(100, 20)
    c.add(Line(0, 0, 435, 0))
    story.append(c)
    story.append(Spacer(0, 15))
    header = ["Nombre", "Apellidos", "Motivo"]
    data=[]
    data.append(header)

    for i in rows:
            row = []
            for j in i:
                row.append(j)
            data.append(row)

    t=Table(data)
    story.append(t)

    if os.path.isfile(doc.filename):
        try:
            os.remove(doc.filename)
            doc.build(story)
            os.system(doc.filename)
        except OSError as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(str(e) + ". El archivo está abierto")
            msg.setWindowTitle("Error")
            msg.exec_()
    else:
        doc.build(story)
        os.system(doc.filename)

def report_bajas_por_anno(curso, anno):
    rows = Baja_Service.read_bajas_por_anno(Baja_Service, curso, anno)
    w, h = A4
    doc = SimpleDocTemplate("Bajas_por_anno+"+"_curso_"+str(curso)+"_anno_"+str(anno)+".pdf", pagesize=A4)
    story = []
    d = Drawing(100, -30)
    d.add(Line(0, 0, 435, 0))
    story.append(d)
    story.append(Paragraph("Bajas anuales, Curso:"+str(curso)+" Año:"+str(anno), ParagraphStyle('default', fontSize=21, alignment=1, font = "Helvetica-Bold")))
    c = Drawing(100, 20)
    c.add(Line(0, 0, 435, 0))
    story.append(c)
    story.append(Spacer(0, 15))
    header = ["Nombre", "Apellidos", "Grupo", "Motivo"]
    data=[]
    data.append(header)
    for i in rows:
            row = []
            for j in i:
                row.append(j)
            data.append(row)

    t=Table(data)
    story.append(t)

    if os.path.isfile(doc.filename):
        try:
            os.remove(doc.filename)
            doc.build(story)
            os.system(doc.filename)
        except OSError as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(str(e) + ". El archivo está abierto")
            msg.setWindowTitle("Error")
            msg.exec_()
    else:
        doc.build(story)
        os.system(doc.filename)


