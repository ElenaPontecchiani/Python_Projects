from Question import Question
question_prompt = [
    "What color are roses?\na) Red \nb) Blue/Green \nc) Purple \nd) Yellow\n\n",
    "What color are bananas?\na) Red \nb) Blue/Green \nc) Purple \nd) Yellow\n\n",
    "What color are strawberries?\na) Red \nb) Blue/Green \nc) Purple \nd) Yellow\n\n"
]

#quale domanda displayio nel prompt e quale risposta è corretta
question_whit_right_answer =[
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "d"),
    Question(question_prompt[2], "c")
]

#come parametro lista di oggetti question che vogliamo fare all'utente
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.question_prompt) #visualizzo la domanda, poi l'utente digita a/b/c/d
        if answer == question.answer:
            score +=1
    return score


print("Your score is: " + str(run_test(question_whit_right_answer)) + "/" + str(len(question_whit_right_answer)))

