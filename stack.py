question = ["1 – Which seven-a-side ball game is played in a swimming pool?",
"2 - When was the Olympics last held in London?",
        "3 - What is the world record time of the men's 100m sprint?",
        "4 - The latest Bond song was sung by whom?",
        "5 - Who won the Euro 2016 Final?",
        "6 - Who is the mascot of Pokemon?",
        "7 - How many stars are on the U.S flag?",
        "8 - If 1 = 5, 2 = 10, 3 = 15 and 4 = 20, what does 5 =?",
        "9 - In a right angled triangle one side is 3 and another side is 4, what is the length of the hypotenuse?",
        "10 - What is the 7th decimal place of pi?"]
multi1 = ["A: Marco Polo","A: 1944","A:9.58seconds","A: Charlie Puth","A: Portugal","A: Mew","A: 49","A: 25","A: 2","A: 4"]
multi2 = ["B: Polo","B: 2004","B: 9.68seconds","B: Sam Smith","B: Wales","B: Mewtwo","B: 52","B: 4","B: 5","B: 1"]
multi3 = ["C: Water Polo","C: 2008","C: 9.54seconds","C: Adele","C: France","C: Pikachu","C: 51","C: 5","C: 3.5","C: 9"]
multi4 = ["D: Polo Marco","D: 2012","D: 9.60seconds","D: Daniel Craig","D: Germany","D: Togepi","D: 50","D: 1","D: 6","D: 6"]
correctAnswer = ['C','D','A','B','A','C','D','D','B','D']
valueWon = ['£0','£100','£2500','£500','£1000','£2500','£5000','£10000','£100000','£1000000']

for i,j in enumerate(question):
	x = input(j + '\n ' +multi1[i]+ '\n ' +multi2[i]+ '\n ' +multi3[i]+ '\n ' +multi4[i]+'\n')
	if x == ("A","B","C"):
		print("I'm sorry that was incorrect,",correctAnswer[i],"was the correct answer, you won,",valueWon[i])
	else:
		y = input("Congratulations, you won" +" " +valueWon[i]+" " +"would you like to continue, yes or no?")
		if y == ("No","no"):
			break
