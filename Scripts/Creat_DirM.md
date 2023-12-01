# Automatização de Estrutura de Pastas e Transferência de Geodatabases

Desenvolver um script Python para criar dinamicamente uma estrutura de pastas mensal e realizar a cópia automatizada do primeiro geodatabase (.gdb) 
encontrado para uma pasta específica, simplificando e organizando o processo de armazenamento de dados geoespaciais.

```py
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
```

## Importação de Bibliotecas:
```py
import os
from datetime import datetime
import shutil
```
+ **os**: Para operações de sistema.
+ **datetime**: Para manipulação de datas.
+ **shutil**: Para operações de cópia de arquivos


## Função **criar_pastas**:
+ A função **criar_pastas** recebe dois parâmetros: **diretorio_base** e **diretorio_origem_gdb**. Vamos entender cada parte dela:
```py
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

```
### Explicando

```py
def criar_pastas(diretorio_base, diretorio_origem_gdb):
```
A função inicia recebendo os diretórios base e de origem do geodatabase.
    
```py
    # Obter o nome do mês atual em maiúsculas
    nome_mes = datetime.now().strftime("%B").upper()
    
    # Obter o ano atual
    ano = datetime.now().strftime("%Y")
    
    # Combinar o nome do mês e ano com um '_' como separador
    nome_mes_ano = f"{nome_mes}_{ano}"
 ```
Aqui, obtém-se o nome do mês e o ano atual, combinando-os com um separador '_' para formar uma identificação única do mês e ano.
    
```py
    # Caminho completo para o diretório do mês atual
    diretorio_mes = os.path.join(diretorio_base, nome_mes_ano)
    ```
    - Gera o caminho completo para o diretório do mês, combinando o diretório base com o nome do mês e ano.
    
```py
    # Caminhos para as pastas internas
    pastas_internas = ['SHP-RAW', 'FINAL', 'IMAGEN-NDVI', 'CSV']
 ```
 Define uma lista de pastas internas desejadas.
    
```py
    try:
        # Criar o diretório do mês
        os.makedirs(diretorio_mes)
        
        # Criar as pastas internas dentro do diretório do mês
        for pasta in pastas_internas:
            os.makedirs(os.path.join(diretorio_mes, pasta))
        
        print(f"Estrutura de pastas criada com sucesso em: {diretorio_mes}")
```
 Dentro de um bloco `try`, cria o diretório do mês e as pastas internas. Se bem-sucedido, imprime uma mensagem de sucesso.
    
```py
        # Lista todos os arquivos no geodatabase
        arquivos_gdb = [f for f in os.listdir(diretorio_origem_gdb) if f.endswith('.gdb')]
        
        # Copia o primeiro arquivo .gdb encontrado para a pasta SHP-RAW
        if arquivos_gdb:
            arquivo_gdb = arquivos_gdb[0]
            caminho_origem = os.path.join(diretorio_origem_gdb, arquivo_gdb)
            caminho_destino = os.path.join(diretorio_mes, 'SHP-RAW', f'{arquivo_gdb}')
            shutil.copytree(caminho_origem, caminho_destino)
            print(f"Arquivo {arquivo_gdb} copiado para SHP-RAW com sucesso.")
```

## Configuração e Execução: 
+ Nesta seção, fornecemos valores para `diretorio_base` e `diretorio_gdb` (substitua pelos caminhos desejados) e chamamos a função `criar_pastas` para iniciar o processo.

```py
# Substitua 'CAMINHO_DO_SEU_DIRETORIO' e 'CAMINHO_DO_SEU_GDB' pelos caminhos desejados
diretorio_base = r'CAMINHO_DO_SEU_DIRETORIO'
diretorio_gdb = r'CAMINHO_DO_SEU_GDB'
criar_pastas(diretorio_base, diretorio_gdb)
```


