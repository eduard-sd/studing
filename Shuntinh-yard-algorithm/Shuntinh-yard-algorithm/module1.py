string = "((9/(5-(1+1)))*3)-(2+(1+1))" #input("input string:")

priority_dic = {
    "^" : {
        "precedence" : 4,
        "associativity" : "Right"
        },
    "*" : {
        "precedence" : 3,
        "associativity" : "Left"
        },
    "/" : {
        "precedence" : 3,
        "associativity" : "Left"
        },
    "+" : {
        "precedence" : 2,
        "associativity" : "Left"
        },
    "-" : {
        "precedence" : 2,
        "associativity" : "Left"
        }
    }
#(1+1)
number_list = []
operator_stack = []
for token in string:
    if token.isdigit() == True:
        number_list.append(token)
    elif token == "(":
        operator_stack.append(token)
    elif token == ")": # пока токен равен правая скобка удаляем из массива
        while operator_stack[-1] != "(": #пока токен не равен левая скобка перемещаем элемент в другой массив
            number_list.append(operator_stack.pop())
        operator_stack.pop()
    else:
        if len(operator_stack) != 0 and operator_stack[-1] != "(":
            print(operator_stack)
            token_priority = priority_dic[token]["precedence"]
            operator_stack_last_sym = priority_dic[operator_stack[-1]]["precedence"]
            while operator_stack_last_sym >= token_priority or priority_dic[token]["associativity"] == Left:
                number_list.append(operator_stack.pop())
        operator_stack.append(token)


for token in operator_stack:
    number_list.append(operator_stack.pop())

print(operator_stack, number_list)



def method (x,y,z):
    if z == "+":
        return int(x) + int(y)
    elif z == "^":
        return int(x)**int(y)
    elif z == "-":
        return int(x)-int(y)
    elif z == "/":
        return int(int(x)/int(y))
    elif z == "*":
        return int(x)*int(y)
    else:
        return 0


number_list2 = []
def last_func (start_list):
    for i,n in enumerate(start_list):
       if not n.isdigit():
            number_list2 = method(start_list[i-2],start_list[i-1],n)
            start_list[i-1] = str(number_list2)
            del start_list[i]
            del start_list[i-2]
            print(start_list)
            return last_func(start_list)
       elif n.isdigit() and len(start_list)==1:
           return int(n)


print(last_func(number_list))



