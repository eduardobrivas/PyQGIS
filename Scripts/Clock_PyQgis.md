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
