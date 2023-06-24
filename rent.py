import re

class Carro:
    def __init__(self, modelo, ano, placa):
        self.modelo = modelo
        self.ano = ano
        self.placa = placa

def criar_carro(modelo, ano, placa):
    carro = Carro(modelo, ano, placa)
    with open("carros.txt", "a") as arquivo:
        arquivo.write(f"{carro.modelo},{carro.ano},{carro.placa}\n")

def obter_carros():
    carros = []
    with open("carros.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            dados = linha.strip().split(",")
            carro = Carro(dados[0], dados[1], dados[2])
            carros.append(carro)
    return carros

def atualizar_carro(placa, novo_modelo, novo_ano):
    carros = obter_carros()
    for carro in carros:
        if carro.placa == placa:
            carro.modelo = novo_modelo
            carro.ano = novo_ano
    with open("carros.txt", "w") as arquivo:
        for carro in carros:
            arquivo.write(f"{carro.modelo},{carro.ano},{carro.placa}\n")

def deletar_carro(placa):
    carros = obter_carros()
    carros = [carro for carro in carros if carro.placa != placa]
    with open("carros.txt", "w") as arquivo:
        for carro in carros:
            arquivo.write(f"{carro.modelo},{carro.ano},{carro.placa}\n")

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

def validar_cpf(cpf):
    cpf = re.sub('[^0-9]', '', cpf)

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    soma = 0
    peso = 10
    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1

    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0

    if resto != int(cpf[9]):
        return False

    soma = 0
    peso = 11
    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1

    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0

    if resto != int(cpf[10]):
        return False

    return True

def criar_cliente(nome, cpf):
    if validar_cpf(cpf):
        cliente = Cliente(nome, cpf)
        with open("clientes.txt", "a") as arquivo:
            arquivo.write(f"{cliente.nome},{cliente.cpf}\n")
    else:
        print("CPF inválido.")

def obter_clientes():
    clientes = []
    with open("clientes.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            dados = linha.strip().split(",")
            cliente = Cliente(dados[0], dados[1])
            clientes.append(cliente)
    return clientes

def atualizar_cliente(cpf, novo_nome):
    clientes = obter_clientes()
    for cliente in clientes:
        if cliente.cpf == cpf:
            cliente.nome = novo_nome
    with open("clientes.txt", "w") as arquivo:
        for cliente in clientes:
            arquivo.write(f"{cliente.nome},{cliente.cpf}\n")

def deletar_cliente(cpf):
    clientes = obter_clientes()
    clientes = [cliente for cliente in clientes if cliente.cpf != cpf]
    with open("clientes.txt", "w") as arquivo:
        for cliente in clientes:
            arquivo.write(f"{cliente.nome},{cliente.cpf}\n")

class Aluguel:
    def __init__(self, cpf, placa):
        self.cpf = cpf
        self.placa = placa

def criar_aluguel(cpf, placa):
    clientes = obter_clientes()
    carros = obter_carros()

    cpf_existe = False
    for cliente in clientes:
        if cliente.cpf == cpf:
            cpf_existe = True
            break

    placa_existe = False
    for carro in carros:
        if carro.placa == placa:
            placa_existe = True
            break

    if not cpf_existe or not placa_existe:
        print("CPF ou placa não encontrados.")
        return

    aluguel = Aluguel(cpf, placa)
    with open("alugueis.txt", "a") as arquivo:
        arquivo.write(f"{aluguel.cpf},{aluguel.placa}\n")

def obter_alugueis():
    alugueis = []
    with open("alugueis.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            dados = linha.strip().split(",")
            aluguel = Aluguel(dados[0], dados[1])
            alugueis.append(aluguel)
    return alugueis

def atualizar_aluguel(cpf, nova_placa):
    alugueis = obter_alugueis()
    for aluguel in alugueis:
        if aluguel.cpf == cpf:
            aluguel.placa = nova_placa
    with open("alugueis.txt", "w") as arquivo:
        for aluguel in alugueis:
            arquivo.write(f"{aluguel.cpf},{aluguel.placa}\n")

def deletar_aluguel(cpf):
    alugueis = obter_alugueis()
    alugueis = [aluguel for aluguel in alugueis if aluguel.cpf != cpf]
    with open("alugueis.txt", "w") as arquivo:
        for aluguel in alugueis:
            arquivo.write(f"{aluguel.cpf},{aluguel.placa}\n")

def main(): 
    print("\nPyRent-a-car") 
    print("01 - LISTAR OS CARROS CADASTRADOS")
    print("02 - CADASTRAR UM CARRO ")
    print("03 - EDITAR UM CARRO CADASTRADO ")
    print("04 - DELETAR UM CARRO ")
    print("05 - LISTAR OS CLIENTES CADASTRADOS")
    print("06 - CADASTRAR UM CLIENTE")
    print("07 - EDITAR INFORMAÇÕES DE UM CLIENTE")
    print("08 - DELETAR UM CLIENTE")
    print("09 - LISTAR ALUGUEIS")
    print("10 - ALUGAR UM CARRO")
    print("11 - EDITAR ALUGUEL DE CARRO")
    print("12 - DELETAR ALUGUEL")
    print("13 - SOBRE O PROJETO") 
    print("14 - SAIR")

while True: 
  main()
  option = int(input("\n Digita a opção: "))

  if (option == 1): 
    obter_carros()
  elif (option == 2):
    modelo = input("Digita o modelo do carro: ")
    ano = input("Digita o ano do carro: ")
    placa = input("Digita a placa do carro: ")
    criar_carro(modelo,ano, placa)
  elif (option == 3): 
    placa = input("\n Placa do carro a ser editado: ")
    modelo = input("\n Novo modelo: ")
    ano = input("\n Novo ano: ")
    atualizar_carro(placa,modelo,ano)
  elif (option == 4): 
    placa = input("\n Placa do carro: ")
    deletar_carro(placa)
  elif (option == 5): 
    obter_clientes()
  elif (option == 6): 
    nome = input("\nNome do cliente: ")
    cpf = input("\nCPF do cliente: ")
    criar_cliente(nome,cpf)
  elif (option == 7):
    cpf = input("\nCPF do cliente a ser editado: ")
    nome = input("\nNovo nome: ")
    atualizar_cliente(cpf,nome)
  elif (option == 8): 
    cpf = input("\nDigita o CPF do cliente a ser deletado: ")
    deletar_cliente(cpf)
  elif (option == 9): 
    obter_alugueis()
  elif (option == 10): 
    cpf = input("\n CPF do cliente: ")
    placa = input("\n Placa do carro: ")
    criar_aluguel(cpf,placa)
  elif (option == 11): 
    cpf = input("\nInforme o CPF do cliente que terá o veículo editado: ")
    placa = input("\n Informe a nova placa: ")
    atualizar_aluguel(cpf,placa)
  elif (option == 12): 
    cpf = input("\n Informe o CPF que terá o aluguel deletado: ")
    deletar_aluguel(cpf)
  elif (option == 13): 
        print("Feito por Guilherme de Medeiros Santos")
        print("PyRent-a-car: o melhor amigo da locadora de veículos!") 
  elif (option == 14): 
    exit()
