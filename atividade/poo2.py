# É apenas teste
from classes import *

# Criando uma frota
frota_empresa = Frota(input("Digite o nome da frota: "))

# Criando veículos
carro1 = Veiculo(input("Digite o nome do carro: "), input("Digite a cor do carro: "), input("Digite a placa do carro: "))
carro2 = Veiculo(input("Digite o nome do carro: "), input("Digite a cor do carro: "), input("Digite a placa do carro: "))

# Adicionando veículos à frota
frota_empresa.adicionar_veiculo(carro1)
frota_empresa.adicionar_veiculo(carro2)

# Criando motoristas
motorista1 = Motorista(input("Digite o nome do motorista: "), int(input("Digite a idade do motorista: ")), input("Digite a CNH do motorista: ") )
motorista2 = Motorista(input("Digite o nome do motorista: "), int(input("Digite a idade do motorista: ")), input("Digite a CNH do motorista: ") )

# Associando motoristas aos veículos
carro1.adicionar_motorista(motorista1)
carro2.adicionar_motorista(motorista1)
carro2.adicionar_motorista(motorista2)

# Listando os veículos da frota
frota_empresa.listar_veiculos()
# Listando motoristas dos veículos
carro1.listar_motoristas()
carro2.listar_motoristas()
