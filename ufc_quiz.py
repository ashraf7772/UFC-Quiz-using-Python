print ("Hi, this is Ashrafs Quiz on UFC ") #my welcome message

startQuiz = input("Do you want to start the quiz? ") #ask if the user wants to play

if startQuiz.lower() != "yes": #if they don't say yes, quit the program
    quit()

print("OK, lets start: ")
score = 0
#question 1
q1 = input("Who is the current light-weight champ? ")
if q1.lower() == "islam":
    print("correct")
    score += 1
else: 
    print("wrong")

#question 2
q2 = input("Who is the current heavy-weight champ? ")
if q2.lower() == "jon jones":
    print("correct")
    score += 1
else: 
    print("wrong")

#question 3
q3 = input("What year did Conor Mcgregor become light-weight champ? ")
if q3 == "2016":
    print("correct")
    score += 1
else: 
    print("wrong")

#question 4
q4 = input("Who was the first fighter to hold two belts simultaneously? ")
if q4.lower() == "conor mcgregor":
    print("correct")
    score += 1
else: 
    print("wrong")
    
print("Your score is " + str(score)) #total mark
print("You got " + str((score/4) * 100) + "%") #percentage