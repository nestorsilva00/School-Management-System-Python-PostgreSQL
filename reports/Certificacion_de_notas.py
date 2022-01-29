from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Table, SimpleDocTemplate, Paragraph, Spacer
from reportlab.graphics.shapes import Drawing, Line
from service.Nota_Service import Nota_Service
from PyQt5.QtWidgets import QMessageBox
from utils import Validaciones
import os

def report_certificacion_de_notas(cod_est, nombre, apellidos):
    w, h = A4
    doc = SimpleDocTemplate("Certificado_de_notas_de_"+nombre+str(cod_est)+".pdf", pagesize=A4)
    story = []
    d = Drawing(100, -30)
    d.add(Line(0, 0, 435, 0))
    story.append(d)
    story.append(Paragraph("Certificado de notas de "+nombre+" "+apellidos, ParagraphStyle('default', fontSize=15, alignment=1, font = "Helvetica-Bold")))
    c = Drawing(100, 20)
    c.add(Line(0, 0, 435, 0))
    story.append(c)
    story.append(Spacer(0, 15))
    header = ["Asignatura",  "Evaluación", "Año", "Curso"]
    data=[]
    data.append(header)
    rows=Nota_Service.certificado_de_notas(Nota_Service, cod_est)
    for i in range(0,len(rows)):
            row = []
            if i>0 and rows[i][2]!=rows[i-1][2]:
                promedio=Nota_Service.promedio_anual_por_estudiante(Nota_Service, cod_est, int(rows[i-1][2]))[0][0]
                promedio = Validaciones.reducir_a_cifras_significativas(float(promedio), 2)
                data.append(["Promedio: ", str(promedio)])
            for j in rows[i]:
                row.append(j)
            data.append(row)
    anno_actual = rows[len(rows)-1][2]
    promedio = Nota_Service.promedio_anual_por_estudiante(Nota_Service, cod_est, int(anno_actual))[0][0]
    promedio = Validaciones.reducir_a_cifras_significativas(float(promedio), 2)
    data.append(["Promedio: ", str(promedio)])
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

