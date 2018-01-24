#1 написать формулу пи 
#2 создать обьект хранения числа пи 
#3 указать количество знаком после запятой

x,y,z = 0,1,2

t = 4
base = 3
count = 1
number_after_point = input("input_count_after:")

while count < int(number_after_point):
    count += 1
    x +=2
    y +=2
    z +=2
    if count % 2 == 0:
        base += t/(x*y*z)
    elif count % 2 != 0:
        base -= t/(x*y*z)
        
print("пи1",base)


pi = (3+4/(2*3*4)-4/(4*5*6))
print ("пи1",pi)