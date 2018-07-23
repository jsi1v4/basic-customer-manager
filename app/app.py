#By jose silva
import funcs

print("Create by Jose Silva...")


def menu():
    print("\n\n|----- Menu: -----|\n\n" +
        "1) Consulta geral \n" +
        "2) Consulta por nome \n" +
        "3) Consulta por CPF-CNPJ \n" +
        "  ____________________  \n\n" +
        "4) Inserir novo registro \n" +
        "5) Editar registro \n" +
        "6) Deletar registro \n" +
        "  ____________________  \n\n" +
        "7) Subtotais com Soma \n" +
        "8) Subtotais com Media \n" +
        "  ____________________  \n\n" +
        "0) Para sair... \n" +
        "menu) Para voltar ao menu... \n"
        )


def options():
    opt = raw_input("\n >>> Entre com o numero da opcao desejada: ")

    if opt == 'menu':
        menu()
        try_option()

    elif opt == '0':
        exit

    elif opt == '1':
        funcs.exeConsAll()
        try_option()

    elif opt == '2':
        funcs.exeConsByName()
        try_option()

    elif opt == '3':
        funcs.exeConsByCPF()
        try_option()

    elif opt == '4':
        funcs.exeInsert()
        try_option()

    elif opt == '5':
        funcs.exeEdit()
        try_option()

    elif opt == '6':
        funcs.exeDelete()
        try_option()

    elif opt == '7':
        funcs.optSum()
        try_option()

    elif opt == '8':
        funcs.optAvg()
        try_option()

    else:
        print("Entre com uma opcao valida!")
        try_option()


def try_option():
    try:
        options()
    except ValueError:
        print(" \n Erro: Entre com uma opcao valida! \n")
        try_option()
    except NameError:
        print(" \n Erro: Entre com uma opcao valida! \n")
        try_option()
    except SyntaxError:
        print(" \n Erro: Entre com uma opcao valida! \n")
        try_option()


#begin
menu()
try_option()


#end
print("end...")