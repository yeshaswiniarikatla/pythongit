print("*********************")
print("welcome to quiz game")

question_bank=[
    {"text":"The ability of one class to acquire methods and attributes from another class is called.","Answer":"A"},
    {"text":"Which of the following is a type of inheritance?","Answer":"D"},
    {"text":"What type of inheritance has multiple subclasses to a single superclass?","Answer":"C"},
    {"text":"What is the depth of multilevel inheritance in python?","Answer":"C"},
    {"text":"What does MRO Stand for?","Answer":"B"}
]




Options=[["A.Inheritance","B.Abstraction","C.Polymorphism","D.Objects"],
         ["A.Single","B.Double","C.Multiple","D.Both A and C"],
         ["A.Multiple Inheritance","B.Multilevel Inheritance","C.Hierarchial Inheritance","D.None of these"],
         ["A.Two Level","B.Three Levrl","C.Any Level","D.None of these"],
         ["A.Method Recursive Object","B.Method Resolution Order","C.Main Resolution Order","D.Method Resolution Object"]]
score=0


def check_answer(user_guess,correct_answer):
    if user_guess==correct_answer:
        return True
    else:
        return False


for question_num in range(len(question_bank)):
    print("***********************")
    print(question_bank[question_num]["text"])
    for i in Options[question_num]:
        print(i)


    guess=input("enter your answer(A/B/C/D): ")
    is_correct=check_answer(guess,question_bank[question_num]["Answer"])
    if is_correct:
        print("correct Answer")
        score+=1
    else:
        print("incorrect answer")
        print("The correct answer is: ",question_bank[question_num]["Answer"])
print("your final score is: ",score)
print("your percentage is:",(score/len(question_bank))*100)
    
