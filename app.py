import random

saudacao = ("Olá, seja bem vindo!")
nome = input("Como você se chama ? ")
idade = int(input(f"Muito prazer {nome}, eu me chamo Brenda! E me diga, quantos anos você tem ?" ))

if idade <=17: 
    print(f"É muito legal ter você aqui conosco, {nome} ,mas você precisará comparecer com um responsável por ter {idade} anos sendo menor de idade, combinado ?") 
else: 
    resposta = input("Legal, e como você ficou sabendo da nossa feira cultural ? (instagram, facebook, whatsapp, amigos, escola, trabalho ou outros")

    redes_sociais = ["Instagram", "Facebook", "WhatsApp"]
    amigos = "amigos"
    familia = "família"
    escola = "escola"

    def gerar_informacao():
     informacoes = [f"{redes_sociais} {amigos} {familia}"]
     return random.choice(informacoes)


    resposta = input(f"Que bom saber disso ;) ! Beleza {nome}, então vamos dar início as explicações, você está pronto(a) ? (sim/não)")



if resposta.lower() == "sim":
 print("Fechooou ! Bora lá")

else: 
 print("Ah entendi, que pena ! Mas nos vemos em breve ;)")
