# Timer Python QGIS Eficiente
Medir e exibir o tempo de execução de código em Python de maneira simples e eficaz.
```py
from time import perf_counter, localtime, strftime

class Timer:
    def __enter__(self):
        self.start_time = perf_counter()
        return self

    def __exit__(self, *args):
        self.end_time = perf_counter()
        elapsed_time = self.end_time - self.start_time
        self.print_elapsed_time(elapsed_time)

    def print_elapsed_time(self, elapsed_time):
        if elapsed_time <= 60:
            time_str = '{0:.1f}s'.format(elapsed_time)
        elif elapsed_time <= 3600:
            time_str = '{0:.1f}m'.format(elapsed_time / 60)
        else:
            time_str = '{0:.2f}h'.format(elapsed_time / 3600)

        print('Tempo decorrido: %s' % time_str)

# Exemplo de uso
print('Início do processamento: %s' % strftime('%A %d de %B de %Y %Hh%Mmin%Sseg %Z', localtime()))
with Timer() as timer:
    # Seu código ou processo aqui
    # ...

# O tempo é automaticamente impresso ao sair do bloco 'with'
```
## Importações:
```py
from time import perf_counter, localtime, strftime
```
+ **perf_counter**: Uma função que fornece um contador de alta resolução para medir o tempo decorrido.
+ **localtime, strftime**: Funções para obter e formatar a data e hora local.

  ## Classe Timer:
```py
class Timer:
```
+ Define uma classe chamada **Timer**.

  ## Método **__enter__**:
```py
def __enter__(self):
    self.start_time = perf_counter()
    return self
```
+ Chamado quando você entra no bloco **with**. Registra o tempo de início usando **perf_counter()** e retorna a instância do objeto **Timer**.

  ## Método **__exit__**:
```py
def __exit__(self, *args):
    self.end_time = perf_counter()
    elapsed_time = self.end_time - self.start_time
    self.print_elapsed_time(elapsed_time)
```
+ Chamado quando você sai do bloco **with**. Registra o tempo de término, calcula o tempo decorrido e chama **print_elapsed_time** para exibi-lo.

  ## Método **print_elapsed_time**:
```py
def print_elapsed_time(self, elapsed_time):
    if elapsed_time <= 60:
        time_str = '{0:.1f}s'.format(elapsed_time)
    elif elapsed_time <= 3600:
        time_str = '{0:.1f}m'.format(elapsed_time / 60)
    else:
        time_str = '{0:.2f}h'.format(elapsed_time / 3600)

    print('Tempo decorrido: %s' % time_str)
```
+ Formata o tempo decorrido em segundos, minutos ou horas e imprime na tela.

  ## Exemplo de uso::
```py
print('Início do processamento: %s' % strftime('%A %d de %B de %Y %Hh%Mmin%Sseg %Z', localtime()))
with Timer() as timer:
    # Seu código ou processo aqui
    # ...
```
+ Demonstração de como usar a classe **Timer** com o bloco **with**. O tempo inicial é impresso, e o tempo decorrido é automaticamente impresso quando o bloco **with** é concluído.

# Avaliação Temporal em multiplos Blocos 

Para medir o tempo de execução de blocos de código específicos, você pode incorporar a lógica do **Timer** em cada bloco usando a instrução **with**. Aqui está um exemplo de como você pode fazer isso:

```py
from time import perf_counter, localtime, strftime

class Timer:
    def __init__(self, block_name="Bloco"):
        self.block_name = block_name

    def __enter__(self):
        self.start_time = perf_counter()
        return self

    def __exit__(self, *args):
        self.end_time = perf_counter()
        elapsed_time = self.end_time - self.start_time
        self.print_elapsed_time(elapsed_time)

    def print_elapsed_time(self, elapsed_time):
        if elapsed_time <= 60:
            time_str = '{0:.1f}s'.format(elapsed_time)
        elif elapsed_time <= 3600:
            time_str = '{0:.1f}m'.format(elapsed_time / 60)
        else:
            time_str = '{0:.2f}h'.format(elapsed_time / 3600)

        print('Tempo decorrido no {}: {}'.format(self.block_name, time_str))

# Exemplo de uso
with Timer("Bloco 1") as timer1:
    # Seu primeiro bloco de código
    # ...

with Timer("Bloco 2") as timer2:
    # Seu segundo bloco de código
    # ...
```
