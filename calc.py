import re

print("Welcome to Our Magical Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""

    if previous == 0:
        equation = input("Enter Your Equation:\n")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        print("Goodbye, human!")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


        #print("You Typed", previous)

while run:
    performMath()