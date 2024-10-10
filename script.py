import pywhatkit as kit
import time

# Função para ler o arquivo de contatos
def ler_contatos(arquivo_contatos):
    with open(arquivo_contatos, 'r') as file:
        contatos = [linha.strip() for linha in file.readlines()]
    return contatos

# Função para ler a mensagem de um arquivo
def ler_mensagem(arquivo_mensagem):
    with open(arquivo_mensagem, 'r') as file:
        mensagem = file.read().strip()
    return mensagem

# Função para ler o horário de envio de um arquivo
def ler_horario(arquivo_horario):
    with open(arquivo_horario, 'r') as file:
        horario = file.read().strip()
        hora, minuto = map(int, horario.split(':'))
    return hora, minuto

# Arquivos externos
arquivo_contatos = 'contatos.txt'
arquivo_mensagem = 'mensagem.txt'
arquivo_horario = 'horario.txt'

# Lê os contatos, a mensagem e o horário de envio
numeros_telefone = ler_contatos(arquivo_contatos)
mensagem = ler_mensagem(arquivo_mensagem)
hora_envio, minuto_envio = ler_horario(arquivo_horario)

# Envia a mensagem para cada número
for numero in numeros_telefone:
    try:
        kit.sendwhatmsg(numero, mensagem, hora_envio, minuto_envio)
        print(f"Mensagem enviada para {numero} às {hora_envio}:{minuto_envio}")
        time.sleep(60)  # Pausa de 60 segundos entre os envios
        minuto_envio += 2  # Incrementa 2 minutos para o próximo envio
    except Exception as e:
        print(f"Ocorreu um erro ao enviar a mensagem para {numero}: {str(e)}")
