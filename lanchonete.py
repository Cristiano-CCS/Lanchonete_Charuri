print("=== Lá no Charuri ===")
print(" "*4, "Lachonete")

nome_cliente = input("Por favor, digite o seu nome: ")
print(f"Olá, {nome_cliente}")

print("=== NOSSO CARDÁPIO ===")
print("1. Hambúrguer Matador - R$39.59")
print("2. Batata Frita - R$9.99")
print("3. Cachorro-quente - R$20.59")

# Recebendo dados do pedido
print("\n Faça o seu pedido")
qtd_hamburguer = int(input("Quantos hamburguers você deseja? "))
qtd_batataFrita = int(input("Quantos porções de batata frita você deseja? "))
qtd_cachorroQuente = int(input("Quantos cachorros quentes você deseja? "))

# Fechando a conta.
total_hamburguer = qtd_hamburguer * 39.59
total_batataFrita = qtd_batataFrita * 9.99
total_cachorroQuente = qtd_cachorroQuente * 20.59

# Exibindo o cupom fiscal.
print("\n" + "="*30)
print(" " * 8 + "CUPOM FISCAL" + " " * 8)
print("=" * 30)
print(f"Cliente: {nome_cliente}")

print(f"Hamburguer Matador: {total_hamburguer}")
print(f"Batata Frita: {total_batataFrita}")
print(f"Cachorro-quente: {total_cachorroQuente}")
print(f"Total do pedido: {total_hamburguer+total_batataFrita+total_cachorroQuente}")