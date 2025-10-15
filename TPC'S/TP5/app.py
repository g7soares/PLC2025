import json
import sys
import tp5 as alex

f=open("stock.json","r")
stock=json.load(f)

saldo = 0
open = True

def get_saldo(saldo):
    ret = 0
    while saldo >= 100: #isto ta em centimos
        saldo -= 100
        ret += 100
    return f'{int(ret/100)}e{int(saldo)}c'

def devolver_troco(saldo):
    moedas = [200, 100, 50, 20, 10, 5, 2, 1] 
    resultado = []

    for moeda in moedas:
        qtd = saldo // moeda
        if qtd > 0:
            saldo -= qtd * moeda
            if moeda >= 100:
                resultado.append(f"{qtd}x {moeda//100}e")
            else:
                resultado.append(f"{qtd}x {moeda}c")

    return "Pode retirar o troco: " + ", ".join(resultado) + "."

for linha in sys.stdin:

    alex.lexer.input(linha)

    for tok in alex.lexer:
        
        if(tok.type == 'LISTAR'):
            saida = "maq:\n"
            saida += "cod  | nome         | quantidade |  preço\n"
            saida += "------------------------------------------------------\n"

            for prod in stock["stock"]:
                saida += f"{prod['cod']}     {prod['nome']}    {prod['quant']}         {prod['preco']}\n"

            saida += "\nSaldo = " + get_saldo(saldo) + "\n" 
            print(saida)

        elif(tok.type == 'VALOR_EURO'):
            saldo += int(tok.value[:-1])*100
        
        elif(tok.type == 'VALOR_CENT'):
            saldo += int(tok.value[:-1])
        
        elif(tok.type == 'FIM_MOEDA'):
            print("maq: Saldo = "+ get_saldo(saldo))

        elif(tok.type == 'SELECIONAR'):
            pass

        elif(tok.type == 'CODIGO'):
            found = False
            for prod in stock["stock"]:
                if prod['cod'] == tok.value and prod['quant'] > 0:
                    found = True
                    if prod['preco']*100 <= saldo:
                        saldo -= int(prod['preco']*100)
                        prod['quant'] -= 1
                        print("maq: Pode retirar o produto dispensado " +  prod['nome'])
                        print('maq: Saldo = ' + get_saldo(saldo))
                    else:
                        print("maq: Saldo insuficiente para satisfazer o seu pedido\n")
                        print("Saldo = " + get_saldo(saldo) + "; Pedido = " + get_saldo(int(prod['preco']*100)))
                    break
            
            if not found:
                print("maq: Produto inexistente\n")
            

        elif(tok.type == 'SAIR'):
            print("maq: " + devolver_troco(saldo))
            print("maq: volte sempre\n")
            open = False

            
    if not open:
        # print("ardeu\n")
        break