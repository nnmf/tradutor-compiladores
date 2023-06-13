

def iniciar_tradutor(string):
    # string = tabular_conteudo(string)
    string = remover_limitadores_e_outros(string)
    string = adicionar_parenteses_print(string)
    string = manipular_declaracao(string)
    print(string)
    print("----------------- Executando o Código -----------------")
    exec(string)


def tabular_conteudo(string):
    linhas = string.split('\n')  # Divide o texto em linhas
    resultado = []  # Lista para armazenar as linhas tabuladas

    nivel_tabulacao = 0  # Contador de nível de tabulação

    for linha in linhas:
        linha = linha.strip()  # Remove espaços em branco no início e no final da linha

        if linha.startswith('}') and nivel_tabulacao > 0:
            nivel_tabulacao -= 1  # Diminui o nível de tabulação

        resultado.append('\t' * nivel_tabulacao + linha)  # Adiciona a linha atual com tabulação

        if linha.endswith('{'):
            nivel_tabulacao += 1  # Aumenta o nível de tabulação

    resultado_final = '\n'.join(resultado)  # Une as linhas tabuladas em uma única string
    return resultado_final


def manipular_declaracao(string):
    nova_string = string.replace("var ", "")
    # nova_string = nova_string.replace("fun ", "")
    return nova_string


def remover_limitadores_e_outros(string):
    nova_string = ""
    i = 0
    dentro_aspas = False

    while i < len(string):
        if string[i] == '"':
            dentro_aspas = not dentro_aspas
        if dentro_aspas:
            nova_string += string[i]
        else:
            if string[i:i + 2] == '} ':
                i += 2
                continue
            if string[i] == ';' or string[i] == '{' or string[i] == '}':
                i += 1
                continue
            if string[i] == '!':
                nova_string += "not "
                i += 1
                continue
            if string[i:i + 4] == 'true':
                nova_string += 'True'
                i += 4
                continue
            if string[i:i + 5] == 'false':
                nova_string += 'False'
                i += 4
                continue
            nova_string += string[i]
        i += 1

    return nova_string


def adicionar_parenteses_print(string):
    linhas = string.split('\n')  # Divide o texto em linhas
    resultado = []  # Lista para armazenar as linhas modificadas

    for linha in linhas:
        if "print " in linha:
            linha_modificada = linha.replace("print",
                                             "print(") + ")"  # Adiciona parênteses após "print" e no final da linha
            resultado.append(linha_modificada)
        elif "while " in linha:
            linha_modificada = linha.replace("while",
                                             "while") + ":"
            resultado.append(linha_modificada)
        elif "fun " in linha:
            linha_modificada = linha.replace("fun",
                                             "def") + ":"
            resultado.append(linha_modificada)
        elif "if " and "if(" in linha:
            linha_modificada = linha.replace("if",
                                             "if ") + ":"
            resultado.append(linha_modificada)
        elif "else " in linha:
            linha_modificada = linha.replace("else",
                                             "else") + ":"
            resultado.append(linha_modificada)
        # elif "if " in linha:
        else:
            resultado.append(linha)

    resultado_final = '\n'.join(resultado)  # Une as linhas modificadas em uma única string
    return resultado_final

