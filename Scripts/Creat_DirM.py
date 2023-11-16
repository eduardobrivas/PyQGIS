import os
from datetime import datetime
import shutil

def criar_pastas(diretorio_base, diretorio_origem_gdb):
    # Obter o nome do mês atual em maiúsculas
    nome_mes = datetime.now().strftime("%B").upper()

    # Obter o ano atual
    ano = datetime.now().strftime("%Y")

    # Combinar o nome do mês e ano com um '_' como separador
    nome_mes_ano = f"{nome_mes}_{ano}"

    # Caminho completo para o diretório do mês atual
    diretorio_mes = os.path.join(diretorio_base, nome_mes_ano)

    # Caminhos para as pastas internas
    pastas_internas = ['SHP-RAW', 'FINAL', 'IMAGEN-NDVI', 'CSV']

    try:
        # Criar o diretório do mês
        os.makedirs(diretorio_mes)

        # Criar as pastas internas dentro do diretório do mês
        for pasta in pastas_internas:
            os.makedirs(os.path.join(diretorio_mes, pasta))

        print(f"Estrutura de pastas criada com sucesso em: {diretorio_mes}")

        # Lista todos os arquivos no geodatabase
        arquivos_gdb = [f for f in os.listdir(diretorio_origem_gdb) if f.endswith('.gdb')]

        # Copia o primeiro arquivo .gdb encontrado para a pasta SHP-RAW
        if arquivos_gdb:
            arquivo_gdb = arquivos_gdb[0]
            caminho_origem = os.path.join(diretorio_origem_gdb, arquivo_gdb)
            caminho_destino = os.path.join(diretorio_mes, 'SHP-RAW', f'{arquivo_gdb}')
            shutil.copytree(caminho_origem, caminho_destino)
            print(f"Arquivo {arquivo_gdb} copiado para SHP-RAW com sucesso.")

    except Exception as e:
        print(f"Erro ao criar a estrutura de pastas: {e}")

# Substitua 'CAMINHO_DO_SEU_DIRETORIO' e 'CAMINHO_DO_SEU_GDB' pelos caminhos desejados
diretorio_base = r'CAMINHO_DO_SEU_DIRETORIO'
diretorio_gdb = r'CAMINHO_DO_SEU_GDB'
criar_pastas(diretorio_base, diretorio_gdb)
