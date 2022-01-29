from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Table, SimpleDocTemplate, Paragraph, Spacer
from reportlab.graphics.shapes import Drawing, Line
from service.Nota_Service import Nota_Service
from PyQt5.QtWidgets import QMessageBox
from utils import Validaciones
import os

def report_promedios_acumulados_por_grupo(curso, anno, grupo):
    rows = Nota_Service.promedio_acumulado_por_grupo(Nota_Service, curso, anno, grupo)
    w, h = A4
    doc = SimpleDocTemplate("Promedios_Acumulado_grupo_"+str(grupo)+"_curso_"+str(curso)+".pdf", pagesize=A4)
    story = []
    d = Drawing(100, -30)
    d.add(Line(0, 0, 435, 0))
    story.append(d)
    story.append(Paragraph("Promedio acumulado, Grupo: "+str(grupo)+", Curso:"+str(curso), ParagraphStyle('default', fontSize=15, alignment=1, font = "Helvetica-Bold")))
    c = Drawing(100, 20)
    c.add(Line(0, 0, 435, 0))
    story.append(c)
    story.append(Spacer(0, 15))
    header = ["Código del estudiante", "Nombre", "Apellidos", "Promedio acumulado"]
    data=[]
    data.append(header)
    for i in rows:
            row = []
            for j in range(len(i)):
                if j == 3:
                    promedio = Validaciones.reducir_a_cifras_significativas(float(i[j]), 2)
                    row.append(promedio)
                else:
                    row.append(i[j])
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

def report_promedios_anuales_por_grupo(curso, anno, grupo):
    rows = Nota_Service.promedio_anual_por_grupo(Nota_Service, curso, anno, grupo)
    w, h = A4
    doc = SimpleDocTemplate("Promedios_Anual_grupo_"+str(grupo)+"_curso_"+str(curso)+".pdf", pagesize=A4)
    story = []
    d = Drawing(100, -30)
    d.add(Line(0, 0, 435, 0))
    story.append(d)
    story.append(Paragraph("Promedio anual, Grupo: "+str(grupo)+", Curso:"+str(curso)+" Año:"+str(anno), ParagraphStyle('default', fontSize=15, alignment=1, font = "Helvetica-Bold")))
    c = Drawing(100, 20)
    c.add(Line(0, 0, 435, 0))
    story.append(c)
    story.append(Spacer(0, 15))
    header = ["código del estudiante","Nombre", "Apellidos", "Promedio anual", "Año"]
    data=[]
    data.append(header)
    for i in rows:
            row = []
            for j in range(len(i)):
                if j==3:
                   promedio=Validaciones.reducir_a_cifras_significativas(float(i[j]), 2)
                   row.append(promedio)
                else:
                    row.append(i[j])
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


