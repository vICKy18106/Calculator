def add(n1, n2):
  return n1 + n2

def multiply(n1, n2):
  return n1 * n2
 
def subtract(n1, n2):
  return n1 - n2

def divide(n1, n2):
  return n1 / n2


operations = {'+': add, '-': subtract, '/': divide, '*': multiply}

def calculator():
  num1 = int(input("Enter first number:"))
  should_continue = True
  while should_continue:
    for key in operations:
      print(key)
    os = input("Type any operator given above: ")
    num2 = int(input("Enter next number:"))
    calculation = operations[os]
    answer = calculation(num1, num2)
    print(f"{num1} {os} {num2} = {answer}")
    
    if input(f"wnat to calculate with {answer} or wnat new calc type y or n: ")=="y":
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()