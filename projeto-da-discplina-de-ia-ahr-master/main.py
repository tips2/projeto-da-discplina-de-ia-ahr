from backward.backward import Backward


def load_knowledge_base(path, ctx):

    with open(path, "r") as txt_file:
        for line in txt_file:
            ctx.evaluate(line.replace("\n", ""))


def parse_question(variable_name):

    variable_name = variable_name.split("_")

    if len(variable_name) == 4:
        return f"O valor de {variable_name[0]} é {variable_name[1].lower()} ou {variable_name[2].lower()} a {variable_name[3]} ?"
    
    return f"O valor de {variable_name[0]} é {variable_name[1].lower()} a {variable_name[2]} ?"


if __name__ == "__main__":
    
    ctx = Backward()

    # Defining our knowledge base
    # Base de matemática
    load_knowledge_base("data/mat-bin.txt", ctx)
    
    # Base de português
    # load_knowledge_base("data/port-bin.txt", ctx)

    # Let's bind some questions to ask the user whenever the value of the variable is unknown.

    ctx.bind_question("G2_MENOR_IGUAL_8", parse_question("G2_MENOR_IGUAL_8"))
    ctx.bind_question("G2_MENOR_IGUAL_9", parse_question("G2_MENOR_IGUAL_9"))
    ctx.bind_question("GOOUT_MENOR_IGUAL_2", parse_question("GOOUT_MENOR_IGUAL_2"))
    ctx.bind_question("FEDU_MENOR_IGUAL_2", parse_question("FEDU_MENOR_IGUAL_2"))
    ctx.bind_question("SUTUDYTIME_MENOR_IGUAL_3", parse_question("SUTUDYTIME_MENOR_IGUAL_3"))
    ctx.bind_question("STUDYTIME_MENOR_IGUAL_1", parse_question("STUDYTIME_MENOR_IGUAL_1"))
    ctx.bind_question("G1_MENOR_IGUAL_8", parse_question("G1_MENOR_IGUAL_8"))
    ctx.bind_question("G1_MENOR_IGUAL_9", parse_question("G1_MENOR_IGUAL_9"))
    ctx.bind_question("G1_MENOR_IGUAL_10", parse_question("G1_MENOR_IGUAL_10"))
    ctx.bind_question("FAMSUP_IGUAL_0", parse_question("FAMSUP_IGUAL_0"))
    ctx.bind_question("AGE_MENOR_IGUAL_17", parse_question("AGE_MENOR_IGUAL_17"))
    ctx.bind_question("G1_MENOR_IGUAL_8", parse_question("G1_MENOR_IGUAL_8"))
    ctx.bind_question("FAILURES_MENOR_IGUAL_2", parse_question("FAILURES_MENOR_IGUAL_2"))
    ctx.bind_question("FAILURES_MENOR_IGUAL_2", parse_question("FAILURES_MENOR_IGUAL_2"))
    ctx.bind_question("FEDU_MENOR_IGUAL_1", parse_question("FEDU_MENOR_IGUAL_1"))
    ctx.bind_question("FEDU_MENOR_IGUAL_3", parse_question("FEDU_MENOR_IGUAL_3"))
    ctx.bind_question("FREETIME_MENOR_IGUAL_2", parse_question("FREETIME_MENOR_IGUAL_2"))
    ctx.bind_question("GOOUT_MENOR_IGUAL_4", parse_question("GOOUT_MENOR_IGUAL_4"))
    ctx.bind_question("GOOUT_MENOR_IGUAL_1", parse_question("GOOUT_MENOR_IGUAL_1"))
    ctx.bind_question("SCHOOLSUP_IGUAL_0", parse_question("SCHOOLSUP_IGUAL_0"))
    ctx.bind_question("WALC_MENOR_IGUAL_4", parse_question("WALC_MENOR_IGUAL_4"))

    # Initial facts

    # ctx.evaluate("= ")

    # Ask a question

    # Will th student PASS ?

    print(">> O estudante irá passar ?")

    answer = ctx.evaluate("PASS")

    answer = "Sim, é provável que o estudante tenha um bom aproveitamento." if answer[0] else "Não, é provável que o estudante reprove no curso."

    print(answer)
