print("RADAR DE TRANSITO")
velocidade = int(input("Informe a velocidade do carro"))
limite = 100
if velocidade > limite:
    km_acima = velocidade - limite
    valor_da_multa = km_acima * 5.00
    print("Multado por execesso de velocidade")
    print(f"Sua multa é de R$ {valor_da_multa}")

