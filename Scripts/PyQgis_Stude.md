```py
# https://qgis.org/pyqgis/3.14/
# Projeto Qgis


# Criar uma instância
project = QgsProject.instance()

# Identificar o caminho do meu projeto
project.read('D:\dados\dados_sig.qgs')
print(project.fileName())

#
print(project.absoluteFilePath())

print(project.annotationManager())

print(project.crs())

#Salvar projeto do Qgis

project.write('D:\dados\dados_sig.qgs')



```
