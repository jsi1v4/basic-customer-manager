#By jose silva
import mod_database

# functions
def exeConsAll():
    mod_database.tableAll()

def exeConsByName():
    name = raw_input(" ... Entre com o nome desejado: ")
    mod_database.tableByName(name)

def exeConsByCPF():
    cpf = raw_input(" ... Entre com o CPF/CPNJ desejado: ")
    mod_database.tableByCpf(cpf)

def exeInsert():
    nome = raw_input(" ... Nome: ")
    cpf = raw_input(" ... CPF/CPNJ: ")
    isActive = raw_input(" ... Ativo? (0='Nao' | 1='Sim'): ")
    vlTotal = raw_input(" ... Valor Inicial: ")
    mod_database.insertTable(nome, cpf, isActive, vlTotal)

def exeDelete():
    sID = raw_input(" ... ID: ")
    mod_database.deleteByID(sID)

def exeEdit():
    sID = raw_input(" ... Qual ID, voce gostaria de editar? ")
    print("dados...")
    nome = raw_input(" ... Nome: ")
    cpf = raw_input(" ... CPF/CPNJ: ")
    isActive = raw_input(" ... Ativo? (0='Nao' | 1='Sim'): ")
    vlTotal = raw_input(" ... Valor Inicial: ")
    mod_database.editByID(sID, nome, cpf, isActive, vlTotal)


#Subtotais
def optSum():
    print("\n ...Subtotais com soma...")
    
    arg1 = raw_input(" ... Entre o ID: ")
    arg2 = raw_input(" ... E o ID: ")
    arg3 = raw_input(" ... Valores maior que (Opcional): ")
    if (not arg1) or (not arg2):
        print("Operacao invalida!")
    else:
        mod_database.tableSUM(arg1, arg2, arg3)

def optAvg():
    print("\n ...Subtotais com media...")

    arg1 = raw_input(" ... Entre o ID: ")
    arg2 = raw_input(" ... E o ID: ")
    arg3 = raw_input(" ... Valores maior que (Opcional): ")
    if (not arg1) or (not arg2):
        print("Operacao invalida!")
    else:
        mod_database.tableAVG(arg1, arg2, arg3)