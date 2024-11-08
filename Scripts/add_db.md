```py
from qgis.core import QgsDataSourceUri, QgsVectorLayer, QgsProject, QgsCoordinateReferenceSystem
import pyodbc

def load_vector_layer_auto(host, dbname, username, password, schema, layer_name, geometry_column="SHAPE"):
    """
    Carrega uma camada vetorial no QGIS diretamente do SQL Server, detectando automaticamente o SRID e o tipo de geometria.
    
    :param host: Endereço do servidor SQL
    :param dbname: Nome do banco de dados
    :param username: Usuário do banco de dados
    :param password: Senha do banco de dados
    :param schema: Nome do schema onde a camada está localizada
    :param layer_name: Nome da camada (tabela ou view) no banco de dados
    :param geometry_column: Nome da coluna de geometria (padrão: "SHAPE")
    """
    # Configura a conexão e a consulta SQL para obter SRID e tipo de geometria de forma eficiente
    conn_str = f"DRIVER={{SQL Server}};SERVER={host};DATABASE={dbname};UID={username};PWD={password}"
    query = f"""
    SELECT TOP 1
        {geometry_column}.STSrid AS srid,
        {geometry_column}.STGeometryType() AS tipo_geom
    FROM {schema}.{layer_name}
    """

    # Conecta e executa a consulta para obter SRID e tipo de geometria
    with pyodbc.connect(conn_str) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        if not result:
            print("Erro ao obter tipo de geometria ou SRID da camada.")
            return
        srid, tipo_geom = result

    # Configura a URI de conexão com o tipo de geometria e SRID obtidos
    uri = QgsDataSourceUri()
    uri.setConnection(host, "1433", dbname, username, password)
    uri.setDataSource(schema, layer_name, geometry_column)
    uri.setSrid(str(srid))
    uri.setParam("type", tipo_geom)  # Define o tipo de geometria automaticamente
    uri.setParam("disableInvalidGeometryHandling", "0")
    uri.setParam("primaryKeyInGeometryColumns", "0")

    # Carrega a camada no QGIS
    layer = QgsVectorLayer(uri.uri(False), layer_name, "mssql")
    if layer.isValid():
        layer.setCrs(QgsCoordinateReferenceSystem(int(srid), QgsCoordinateReferenceSystem.PostgisCrsId))
        QgsProject.instance().addMapLayer(layer)
        print(f"Camada '{layer_name}' carregada com sucesso!")
    else:
        print(f"Erro ao carregar a camada '{layer_name}'.")

# Parâmetros de conexão - ajuste conforme necessário
host = "azsrvprd0227.klabin.net"
dbname = "GEO"
username = "acessoleitura"
password = "acessoleitura"
schema = "geoklabin"
layer_name = "AREA_PRODUTIVA_evw"  # Nome da camada

# Executa a função para carregar a camada
load_vector_layer_auto(host, dbname, username, password, schema, layer_name)
```
