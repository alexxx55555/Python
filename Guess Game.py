print("Guess the number " + "you have 3 attempts")

secret_number = 7

guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
  guess = int(input('Enter a number: '))
  guess_count +=1
  if guess == secret_number:
      print("You won!")
      break
  else:
      print('Sorry, incorrect number. Try again.')
else:
    print('Sorry, you lost! ')