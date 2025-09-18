import csv
import json
def ex1():
    linhas = []
    dic = {}
    with open('alunos.csv', mode ='r')as file:
        ficheiro = csv.reader(file)
        i = 0
        for linha in ficheiro:
            if i == 0:
                i = i+1
                continue
            # nome = linha[1]
            # curso = linha[2]
            # notas = [linha[3], linha[4], linha[5], linha[6]]
            dic[linha[0]] = {"nome": linha[1], "curso": linha[2], "notas": linha[3:]}
            # dic = { aluno[0:]:{"nome": linha[1], "curso": linha[2], "notas": linha[3:] } for aluno in ficheiro}
            i = i+1
        
    # print(dic)
    return dic

def media(dic):
    # ret = []
    total = 0
    for aluno_id in dic:  
        aluno = dic[aluno_id]  
        soma = 0
        for nota in aluno["notas"]:
            soma = soma + int(nota)  
        media_aluno = soma / len(aluno["notas"])
        total = total + media_aluno
    total = total / len(dic)
    print(total)
    return total


def estrutura():
    f=open("cinema.json","r")
    dados =json.load(f)
    dic = {} 
    for i in dados["filmes"]:
        dic[i["title"]] = [dic[i["year"]], dic[i["Cast"]], dic[i["genres"]]] 
    print(dic)
        
    










def main():
    try:
        estrutura()
    except FileNotFoundError:
        print("Erro: Arquivo 'alunos.csv' não encontrado.")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()