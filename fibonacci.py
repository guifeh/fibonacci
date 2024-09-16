def fibonacci(n):
    """Gera a sequência de Fibonacci até o número 'n'."""
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence

def pertence_fibonacci(num):
    """Verifica se o número informado pertence à sequência de Fibonacci."""
    if num < 0:
        return False
    fib_sequence = fibonacci(num)
    return num in fib_sequence

def main():
    """Função principal para execução do programa."""
    while True:
        try:
            numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
            if pertence_fibonacci(numero):
                print(f"O número {numero} pertence à sequência de Fibonacci.")
            else:
                print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
        except ValueError:
            print("Por favor, insira um número inteiro válido.")
        
        # Pergunta se o usuário deseja continuar ou sair
        continuar = input("Deseja verificar outro número? (Digite 's' para continuar ou qualquer outra tecla para sair): ")
        if continuar.lower() != 's':
            break

    print("Programa encerrado. Pressione qualquer tecla para sair.")
    input()  # Aguarda o usuário pressionar uma tecla para encerrar

if __name__ == "__main__":
    main()
