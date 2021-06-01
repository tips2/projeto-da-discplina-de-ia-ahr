import re
from backward.backward import Backward


def load_knowledge_base(path, ctx):
    """
    Carrega a base de conhecimento retornando todos os símbolos presentes no consequente das regras.
    ---
    Parâmetros
    path - Caminho do arquivo '.txt' para a base de conhecimento.
    ctx - Objeto da classe Backward.
    """
    symbols = []

    with open(path, "r") as txt_file:
        
        for line in txt_file:
            symbols.append(line.split(" "))
            ctx.evaluate(line.replace("\n", ""))
    
    symbols = [s.replace("FAIL", "").replace("PASS", "") for ss in symbols for s in ss]
    symbols = [re.sub(r"[&!=><\n]", "", s) for s in symbols]
    symbols = [s for s in symbols if s != ""]

    return sorted(symbols)


def parse_question(variable_name):
    """
    Dado o nome de uma variável retorna a pergunta caso o valor da variável seja indefinido.
    ---
    Parâmetros
    variable_name - Nome da variável, deve ser uma string.
    """
    variable_name = variable_name.split("_")

    if len(variable_name) == 4:
        return f"O valor de {variable_name[0]} é {variable_name[1].lower()} ou {variable_name[2].lower()} a {variable_name[3]} ?"
    
    return f"O valor de {variable_name[0]} é {variable_name[1].lower()} a {variable_name[2]} ?"


if __name__ == "__main__":

    print("=========== Sistema Especialista - Rendimento Escolar ===========")

    while True:

        print(">> Informe a disciplina que o aluno irá cursar ou está cursando.")

        # Defining our knowledge base

        ctx = Backward()
        course = input(">> [1] para Língua Portuguesa e [2] para Matemática.\n<< ")

        if course == '1':
            symbols = load_knowledge_base("data/port-bin.txt", ctx)
        elif course == '2':
            symbols = load_knowledge_base("data/mat-bin.txt", ctx)
        else:
            raise ValueError(">> Por favor responda [1] ou [2].")
            
        # Let's bind some questions to ask the user whenever the value of the variable is unknown.

        for s in symbols:
            ctx.bind_question(s, parse_question(s))

        # Ask a question

        query = input(">> Deseja saber se o estudande irá ser aprovado [a] ou reprovado [r]?\n<< ")
        
        if query == "a":
            print("<< O estudante será aprovado?")
            answer = ctx.evaluate("PASS")
            answer = "Sim, é provável que o estudante tenha um bom aproveitamento." if answer[0] else "Não, é provável que o estudante reprove no curso."
            print(">> " + answer)
        elif query == "r":
            print("<< O estudante será reprovado ?")
            answer = ctx.evaluate("FAIL")
            answer = "Sim, é provável que o estudante reprove." if answer[0] else "Não, é provável que o estudante tenha um bom aproveitamento."
            print(">> " + answer)
        else:
            raise ValueError(">> Por favor, responda [a] ou [r].")

        query = input(">> Deseja continuar ? Responda Sim [s] ou Não [n] ?")

        if query == "n":
            print(">> Sessão encerrada.")
            break