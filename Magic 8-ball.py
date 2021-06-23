import random

name = input("Enter your name:")
question = input("Ask your question:")
answer = ""

random_number = random.randint(1, 10)

if question == "":
  print("Please ask the Magic 8-Ball a question.")
else:
  if name == "":
    print("Question: " + question)
  else:
    print(name + " asks: " + question)
    
  print("Magic 8-Ball's answer: ", end= answer)
  
  if random_number == 1:
    answer = print("Yes - definitely.")
  elif random_number == 2:
    answer = print("It is decidedly so.")
  elif random_number == 3:
    answer = print("Without a doubt")
  elif random_number == 4:
    answer = print("Reply hazy, try again")
  elif random_number == 5:
    answer = print("Ask again later")
  elif random_number == 6:
    answer = print("Better not tell you now")
  elif random_number == 7:
    answer = print("My sources say no.")
  elif random_number == 8:
    answer = print("Outlook not so good.")
  elif random_number == 9:
    answer = print("Very doubtful.")
  elif random_number == 10:
    answer = print("Maybe")
  else:
    answer = print("Error")
    
  
