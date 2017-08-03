class Question:
    
    def __init__(self, question, a, b, correct):
        self.questionText = question
        self.answerA = a
        self.answerB = b
        self.correct = correct
        
    def ask(self):
        print(self.questionText)
        print("A)", self.answerA)
        print("B)", self.answerB)

testQuestion = Question("Blah blah blah?", "Yep", "Nope", 'A')
testQuestion.ask()
answer = input("Type A or B: ")
if answer == testQuestion.correct:
    print("Yay")
else:
    print("Boo")
