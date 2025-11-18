def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def calculadora():
    print("=== CALCULADORA PYTHON ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")

    while True:
        opcao = input("\nEscolha uma opção: ")

        if opcao == "0":
            print("Encerrando calculadora...")
            break

        if opcao not in ["1", "2", "3", "4"]:
            print("Opção inválida, tente novamente!")
            continue

        try:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Digite apenas números!")
            continue

        if opcao == "1":
            resultado = somar(a, b)
        elif opcao == "2":
            resultado = subtrair(a, b)
        elif opcao == "3":
            resultado = multiplicar(a, b)
        elif opcao == "4":
            resultado = dividir(a, b)

        print(f"Resultado: {resultado}")

# Executa a calculadora
calculadora()
