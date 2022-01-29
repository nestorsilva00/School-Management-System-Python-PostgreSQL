from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Table, SimpleDocTemplate, Paragraph, Spacer
from reportlab.graphics.shapes import Drawing, Line
from service.Nota_Service import Nota_Service
from PyQt5.QtWidgets import QMessageBox
import os

def estudiantes_suspensos_por_grupo(curso, anno, grupo):
    w, h = A4
    doc = SimpleDocTemplate("Alumnos_suspensos_curso_"+curso+"_anno_"+str(anno)+"_grupo_"+str(grupo)+".pdf", pagesize=A4)
    story=[]
    d = Drawing(100, -30)
    d.add(Line(0, 0, 435, 0))
    story.append(d)
    story.append(Paragraph("Alumnos suspensos Curso: "+curso+" Año: "+str(anno)+" Grupo: "+str(grupo), ParagraphStyle('default', fontSize=17, alignment=1, font = "Helvetica-Bold")))
    c = Drawing(100, 30)
    c.add(Line(0, 0, 435, 0))
    story.append(c)
    story.append(Spacer(0, 15))
    header = ["Nombre", "Apellidos", "Asignatura"]
    data=[]
    data.append(header)
    rows=Nota_Service.estudiantes_suspensos_por_grupo(Nota_Service, curso, anno, grupo)
    k=0
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



