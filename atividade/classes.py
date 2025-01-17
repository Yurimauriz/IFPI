class Frota:
    def __init__(self, nome_frota): 
        # Função para definir o nome da frota e criar uma lista vazia para adicionar os veiculos       
        self.nome_frota = nome_frota
        self.veiculos = []  # Composição: Frota contém diretamente objetos da classe Veículo

    def adicionar_veiculo(self,veiculo): 
        # Função para adicionar um veiculo a frota
        self.veiculos.append(veiculo)  #append serve para adicionar um item ao final de uma lista
        print(f"O veículo {veiculo.modelo} foi adicionado a {self.nome_frota}")
       
    def listar_veiculos(self): 
        # Função serve para listar todos veiculos na frota
        print(f"Veículos da frota {self.nome_frota}:")
        for veiculo in self.veiculos:
            print(f"Modelo:{veiculo.modelo} com a placa:{veiculo.placa} do ano:{veiculo.ano}")

class Veiculo:
    def __new__(cls, *args, **kwargs):
         #new é um metodo especial para controle de intâncias

        print(f"Instanciando um novo objeto da classe {cls.__name__}.")
        return super().__new__(cls)
    
    def __init__(self, modelo, placa, ano): 
        # Função serve para adicionar um veiculo
        self.modelo = modelo
        self.placa = placa
        self.ano = ano
        self.motorista = [] # Agregação: Motoristas podem ser associados ao veículo

    def adicionar_motorista(self, motorista): 
        # Função serve para adicionar um motorista ao veiculo
        self.motorista.append(motorista) #append serve para adicionar um item ao final de uma lista
        print(f"O motorista {motorista.nome} foi adicionado ao veículo {self.modelo}")

    def listar_motoristas(self): 
        # Função serve para listar os motorista associados ao veiculo
        print(f"Motoristas do veículo {self.modelo}:")
        for motorista in self.motorista:
            print(f"{motorista.nome} com a CNH {motorista.cnh}.") 

class Motorista: 
    def __init__(self, nome, idade, cnh):
         # Função serve para adicionar um motorista
        self.nome = nome
        self.idade = idade
        self.cnh = cnh

