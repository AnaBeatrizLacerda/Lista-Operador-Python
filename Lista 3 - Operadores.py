# EXERCÍCIO NÚMERO 1
quantidade = float(input("Insira a quantidade de arquivos armazenados: "))
tamanho = float(input("Insira o tamanho médio dos arquivos (MB): "))
volume = quantidade * tamanho
total = volume / 1024
print(f"O espaço total acumulado em GB é: {total}")

# EXERCÍCIO NÚMERO 2
tempo = float(input("Insira o tempo em minutos para serem produzidas: "))
quantidade = float(input("Insira a quantidade que será produzida: "))
total = (tempo * quantidade) / 60
print(f"O tempo em horas de produção será: {total}")

# EXERCÍCIO NÚMERO 3
preco = float(input("Insira o valor do produto: "))
frete = float(input("Insira o valor do frete: "))
quantidade = int(input("Insira a quantidade: "))
total = (preco * quantidade) + frete
print(f"O valor total da compra é: {total}")

# EXERCÍCIO NÚMERO 4
velocidade = float(input("Insira a velocidade da internet em Mbps: "))
tempo = float(input("Insira o tempo de download em segundos: "))
dados = (velocidade / 8) * tempo
print(f"A quantidade de dados transferidos em Megabits foi: {dados}")

# EXERCÍCIO NÚMERO 5
licenca = float(input("Insira o valor da licença: "))
desenvolvedor = float(input("Insira a quantidade de desenvolvedores: "))
total = licenca * desenvolvedor
print(f"O custo total das licenças é: {total}")

# EXERCÍCIO NÚMERO 6
ram = float(input("Insira a quantidade de memória RAM em GB: "))
num = float(input("Insira a quantidade de computadores: "))
total = ram * num
print(f"A quantidade de memória RAM no laboratório é {total} GB")

# EXERCÍCIO NÚMERO 7
pecas = float(input("Insira quantas peças são montadas por minuto: "))
operacao = float(input("Insira o tempo de operação em minutos: "))
total = pecas * operacao
print(f"O total de peças produzidas em minuto são: {total}")

# EXERCÍCIO NÚMERO 8
quantidade = int(input("Insira a quantidade de câmeras: "))
preco = float(input("Insira o preço de cada câmera: "))
instalacao = float(input("Insira o custo de instalação por câmera: "))
total = (quantidade * preco) + (instalacao * quantidade)
print(f"O valor total do custo foi R$ {total}")

# EXERCÍCIO NÚMERO 9
tamanho = float(input("Insira o tamanho do arquivo em MB: "))
quantidade = int(input("Insira a quantidade de arquivos: "))
total = (quantidade * tamanho) / 1024
print(f"O tamanho total em GB é de: {total}")

# EXERCÍCIO NÚMERO 10
mensal = float(input("Insira o valor mensal do servidor: "))
tempo = int(input("Insira o tempo de contrato em meses: "))
total = mensal * tempo
print(f"O valor total pago é de R$ {total} em {tempo} meses")

# EXERCÍCIO NÚMERO 11
tempo = float(input("Insira o tempo de execução em segundos: "))
quantidade = int(input("Insira a quantidade de tarefas executadas: "))
total = (tempo * quantidade) / 60
print(f"O tempo total realizado em minutos é: {total}")

# EXERCÍCIO NÚMERO 12
comprimento = float(input("Insira o comprimento do cabo em metros: "))
quantidade = int(input("Insira a quantidade de cabos: "))
total = comprimento * quantidade
print(f"O comprimento total de cabos instalados é de: {total}")

# EXERCÍCIO NÚMERO 13
tamanho = float(input("Insira o tamanho médio de log em MB: "))
quantidade = float(input("Insira a quantidade de logs gerados por dia: "))
total = tamanho * quantidade
tamanho_total_gb = total / 1024
print(f"O tamanho total de logs gerados em um dia é: {tamanho_total_gb} GB")

# EXERCÍCIO NÚMERO 14
quantidade = int(input("Insira a quantidade de páginas impressas por minuto: "))
tempo = float(input("Insira o tempo em minutos: "))
total = quantidade * tempo
print(f"O total de páginas impressas são: {total}")

# EXERCÍCIO NÚMERO 15
horas = float(input("Insira a quantidade de horas trabalhadas por dia: "))
dias = int(input("Insira a quantidade de dias do projeto: "))
total = horas * dias
print(f"O total de horas trabalhadas são de: {total}")
# EXERCÍCIO NÚMERO 16
consumo = float(input("Insira o consumo de energia de um servidor em watts: "))
quantidade = int(input("Insira a quantidade de servidores: "))
total = consumo * quantidade
print(f"O consumo total de energia é: {total} watts")

# EXERCÍCIO NÚMERO 17
capacidade = float(input("Insira a capacidade de um HD em TB: "))
quantidade = int(input("Insira a quantidade de HDs: "))
total = capacidade * quantidade
print(f"A capacidade total de armazenamento é: {total} TB")

# EXERCÍCIO NÚMERO 18
acessos = int(input("Insira quantos acessos ocorrem por minuto: "))
tempo = int(input("Insira a quantidade de minutos monitorados: "))
total = acessos * tempo
print(f"O total de acessos registrados é: {total}")

# EXERCÍCIO NÚMERO 19
largura = float(input("Insira a largura da tela: "))
altura = float(input("Insira a altura da tela: "))
total = largura * altura
print(f"A área da tela é: {total}")

# EXERCÍCIO NÚMERO 20
base = float(input("Insira o valor base: "))
expoente = float(input("Insira o valor do expoente: "))
total = base ** expoente
print(f"O resultado da potência é: {total}")

# EXERCÍCIO NÚMERO 21
import math

a = float(input("Digite o lado a: "))
b = float(input("Digite o lado b: "))
c = float(input("Digite o lado c: "))
tipo = ["Isósceles", "Equilátero", "Escaleno"][(a == b == c) * 1 + (a != b and b != c and a != c) * 2]
p = (a + b + c) / 2
area = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(f"Tipo do triângulo é: {tipo}")
print(f"Área do triângulo: {area}")


