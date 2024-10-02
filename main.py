from pessoa import Pessoa

def main():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    
    pessoa = Pessoa(nome, idade)
    
    ano_nascimento = pessoa.calcular_ano_nascimento()
    print(f"{pessoa.get_nome()}, você nasceu em aproximadamente {ano_nascimento}.")

if __name__ == "__main__":
    main()