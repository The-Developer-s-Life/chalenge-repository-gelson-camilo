"""
Este algoritmo foi sugerido no grupo de programação the developer's life do whatsapp pelo dev. 
Zacarias Capingala Seg. 29-07-2024 e foi desenvolvido por
Gelson A. D. Camilo.

O Programa:
Crie um programa que identifique se um número de telefone é valido.
Exemplos números inválidos:
1 Números que começam, com: +244
2 Números que começam, com: 999, 900, 909
3 Tamanho de caracteres: > 9
4 Primeiro número:  != 9
4 Números validos, que começam: 92, 93, 94, 91, 95, 99"""

iniciaisInvalidas=[244,999,900,909]
iniciaisValidas=[92,93,94,91,95,99]
try:
    numero=int(input('insira o número de telemóvel:'))
    numero=str(numero) 
    print()
    if(int(numero[0:3]) in iniciaisInvalidas):
        print("O número do telemóvel é inválido porque começa com uma inicial inválida")
    elif(len(numero)>9):
        print("O número é inválido pois o tamanho ultrapassa os 9 caracteres")
    elif(numero[0]!='9'):
        print("O número é inválido porque não começa com 9")
    elif(int(numero[0:2]) in iniciaisValidas):
        print("Muito bem, o seu número de telemóvel é válido")
    else:
        print("Por alguma razão não conseguimos validar o seu número")
except:
    print("O número inserido não é válido, tente novamente mais tarde")
    

