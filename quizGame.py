# This is a Quizz game with some questions and answers 

quizz = ("What is my favorite color? ", 
      " What is the brand of my first car? ", 
      "How old am I?", 
      "What is my home town?", 
      "I was born in: ")
index_options = 0
options = (("A. Green B. Red C. Blue D. Grey "), 
           ("A. Fiat B. Ford C. Volvo D. BMW"), 
           ("A. 22 B. 32 C. 31 D. 28 "), 
           ("A. Belo Horizonte B. Contagem C. Betim D. Neves"), 
           ("A.2004 B. 1994 C. 1995 D.1997 "))

for questions in quizz:
    print(questions)
    for option in options[index_options]:
        print(option)
    print("-------------------------------------------------------------------------")
