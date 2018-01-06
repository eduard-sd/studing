from random import randint

y =  randint(0,100)


print('hello where its a game: \n\nthe rules are easy, try to guess a number\n\n')
  



def game():
    value2 = input('введи число:' )
    x = int(value2)
    if x == y:
        print ('молодец победила')
    elif x > y:
        print ('твое число больше')
        game()
    elif x < y :
        print('твое число меньше')
        game()
    
game()