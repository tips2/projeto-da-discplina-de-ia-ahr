from typing import Mapping
from backward import Backward


"""
    Given the kowledge base:
        
        If X croaks and X eats flies – Then X is a frog
        If X chirps and X sings – Then X is a canary
        If X is a frog – Then X is green
        If X is a canary – Then X is yellow

    And initial facts:

        Fritz croaks
        Fritz eats flies

    Our goal is to decide wether Fritz is green.
"""


if __name__ == "__main__":
    
    ctx = Backward()

    # Defining our knowledge base
    ctx.evaluate("ABSENCES_MENOR_IGUAL_9 & G1_MENOR_IGUAL_7 | G2_MENOR_IGUAL_7 | G1_MENOR_IGUAL_10 & !ABSENCES_MENOR_IGUAL_10 | FAILURES_IGUAL_0 | ABSENCES_MENOR_IGUAL_15 | ABSENCES_MENOR_IGUAL_1 | !ABSENCES_MENOR_IGUAL_8 => FAIL")
    ctx.evaluate("!ABSENCES_MENOR_IGUAL_9 & G1_MENOR_IGUAL_7| !FAILURES_IGUAL_0| AGE_MENOR_IGUAL_17 & ABSENCES_MENOR_IGUAL_13 | !G1_MENOR_IGUAL_10 & !G2_MENOR_IGUAL_9 | !ABSENCES_MENOR_IGUAL_15 | !ABSENCES_MENOR_IGUAL_1 & ABSENCES_MENOR_IGUAL_8 => PASS")
    ctx.evaluate("G1_MENOR_IGUAL_7 & ABSENCES_MENOR_IGUAL_10 => ABSENCES_MENOR_IGUAL_9")
    ctx.evaluate("G2_MENOR_IGUAL_9 & !G2_MENOR_IGUAL_7 => ABSENCES_MENOR_IGUAL_10")
    ctx.evaluate("!ABSENCES_MENOR_IGUAL_10 => G1_MENOR_IGUAL_10")
    ctx.evaluate("!G1_MENOR_IGUAL_10 => FAILURES_IGUAL_0")
    ctx.evaluate("!G2_MENOR_IGUAL_9 => G1_MENOR_IGUAL_10")
    ctx.evaluate("G1_MENOR_IGUAL_10 => AGE_MENOR_IGUAL_17")
    ctx.evaluate("AGE_MENOR_IGUAL_17 &  ABSENCES_MENOR_IGUAL_13 => ABSENCES_MENOR_IGUAL_5")
    ctx.evaluate("ABSENCES_MENOR_IGUAL_13 => ABSENCES_MENOR_IGUAL_15")
    ctx.evaluate("!AGE_MENOR_IGUAL_17 => ABSENCES_MENOR_IGUAL_1")
    
    # Initial facts

    # ctx.evaluate("= croaks eatsFlies")

    # Let's bind some questions to ask the user whenever the value of the variable is unknown.

    """ctx.bind_question("croaks", "Does it croak?")
    ctx.bind_question("eatsFlies", "Does it eat flies?")
    ctx.bind_question("chirps", "Does it chirp?")
    ctx.bind_question("sings", "Does it sing?")
    """
    ctx.bind_question("ABSENCES_MENOR_IGUAL_9", "ABSENCES_MENOR_IGUAL_9?")
    ctx.bind_question("G1_MENOR_IGUAL_7","G1_MENOR_IGUAL_7?")
    ctx.bind_question("ABSENCES_MENOR_IGUAL_10","ABSENCES_MENOR_IGUAL_10?")
    ctx.bind_question("G1_MENOR_IGUAL_10","G1_MENOR_IGUAL_10?")
    ctx.bind_question("FAILURES_IGUAL_0","FAILURES_IGUAL_0?")
    ctx.bind_question("G2_MENOR_IGUAL_7","G2_MENOR_IGUAL_7?")
    ctx.bind_question("G2_MENOR_IGUAL_9","G2_MENOR_IGUAL_9?")
    ctx.bind_question("AGE_MENOR_IGUAL_17","AGE_MENOR_IGUAL_17?")
    ctx.bind_question("ABSENCES_MENOR_IGUAL_13","ABSENCES_MENOR_IGUAL_13?")
    ctx.bind_question("ABSENCES_MENOR_IGUAL_15","ABSENCES_MENOR_IGUAL_15?")
    ctx.bind_question("ABSENCES_MENOR_IGUAL_1","ABSENCES_MENOR_IGUAL_1?")
    ctx.bind_question("ABSENCES_MENOR_IGUAL_8","ABSENCES_MENOR_IGUAL_8?")


    # Ask a question:

    # Is fritz green ?

    answer = ctx.evaluate("PASS")

    answer = "Yes, pass." if answer[0] else "No, don't pass."

    print(answer)

    # Is fritz yellow ?

    answer = ctx.evaluate("FAIL")

    answer = "Yes, fail." if answer[0] else "No, don't fail."

    print(answer)