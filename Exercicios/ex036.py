#Análise de emprestimo

salario = float(input('Informe o seu redimento mensal: '))
valorCasa = float(input('Informe o valor da casa: '))
ano = int(input('Informe em quantos anos vc quer pagar o financiamento: '))

prestacao = valorCasa / (ano * 12)

#Verifica se a prestação é maior que 30% o salário do cliente, caso seja, nega o empréstimo
if prestacao > (salario * 0.3):
    print('\033[41mEmpréstimo Negado\033[m')
else:
    print('\033[42mEmpréstimo aprovado!\033[m')
