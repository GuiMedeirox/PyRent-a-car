import sqlite3, os

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

try:
    cursor.execute(""" CREATE TABLE carro ( modelo TEXT, ano INTEGER, placa TEXT ); """)
    cursor.execute(""" CREATE TABLE cliente ( nome TEXT, cpf TEXT); """)
    cursor.execute(""" CREATE TABLE aluguel_dos_clientes ( cpf_cliente TEXT, placa_carro TEXT ); """ )
except: 
    print("database funcionando :) ")

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
    

def createCarro(modelo, ano, placa, cursor ): 
    cursor.execute("INSERT INTO carro (modelo, ano, placa) VALUES (?, ?, ?)",(modelo, ano, placa))

def readCarro(): 
    consulta = cursor.execute("SELECT modelo, placa FROM carro").fetchall()
    for resultado in consulta: 
        print("||" ,resultado[0] ," PLACA " ,resultado[1] ,end=" ")

def updateCarro(placaAlvo):
    edit = int(input("VOCÊ QUER EDITAR O MODELO DO CARRO (1) OU O ANO DELE (2)? \n"))
    if edit == 1: 
        novoModelo = input("Qual o novo modelo do carro? \n")
        cursor.execute("UPDATE carro SET modelo = ? WHERE placa = ?", (novoModelo, placaAlvo))
        connection.commit()
    elif edit == 2: 
        novoAno = input("Qual o novo ano do carro? \n")
        cursor.execute("UPDATE carro SET ano = ? WHERE placa = ?", (novoAno, placaAlvo))
        connection.commit()
    else: 
        print("Opção inválida")

def deleteCarro(placaAlvo):
    cursor.execute("DELETE FROM carro WHERE placa = ?", (placaAlvo,))
    connection.commit()

def createCliente(nome, cpf, cursor):
    cursor.execute("INSERT INTO cliente (nome, cpf) VALUES (?, ?)", (nome, cpf))
    connection.commit()

def readCliente(): 
    consulta = cursor.execute("SELECT nome, cpf FROM cliente").fetchall()
    for resultado in consulta: 
        print("||" ,resultado[0], " CPF: ", resultado[1] ," || ", end=" ")

def updateCliente(opt): 
    if opt == 1: 
        cpfAlvo = input("Digita o CPF da pessoa que será alterado o nome: ")
        novoNome = input("Digita o novo nome: ")
        cursor.execute("UPDATE cliente SET nome = ? WHERE cpf = ?", (novoNome, cpfAlvo))
        connection.commit()
    elif opt == 2: 
        nomeAlvo = input("Digita o nome da pessoa que terá o CPF alterado: ")
        novoCPF = input("Digita o novo CPF: ")
        cursor.execute("UPDATE cliente SET cpf = ? WHERE nome = ?", (novoCPF, nomeAlvo))
        connection.commit()
    else: 
        print("Opção inválida. ")

def deleteClientes(cpfAlvo):
    cursor.execute("DELETE FROM cliente WHERE cpf = ?", (cpfAlvo,))
    connection.commit()

def createAluguel(cpf, placa): 
    cursor.execute("INSERT INTO aluguel_dos_clientes (cpf_cliente, placa_carro) VALUES (?, ?)",(cpf, placa))
    connection.commit()

def readAluguel():
    consulta = cursor.execute("SELECT cpf_cliente, placa_carro FROM aluguel_dos_clientes").fetchall()
    for resultado in consulta: 
        print("|| CPF " ,resultado[0], " placa do carro: ", resultado[1] ," || ", end=" ")

def updateAluguel(edit):
    if edit == 1: 
        placaAlvo = input("Digita a placa que esteja vinculada ao CPF que será alterado:  ")
        novoCPF = input("Agora digite o novo CPF: ")
        cursor.execute("UPDATE aluguel_dos_clientes SET cpf_cliente = ? where placa_carro = ?",(novoCPF, placaAlvo))
        connection.commit()
    elif edit == 2: 
        cpfAlvo = input("Digita o CPF que esteja atrelado à placa que você quer alterar: ")
        novaPlaca = input("Digita a nova placa: ")
        cursor.execute("UPDATE aluguel_dos_clientes SET placa_carro = ? where cpf_cliente = ?",(novaPlaca, cpfAlvo))
        connection.commit() 
    else:                   
        print("Opção inválida")

def deleteAluguel(cpfAlvo): 
    cursor.execute("DELETE FROM aluguel_dos_clientes WHERE cpf = ?",(cpfAlvo,))
    connection.commit()

while True: 
    main()
    option = input("Digita o que você quer visualizar: ")

    if option == "1": 
        os.system("cls || clear")
        readCarro()
    
    elif option == "2": 
        modelo = input("Digita o modelo do carro: ")
        ano = input("Digita o ano do carro: ")
        placa = input("Digita a placa do carro: ")
        createCarro(modelo, ano, placa, cursor)
        connection.commit()

    elif option == "3": 
        placaAlvo = input("Digita a placa do carro que você desejará editar: ")
        updateCarro(placaAlvo)
        
    elif option == "4": 
        placaAlvo = input("DIGITA A PLACA ALVO DO CARRO: ")
        deleteCarro(placaAlvo)

    elif option == "5":  
        os.system("cls || clear")
        readCliente()

    elif option == "6": 
        nome = input("Nome do cliente: ")
        cpf = input("CPF do cliente: ")
        createCliente(nome, cpf, cursor)

    elif option == "7": 
        opt = int(input("O QUE VOCÊ QUER EDITAR, NOME(1) OU CPF(2)? "))
        updateCliente(opt)

    elif option == "8": 
        cpfAlvo = input("DIGITA O CPF DA PESSOA A SER DELETADA: ")
        deleteClientes(cpfAlvo)

    elif option == "9":  
        os.system("cls || clear")
        readAluguel()

    elif option == "10": 
        cpf = input("DIGITA O CPF DA PESSOA QUE IRÁ ALUGAR O VEÍCULO: ")
        placa = input("DIGITE A PLACA DO VEÍCULO A SER ALUGADO: ")
        createAluguel(cpf, placa)

    elif option == "11": 
        edit = int(input("VOCÊ QUER EDITAR CPF(1) OU A PLACA DO CARRO(2)? \n"))
        updateAluguel(edit)

    elif option == "12":
        cpfAlvo = input("Digita o CPF da pessoa que terá o aluguel deletado: ")
        deleteAluguel(cpfAlvo)
    
    elif option == "13": 
        os.system("cls || clear")
        print("Feito por Guilherme de Medeiros Santos")
        print("PyRent-a-Car -> gerencie seus carros alugados usando python!") 
    
    elif option == "14": 
        exit()
