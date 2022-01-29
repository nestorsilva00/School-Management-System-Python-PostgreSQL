from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Table, SimpleDocTemplate, Paragraph, Spacer
from reportlab.graphics.shapes import Drawing, Line
from service.Evaluacion_Service import Evaluacion_Service
from PyQt5.QtWidgets import QMessageBox
import os

def report_evaluaciones_grupo_asignaturas():
    w, h = A4
    doc = SimpleDocTemplate("Evaluaciones_de_asignaturas_por_grupo.pdf", pagesize=A4)
    story = []
    d = Drawing(100, -30)
    d.add(Line(0, 0, 435, 0))
    story.append(d)
    story.append(Paragraph("Evaluaciones de asignaturas por grupo", ParagraphStyle('default', fontSize=21, alignment=1, font = "Helvetica-Bold")))
    c = Drawing(100, 20)
    c.add(Line(0, 0, 435, 0))
    story.append(c)
    story.append(Spacer(0, 15))
    header = ["Curso", "Año", "Grupo", "Asignatura", "Nombre", "Apellidos", "Evaluación"]
    data=[]
    data.append(header)
    rows=Evaluacion_Service.report_evaluaciones_asignaturas_grupo(Evaluacion_Service)
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

