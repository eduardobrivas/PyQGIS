import processing
import os

# Defina a pasta de entrada
pasta_entrada = r'C:\Users\eduardo.rivas\OneDrive - ARAUCO\2023\CAR_MS\Nova pasta\CARMS0026766_INSCRITO'

# Lista todos os arquivos na pasta de entrada com a extensão .shp
arquivos_shp = [f for f in os.listdir(pasta_entrada) if f.endswith('.shp')]

# Defina o sistema de coordenadas de destino (altere conforme necessário)
target_crs = 'EPSG:31982'  # Por exemplo, WGS84

# Crie a pasta de saída como subpasta da pasta de entrada
pasta_saida = os.path.join(pasta_entrada, 'reprojetados')

# Certifique-se de que a pasta de saída exista, se não, crie-a
if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

# Reprojete cada shapefile na pasta de entrada
for arquivo_shp in arquivos_shp:
    caminho_entrada = os.path.join(pasta_entrada, arquivo_shp)
    caminho_saida = os.path.join(pasta_saida, arquivo_shp)
    
    processing.run("native:reprojectlayer", {
        'INPUT': caminho_entrada,
        'TARGET_CRS': target_crs,
        'OUTPUT': caminho_saida
    })

print("Reprojeção concluída. Arquivos salvos em:", pasta_saida)