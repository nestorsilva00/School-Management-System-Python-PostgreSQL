from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Table, SimpleDocTemplate, Paragraph, Spacer
from reportlab.graphics.shapes import Drawing, Line
from service.Estudiante_Service import Estudiante_Service
from PyQt5.QtWidgets import QMessageBox
import os

def repitentes_por_anno(curso, anno):
    w, h = A4
    doc = SimpleDocTemplate("Repitentes_Año_"+str(anno)+"_Curso_"+curso+".pdf", pagesize=A4)
    story=[]
    d = Drawing(100, -30)
    d.add(Line(0, 0, 435, 0))
    story.append(d)
    story.append(Paragraph("Repitentes Año: "+str(anno)+" Curso: "+curso, ParagraphStyle('default', fontSize=21, alignment=1, font = "Helvetica-Bold")))
    c = Drawing(100, 30)
    c.add(Line(0, 0, 435, 0))
    story.append(c)
    story.append(Spacer(0, 15))
    header = ["Nombre", "Apellidos", "Grupo"]
    data=[]
    data.append(header)
    rows=Estudiante_Service.repitentes_por_anno(Estudiante_Service, curso, anno)

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



