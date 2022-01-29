from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Table, SimpleDocTemplate, Paragraph, Spacer
from reportlab.graphics.shapes import Drawing, Line
from service.Nota_Service import Nota_Service
from PyQt5.QtWidgets import QMessageBox
from utils import Validaciones
import os

def report_escalafon_por_grupo(curso, anno, grupo):
    rows = Nota_Service.promedio_acumulado_por_grupo(Nota_Service, curso, anno, grupo)
    w, h = A4
    doc = SimpleDocTemplate("Escalafon_grupo_"+str(grupo)+"_curso_"+str(curso)+"_anno_"+str(anno)+".pdf", pagesize=A4)
    story = []
    d = Drawing(100, -30)
    d.add(Line(0, 0, 435, 0))
    story.append(d)
    story.append(Paragraph("Escalafón, Grupo: "+str(grupo)+", Curso:"+str(curso)+" Año:"+str(anno), ParagraphStyle('default', fontSize=21, alignment=1, font = "Helvetica-Bold")))
    c = Drawing(100, 20)
    c.add(Line(0, 0, 435, 0))
    story.append(c)
    story.append(Spacer(0, 15))
    header = ["Posición", "Código del estudiante", "Nombre", "Apellidos", "Promedio acumulado"]
    data=[]
    data.append(header)
    contador=1
    for i in rows:
            row = []
            row.append(contador)
            for j in range(len(i)):
                if j == 3:
                    promedio = Validaciones.reducir_a_cifras_significativas(float(i[j]), 2)
                    row.append(promedio)
                else:
                    row.append(i[j])
            data.append(row)
            contador+=1

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

def report_escalafon_por_anno(curso, anno):
    rows = Nota_Service.escalafon_por_anno(Nota_Service, curso, anno)
    w, h = A4
    doc = SimpleDocTemplate("Escalafon_Anual_grupo_"+"_curso_"+str(curso)+"_anno_"+str(anno)+".pdf", pagesize=A4)
    story = []
    d = Drawing(100, -30)
    d.add(Line(0, 0, 435, 0))
    story.append(d)
    story.append(Paragraph("Escalafón anual, Curso:"+str(curso)+" Año:"+str(anno), ParagraphStyle('default', fontSize=21, alignment=1, font = "Helvetica-Bold")))
    c = Drawing(100, 20)
    c.add(Line(0, 0, 435, 0))
    story.append(c)
    story.append(Spacer(0, 15))
    header = ["Posición","código del estudiante","Nombre", "Apellidos", "Promedio anual"]
    data=[]
    data.append(header)
    contador=1
    for i in rows:
            row = []
            row.append(contador)
            for j in range(len(i)):
                if j == 3:
                    promedio = Validaciones.reducir_a_cifras_significativas(float(i[j]), 2)
                    row.append(promedio)
                else:
                    row.append(i[j])
            data.append(row)
            contador += 1

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


