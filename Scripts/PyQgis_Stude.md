# Tutorial PyQGIS

## Criar uma instância do projeto

```python
# Criar uma instância
project = QgsProject.instance()
```

# Identificar o caminho do meu projeto
```python
project.read(r'C:\Users\eduar\Documents\PyQGIS\dados\dados_sig.qgs')
print(project.fileName())
print(project.absoluteFilePath())
```
# Informações sobre o gerenciador de anotações e o CRS do projeto
```python
print(project.annotationManager())
print(project.crs())
```

# Salvar projeto do QGIS
```python
project.write(r'C:\Users\eduar\Documents\PyQGIS\dados\dados_sig.qgs')
```
# Definir cor de fundo do canvas
```python
project.setBackgroundColor(QColor(51, 153, 255))
project.setBackgroundColor(QColor(255, 255, 255))
```
# Quantidade de camadas no projeto
```python
print(project.count())
```
# Definir o CRS do projeto
```python
project.setCrs(QgisCoordinateReferenceSystem("EPSG 31982"))
```
# Título do projeto
```py
print(project.title())
project.setTitle('Curso PyQGIS')
```
# Informações sobre o elipsoide do projeto
```py
print(project.ellipsoid())
```
# Data e hora da última modificação do projeto
```py
print(project.lastModified())
```



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
