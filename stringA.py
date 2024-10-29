def verificarLetraA(string):
    quantidadeA = string.lower().count('a')
    
    if quantidadeA > 0:
        print(f"A letra a aparece {quantidadeA} vezes na string.")
    else:
        print("A letra a não está presente na string.")

string = input("Digite uma string: ")
verificarLetraA(string)