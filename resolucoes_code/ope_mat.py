# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

try:
    # Solicitar entrada dos números
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    
    # Solicitar o operador
    operador = input("Digite o operador (+, -, *, /): ")
    
    # Validar operador
    if operador not in ['+', '-', '*', '/']:
        print("Erro: Operador inválido. Use +, -, * ou /")
    else:
        # Realizar a operação
        if operador == '+':
            resultado = numero1 + numero2
        elif operador == '-':
            resultado = numero1 - numero2
        elif operador == '*':
            resultado = numero1 * numero2
        elif operador == '/':
            # Validar divisão por zero
            if numero2 == 0:
                print("Erro: Não é possível dividir por zero!")
            else:
                resultado = numero1 / numero2
                print(f"Resultado: {numero1} {operador} {numero2} = {resultado}")
        
        # Mostrar resultado para as outras operações
        if operador in ['+', '-', '*']:
            print(f"Resultado: {numero1} {operador} {numero2} = {resultado}")

except ValueError:
    print("Erro: Digite números válidos!")
except Exception as e:
    print(f"Erro inesperado: {e}")
