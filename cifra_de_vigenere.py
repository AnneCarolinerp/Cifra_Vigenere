#Base do alfabeto
base = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Função encriptar mensagem
#Função encriptar recebe um texto e uma chave
def encrypt(text, key):
  #Variável vazia que mostrará o texto encriptado
  text_encrypt = ''

  #Incialização de uma variavel que indica onde estou no texto / para quando terminar o texto
  i = 0
  #Percorrer cada letra do texto informado
  for letter in text:
    #Formula onde percorre cada primeira letra do texto com a primeira letra da chave e não permite que a chave seja maior do que o texto
    sum = base.index(letter) + base.index(key[i % len(key)])
    #Converte a formula em inteiro e guarda o valor do resto da divisão com base no alfabeto
    module = int(sum) % len(base)
    #Pega as posições, converte em string e cifra o texto
    text_encrypt = text_encrypt + str(base[module])
    #Para incrementar as letras e continuar percorrendo o texto e a chave
    i+=1

  #Retorna o resultado da função
  return text_encrypt

#Função decriptar mensagem
#Função decriptar recebe o texto encriptado e a chave usada para encriptar
def decipher(text_encrypt, key):
  #Variavel vazia que mostrará o texto decriptado
  text_decipher = ''

  #Incialização de uma variavel de 
  i = 0
  #Percorrer cada letra do texto informado
  for letter in text_encrypt:
    #Formula onde percorre cada primeira letra do texto com a primeira letra da chave e não permite que a chave seja maior do que o texto
    sum = base.index(letter) - base.index(key[i % len(key)])
    #Converte a formula em inteiro e guarda o valor do resto da divisão com base no alfabeto
    module = int(sum) % len(base)
    #Pega as posições, converte em string e cifra o texto
    text_decipher = text_decipher + str(base[module])
    #Para incrementar as letras e continuar percorrendo o texto e a chave
    i+=1

  #Retorna o resultado da função
  return text_decipher

#Função para guardar as opções do menu
def menu():
    print("\n**** Menu ****")
    print("[1] Criptografar Texto")
    print("[2] Descriptografar Texto")

#Função Principal
def main():
  #Opção no qual será atribuido as opções do menu
  option = 1

  #Laço de repetição para escolher a opção de criptografar ou descriptografar a mensagem automaticamente
  while option != 0:
    #Chamada da função onde está as opções do menu
    menu()
    #Variavel que irá armazenar a opção do menu escolhida
    option = int(input("\nEntre com número da opção: "))

    if option == 1:
      print("[1] Criptografar Texto\n")
      #Entrada da mensagem que quer cifrar ou decifrar
      text = str(input("Digite a mensagem: \n")).lower()
      #Entrada da chave utilizada para cifrar
      key = str(input("\nDigite a chave de criptografia:\n")).lower()
      #Variavel que recebe o texto encriptado para retornar o valor original no print
      encrypted = encrypt(text, key)
      #Mostrar na tela o texto criptografado
      print("Texto encriptado:\n",encrypt(text,key))
      
    elif option == 2:
      #Entrada da mensagem que quer cifrar ou decifrar
      text = str(input("Digite a mensagem: \n")).lower()
      #Entrada da chave utilizada para cifrar
      key = str(input("\nDigite a chave de criptografia: \n")).lower()
      #Variavel que recebe o texto encriptado para retornar o valor original no print
      txt_decipher = decipher(text, key)
      #Mostrar na tela o texto original
      print("O texto original é:", txt_decipher)

main()