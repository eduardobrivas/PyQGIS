```py
# https://qgis.org/pyqgis/3.14/
# Projeto Qgis


# Criar uma instância
project = QgsProject.instance()

# Identificar o caminho do meu projeto
project.read(r'C:\Users\eduar\Documents\PyQGIS\dados\dados_sig.qgs')
print(project.fileName())

#
print(project.absoluteFilePath())

print(project.annotationManager())

print(project.crs())

#Salvar projeto do Qgis

project.write(r'C:\Users\eduar\Documents\PyQGIS\dados\dados_sig.qgs')

#set canva 

project.setBackgroundColor(QColor(51,153,255))

project.setBackgroundColor(QColor(255,255,255))

#quantidades de camadas no projeto

project.count()

project.setCrs(QgisCoordinateReferenceSystem("EPSG 31982")

project.title()

project.setTitle('Curso PyQGIS')

#identificr qual é o elipsoide do projeto

project.ellipsoid()

project.setEllipsoid(


project.lastModified()

```
