import random
r = random.randint(1,5)
flag =  True
while flag:
    num = input('Type a number for an upper bound: ')
    
    if num.isdigit():
        print('Lets Play!')
        num = int(num)
        flag = False
    else:
        print('Invalid input! Try again!')
    
secret = random.randint(1,num)

guess = None
count = 1

while guess != secret:
    guess = input('Please type a number between 1 and ' + str(num) + ": ")
    if guess.isdigit():
        guess = int(guess)
        
        if guess == secret:
            print('You got it')
        else:
            print('Plaese try again')
            count += 1
            
print('It took you ', count, 'guesses!')   
ask = input(Do you want to play again [yes/no])