totalVendas = float(input("Quantos reais vai vender? "))
margemLucro = float(input("Margem de lucro total das vendas (porcentagem): "))
lucroTotal = float(totalVendas/100 * margemLucro)
print("O lucro total é de R$ %.2f" %lucroTotal)
