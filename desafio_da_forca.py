#conecta este computador com seu Google Drive
from google.colab import drive
drive.mount('/content/drive')

#instala a biblioteca unidecode
!pip install unidecode

from IPython.core.interactiveshell import import_item

#importa bibliotecas
import getpass
import random
from unidecode import unidecode

#abre o arquivo contido no Google Drive conectado acima através do caminho especificado abaixo
with open('/content/drive/MyDrive/trabalho/trabalho.txt', 'r') as f:
    conteudo = f.read()

#caso o usuário queira arriscar a palavra secreta de uma única vez
def arrisca_tudo():
  while True:
    global erros
    global tamanho
    palavra_completa = input("\nChute a palavra completa, lembrando que nessa etapa tudo é aceito! Insira o seu palpite: ")
    palavra_completa = palavra_completa.lower()
    palavra_completa = unidecode(palavra_completa)
    if len(palavra_completa) != len(palavra_sorteada):
      print("\nPalavra possui mais caracteres do que necessário! A palavra secreta possui %i caracter(es)." %len(palavra_sorteada))
    else:
      if palavra_completa in palavra_sorteada:
        tamanho = len(palavra_sorteada)
      else:
        erros = 0
      break

#verifica se a palavra que o usuário inseriu contém na palavra secreta
def verifica_chute(letra):
  global erros
  global tamanho
  global chutes
  acertos = 0
  chutes += letra
  for i in range(len(palavra_sorteada)):
    if letra == palavra_sorteada[i]:
      lista[i] = letra
      acertos += 1
      tamanho += 1
  if acertos == 0:
    erros -= 1
    print("Você errou! Ainda lhe restam %i chance(s) para chute!\n" %erros)
  else:
    print("Você acertou!")
    print(lista)
    print("\n")

#verifica se a letra que o usuário chutou é válida para o jogo. Caso esteja ok, ele chama a função verifica_chute
#Aqui também se pergunta se o usuário deseja chutar de uma vez a palavra secreta, chamando a função arrisca_tudo
def verifica_letra(letra): 
  if letra == " " or letra == "" or letra == '0' or letra == "1" or letra == '2' or letra == '3' or letra == '4' or letra == '5' or letra == '6' or letra == '7' or letra == '8' or letra == '9':
    print("Caracter inválido! Isso não é uma letra, tente novamente.\n")
  elif len(letra) != 1:
    while True:
      arrisca = input("""\nHummm, vi que você chutou mais de um caractere. 
Aqui jogamos no tudo ou nada!!!
Aperte 1 para chutar a palavra toda ou 0 para continuar chutando letra por letra.""")
      if arrisca == "1" or arrisca == "0" :
        if arrisca == '0':
          break
        else:
          arrisca_tudo()
          break
      else:
        print("Erro no valor digitado! Tente novamente.\n")

  elif letra in chutes:
    print("Você já chutou essa opção! Tente novamente.\n")
  else:
    verifica_chute(letra)

#roda o jogo
def inicia_jogo():
  while erros>0 and tamanho<len(palavra_sorteada):
    letra = input("Insira a letra que deseja chutar: ")
    letra = unidecode(letra).lower()
    verifica_letra(letra)

#cria a forca que será impressa na tela e na qual substituiremos as palavras conforme encontradas
def cria_forca(palavra_sorteada):
  for i in range(len(palavra_sorteada)):
    lista.append("_")
  print(lista)
  print("A palavra possui %i caracteres. BOA SORTE!!!\n\n" %(len(palavra_sorteada)))

#apresentação das regras do jogo
def apresentacao ():
  print("""
Seja bem-vindo ao Jogo da Forca!
Você escolheu o modo 1 player, então sortearemos uma palavra aleatória para você!\n
************************************************************************************
Se liga nas regras do jogo:
  --> O objetivo deste jogo é descobrir uma palavra adivinhando suas letras.
  --> Você terá seis chances de erro para acertar a palavra antes de ser enforcado.
  --> Lembrando que removeremos caracteres especiais e acentos.\n
************************************************************************************\n""")

#inicia o menu com as opções de como o usuário quer jogar ou sair do jogo
def chama_menu():
  global menu
  while True:
    menu = input("Digite 1 para modo um player, 2 para o modo dois players e 0 para encerrar jogo: ")
    if menu == "1" or menu == "0" or menu == "2":
      return menu
      break
    else:
      print("Erro no valor digitado! Tente novamente.\n")

#parte final do jogo que retorna a mensagem se ganhou ou perdeu
def mensagem_final():
  if erros == 0:
    caveira = "\U0001F480"
    print(f"\n{caveira*3} Você foi enforcado! A palavra sorteada foi {palavra_sorteada}, tente novamente! {caveira*3}\n")
    print("Deseja jogar novamente?")
  else:
    trofeu = "\U0001F3C6"
    print(f"\n{trofeu*3} Você acertou a palavra! Parabéns, você ganhou o jogo! {trofeu*3}\n")
    print("Deseja jogar novamente?")

while True:
  lista = []
  erros = 6
  tamanho = 0
  chutes = ""
  chama_menu()

  if menu == "1":
    apresentacao()
    palavra_sorteada = random.choice(conteudo.split("\n"))
    palavra_sorteada = palavra_sorteada.lower()
    palavra_sorteada = unidecode(palavra_sorteada)
    cria_forca(palavra_sorteada)
    inicia_jogo()
    mensagem_final()

  elif menu == "2":
    apresentacao()
    palavra_sorteada = getpass.getpass("Digite a palavra secreta: ")
    palavra_sorteada = palavra_sorteada.lower()
    palavra_sorteada = unidecode(palavra_sorteada)
    cria_forca(palavra_sorteada)
    inicia_jogo()
    mensagem_final()

  else:
    print("\nAgradecemos sua participação no jogo! Até a proxima.")
    break