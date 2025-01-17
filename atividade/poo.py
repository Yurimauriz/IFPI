from classes import *

# Criando uma frota
frota_empresa = Frota("Frota da Empresa Teste")

# Criando veículos
carro1 = Veiculo("Fiat Uno", "cj.23",2010)
carro2 = Veiculo("Toyota Corolla","cj.24", 2020)

# Adicionando veículos à frota
frota_empresa.adicionar_veiculo(carro1)
frota_empresa.adicionar_veiculo(carro2)

# Criando motoristas
motorista1 = Motorista("PP", 18 ,"123456789")
motorista2 = Motorista("Yuri", 18, "987654321")

# Associando motoristas aos veículos
carro1.adicionar_motorista(motorista1)
carro2.adicionar_motorista(motorista1)
carro2.adicionar_motorista(motorista2)

# Listando os veículos da frota
frota_empresa.listar_veiculos()
# Listando motoristas dos veículos
carro1.listar_motoristas()
carro2.listar_motoristas()