# Média de aprovação = 7
print("=== SISTEMA ESCOLAR ===")
nota = float(input("Informe a nota do aluno: "))
aluno = "Wagner"
if nota >= 7:
    print(f"{aluno}, você está aprovado")
elif nota >= 5:
    print(f"{aluno}, você está recuperação")
else:
    print("REPROVADO")
