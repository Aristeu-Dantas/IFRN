# faça um programa que recebe a largura e altura de uma parede em centímetros e o rendimento de
# uma determinada tinta medido em m2/litro e calcule quantos litros de tinta serão necessários para pintá-la com duas demãos

largura = float(input('Largura(cm): '))/10000
altura = float(input('Altura(cm): '))/10000
rendimento = float(input('Rendimento(m²): '))
area = altura*largura
litros_tinta = 2*area/rendimento
print(f'voce usara {litros_tinta:.2f} galões de tinta.')
