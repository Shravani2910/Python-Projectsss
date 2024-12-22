#Quiz Game

questions=("Which is the Only Desert in India?",
          "By using which process plant prepare food?",
          "When Did India get Indepenence?",
          "A group of Stars called?",
          "Which Country is the largest producer of Bananas?"),

options=(("A.Thar","B.sahara","C.polar","D.Gobi"),
        ("A.Respiration","B.Photosynthesis","C.Rooting","D.Transpiration"),
        ("A.1943","B.1948","C.1949","D.1947"),
        ("A.Galaxy","B.Space","C.Constellation","D.Universe"),
        ("A.England","B.India","C.China","D.Brazil"))

answers=('A','B','D','C','B')
guesses=[]


def ask_question(question, options, correct_answer):
    print(question)
    for option in options:
        print(option)
    
    guess = input("Please enter the letter of your answer: ").upper()
    return guess == correct_answer

def main():
    print("Welcome to the Quiz Game!")
    score = 0

    for i in range(len(questions)):
        if ask_question(questions[i], options[i], answers[i]):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {answers[i]}\n")

    print(f"Your final score is: {score}/{len(questions)}")
    print("Thank you for playing!")

if __name__ == "__main__":
    main()