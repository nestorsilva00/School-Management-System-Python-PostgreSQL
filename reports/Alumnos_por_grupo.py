from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Table, SimpleDocTemplate, Paragraph, Spacer
from reportlab.graphics.shapes import Drawing, Line
from service.Estudiante_Service import Estudiante_Service
from PyQt5.QtWidgets import QMessageBox
import os


def report_alumnos_por_grupo():
    w, h = A4
    doc = SimpleDocTemplate("Alumnos_por_grupo.pdf", pagesize=A4)
    story=[]
    d = Drawing(100, -30)
    d.add(Line(0, 0, 435, 0))
    story.append(d)
    story.append(Paragraph("Listado de alumnos por grupo", ParagraphStyle('default', fontSize=30, alignment=1, font = "Helvetica-Bold")))
    c = Drawing(100, 30)
    c.add(Line(0, 0, 435, 0))
    story.append(c)
    story.append(Spacer(0, 15))
    header = ["Curso", "Año", "Nombre", "Apellidos", "Grupo", "Código", "Número de orden"]
    data=[]
    data.append(header)
    rows=Estudiante_Service.report_lista_estudiantes_grupo(Estudiante_Service)
    k=0
    for i in rows:
            if i[4] != data[len(data)-1][4]:
                k=0
            row = []
            for j in i:
                row.append(j)
            k+=1

            row.append(k)
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
            msg.setText(str(e)+". El archivo está abierto")
            msg.setWindowTitle("Error")
            msg.exec_()
    else:
        doc.build(story)
        os.system(doc.filename)



