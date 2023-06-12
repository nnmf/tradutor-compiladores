aux = []
indentation = ""


def iniciar_tradutor(auxiliar, string):
    global aux

    def decision():
        print("topo da lista auxiliar do tradutor: " + aux[-1])
        if aux[-1] == "print":
            escrever_print()
        elif aux[-1] == "fun":
            escrever_fun()
        elif aux[-1] == "var":
            escrever_var()
        elif aux[-1] == "while":
            escrever_while()
        elif aux[-1] == "if":
            escrever_if()
        else:
            escrever_programa()

    def escrever_print():
        global aux
        with open("./testes/programa.py", "a") as arquivo:
            arquivo.write(auxiliar)
            if string == ";":
                arquivo.write(")\n")
                aux.pop()
            elif string == "print":
                arquivo.write(indentation + string + "(")
            else:
                escrever_programa()

    def escrever_fun():
        global aux, indentation
        with open("./testes/programa.py", "a") as arquivo:
            arquivo.write(auxiliar)
            if string == "}":
                arquivo.write("\n")
                indentation = indentation[: -1]
                aux.pop()
            elif string == "{":
                arquivo.write(":" + "\n")
                indentation = indentation + " "
            elif string == "(":
                arquivo.write("(")
            elif string == ")":
                arquivo.write(")")
            elif string == ";":
                arquivo.write("\n")
            elif string == "fun":
                arquivo.write("def ")
            else:
                escrever_programa()

    def escrever_var():
        global aux
        with open("./testes/programa.py", "a") as arquivo:
            arquivo.write(auxiliar)
            if string == ";":
                arquivo.write("\n")
                aux.pop()
            elif string == "var":
                arquivo.write(indentation + "")
            else:
                escrever_programa()

    def escrever_while():
        global aux, indentation
        with open("./testes/programa.py", "a") as arquivo:
            arquivo.write(auxiliar)
            if string == "}":
                arquivo.write("\n")
                indentation = indentation[: -1]
                aux.pop()
            elif string == "{":
                arquivo.write(":" + "\n")
                indentation = indentation + " "
            elif string == "(":
                arquivo.write(" ")
            elif string == ")":
                arquivo.write("")
            elif string == ";":
                arquivo.write("\n")
            else:
                escrever_programa()

    def escrever_if():
        global aux, indentation
        with open("./testes/programa.py", "a") as arquivo:
            arquivo.write(auxiliar)
            if string == "}":
                arquivo.write("\n")
                indentation = indentation[: -1]
                aux.pop()
            elif string == "{":
                arquivo.write(":" + "\n")
                indentation = indentation + " "
            elif string == "(":
                arquivo.write(" ")
            elif string == ")":
                arquivo.write("")
            elif string == ";":
                arquivo.write("\n")
            else:
                escrever_programa()

    def escrever_programa():
        global aux, indentation
        with open("./testes/programa.py", "a") as arquivo:
            arquivo.write(auxiliar)
            if string == "}":
                arquivo.write("\n")
                indentation = indentation[: -1]
                aux.pop()
            elif string == "{":
                arquivo.write(":" + "\n")
                indentation = indentation + " "
            elif string == "(":
                arquivo.write("(")
            elif string == ")":
                arquivo.write(")")
            elif string == ";":
                arquivo.write("\n")
            elif string == "!":
                arquivo.write("not")
            elif string == "true":
                arquivo.write("True")
            elif string == "false":
                arquivo.write("False")
            else:
                arquivo.write(indentation + string + " ")

    def check():
        if string == "print":
            aux.append(string)
        elif string == "fun":
            aux.append(string)
        elif string == "var":
            aux.append(string)
        elif string == "while":
            aux.append(string)
        elif string == "if":
            aux.append(string)

    check()

    if aux:
        decision()
    else:
        aux.append(string)
        decision()


def ler_programa():
    print(open("./testes/programa.py", "r").read())
    print("----------------- Executando o Código -----------------")
    exec(open("./testes/programa.py", 'r').read())


def apagar_txt(op):
    with open(op, 'w') as arquivo:
        arquivo.truncate()
