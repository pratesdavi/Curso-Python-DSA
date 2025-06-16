def calcular(numero1, numero2, operacao):
    """
    Realiza uma operação matemática entre dois números.

    Parâmetros:
        numero1 (float): O primeiro número.
        numero2 (float): O segundo número.
        operacao (str): A operação desejada (+, -, *, /).

    Retorna:
        float ou str: O resultado da operação, ou uma mensagem de erro.
    """
    if operacao == '+':
        return numero1 + numero2
    elif operacao == '-':
        return numero1 - numero2
    elif operacao == '*':
        return numero1 * numero2
    elif operacao == '/':
        if numero2 == 0:
            return 'Erro: divisão por zero'
        return numero1 / numero2
    else:
        return 'Operação inválida'

# Bloco principal do programa
if __name__ == "__main__":
    try:
        # Entrada de dados do usuário
        numero1 = float(input('Digite o primeiro número: '))
        numero2 = float(input('Digite o segundo número: '))
        operacao = input('Selecione uma operação (+, -, *, /): ').strip()

        # Chamada da função de cálculo
        resultado = calcular(numero1, numero2, operacao)

        # Exibição do resultado
        print(f'Resultado: {resultado}')

    except ValueError:
        # Tratamento de erro para entradas não numéricas
        print('Erro: entrada inválida. Certifique-se de digitar números válidos.')
