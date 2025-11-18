def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero!")
    return a / b

def potencia(a, b):
    return a ** b

def calculate(a, b, op):
    """Função usada pelos testes unitários, integração e E2E"""
    if op == "+":
        return somar(a, b)
    elif op == "-":
        return subtrair(a, b)
    elif op == "*":
        return multiplicar(a, b)
    elif op == "/":
        return dividir(a, b)
    elif op == "^":
        return potencia(a, b)
    else:
        return "Operação inválida!"


# Interface opcional no terminal
def calculadora():
    print("=== CALCULADORA PYTHON ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Potência")
    print("0 - Sair")

    while True:
        opcao = input("\nEscolha uma opção: ")

        if opcao == "0":
            print("Encerrando calculadora...")
            break

        if opcao not in ["1", "2", "3", "4", "5"]:
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
            try:
                resultado = dividir(a, b)
            except ValueError as e:
                print(e)
                continue
        elif opcao == "5":
            resultado = potencia(a, b)

        print(f"Resultado: {resultado}")


if __name__ == "__main__":
    calculadora()
