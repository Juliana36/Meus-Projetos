saldo = float(500)
historico_deposito = []  #para criar um historico dos depositos
historico_saque = []  #para criar um historico dos saques
mensagem = f'''
    --------------------------------- 
            [A] SACAR
            [B] DEPOSITAR
            [C] VER EXTRATO
            [G] SAIR
    ---------------------------------  
      '''

print(mensagem)
resposta = input("O que você deseja fazer? ").upper()

while resposta != "G":

    if resposta == "A":
        saque = float(input('Quanto deseja sacar?'))

        if saldo == 0:
            print('Sem Saldo em Conta. ')

        elif saque > saldo and 0 > saldo:
           print('Saldo insuficiente.')
        
        elif saque < 0:
            print('Não é possivél efetuar esse saque')

        elif saque > 500:
            print('Limite de saque é R$500,00.')

        elif len(historico_saque) > 2:
            print("Não é possível realizar o saque. \n Apenas 3 saques por dia.")

        else:
            saldo -= saque
           
            historico_saque.append(saque)
            

    
    elif resposta == 'B':
        deposito = float(input('Quanto deseja depositar?'))
      
        if deposito > 0:
            historico_deposito.append(deposito)
            saldo += deposito

        else:
            print('Número inválido. Tente novamente.')

         
    
    
    elif resposta == 'C':
        for index, valor in enumerate(historico_saque): #para criar uma lista uma embaixo do outra dos saques
            print(f"Extrato dos Saques: {index + 1}: R${valor:.2f}") #isso vai enumerando cada saque enquanto coloca o valor.

        print('----------------------------') #para dar um espaçamento
    
        for index, valor in enumerate(historico_deposito): #para criar uma lista uma embaixo do outra dos depositos
            print(f"Extrato dos Depositos : {index + 1}: R${valor:.2f}") #isso vai enumerando cada deposito enquanto coloca o valor.
        print('-----------------------------') #para dar um espaçamento

        print(f'Atualmente seu saldo é de R${saldo:.2f}')


    else:
        print ("Não é possivel")

    print(mensagem)
    resposta = input("O que você deseja fazer? ").upper()
    
    
print('saindo do programa')