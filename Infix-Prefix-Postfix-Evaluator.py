import operator 

# this dictionary 'operations' is used to 'covert' stringed operators to actual operators.
operations = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '^' : operator.pow
}

# stack implementation
class Stack:
    def __init__(self):
        self.items = []
  
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if (self.size() == 0):
            raise "Nothing to remove since stack is empty!"
        else:
            return self.items.pop()
    
    def top(self):
      return self.items[-1]

    def isEmpty(self):
      if self.size() == 0:
        return True

    def display(self):
        print(self.items)
        return

    def size(self):
        return len(self.items)

# checks if character is an operand
def isOperand(char):
  if char.isnumeric():
    return True

# checks if character is an operator
def isOperator(char):
  if char in "+-/*^":
    return True

# checks if op1 has higher precedence than op2
def hasHigherPrecedence(op1, op2):
  precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
  try: 
    prec_op1 = precedence[op1]
    prec_op2 = precedence[op2]
    
    if prec_op1 >= prec_op2:
      return True
    return False

  except KeyError:
    return False


class Postfix:
  def __init__(self, expression:list):
    self.expression = expression

  def evaluate(self):
    expression = self.expression
    stack = Stack()
    result = 0

    try:
      for i in range(len(expression)):

        if isOperand(expression[i]):
          stack.push(expression[i])
      
        elif isOperator(expression[i]):
          op1 = int(stack.top())
          stack.pop()
          op2 = int(stack.top())
          stack.pop()
          res = operations[expression[i]](op2, op1)
          stack.push(res)
        
      while not stack.isEmpty():
        result += stack.top()
        stack.pop()
      
      return result
    
    except:
      return 'Error! The expression you entered is not acceptable. Please try again.'


class Prefix:
  def __init__(self, expression: list):
    self.expression = expression

  def evaluate(self):
    expression = self.expression[::-1] # reverse the list
    stack = Stack()
    result = 0

    try:
      for i in range(len(expression)):

        if isOperand(expression[i]):
          stack.push(expression[i])
      
        elif isOperator(expression[i]):
          op1 = int(stack.top())
          stack.pop()
          op2 = int(stack.top())
          stack.pop()
          res = operations[expression[i]](op1, op2)
          stack.push(res)
        
      while not stack.isEmpty():
        result += stack.top()
        stack.pop()
      
      return result
    
    except:
      return 'Error! The expression you entered is not acceptable. Please try again.'

  
class Infix:
  def __init__(self, expression: list):
    self.expression = expression

  def convertToPostfix(self):
    expression = self.expression
    stack = Stack()
    result = []

    try:
      for i in range(len(expression)):
        if isOperand(expression[i]):
          result.append(expression[i])

        elif isOperator(expression[i]):
          while not stack.isEmpty() and hasHigherPrecedence(stack.top(), expression[i]) and stack.top() != '(':
            result.append(stack.top())
            stack.pop()

          stack.push(expression[i])
        
        elif expression[i] == '(':
          stack.push(expression[i]) 

        elif expression[i] == ')':
          while not stack.isEmpty() and stack.top() != '(':
            result += stack.top()
            stack.pop()
          stack.pop() # pops the opening parenthesis

      while not stack.isEmpty():
        result += stack.top()
        stack.pop()
      
      return result

    except:
      return 'Error! The expression you entered is not acceptable. Please try again.'

  def evaluate(self):
    expression = self.convertToPostfix()
    stack = Stack()
    result = 0

    try:
      for i in range(len(expression)):

        if isOperand(expression[i]):
          stack.push(expression[i])
      
        elif isOperator(expression[i]):
          op1 = int(stack.top())
          stack.pop()
          op2 = int(stack.top())
          stack.pop()
          res = operations[expression[i]](op2, op1)
          stack.push(res)
        
      while not stack.isEmpty():
        result += stack.top()
        stack.pop()
      
      return result
    
    except:
      return 'Error! The expression you entered is not acceptable. Please try again.'

 
def main():
    print("Select input expression: \n (1) Infix\n (2) Prefix\n (3) Postfix\n")
    type_expression = input("Type the number of chosen expression: ")

    if type_expression == "1":
        input_expression = input(f"Enter your infix expression: ")
        input_expression_list = input_expression.split() # turns expression string input into a list 
        _expression = Infix(input_expression_list)
        print()
        print("Your Infix Expression:", input_expression)
        print("Answer:", _expression.evaluate())
        print() 

    elif type_expression == "2":
        input_expression = input(f"Enter your prefix expression: ")
        input_expression_list = input_expression.split() # turns expression string input into a list 
        _expression = Prefix(input_expression_list)
        print()
        print("Your Prefix Expression:", input_expression)
        print("Answer:", _expression.evaluate())
        print() 

    elif type_expression == "3":
        input_expression = input(f"Enter your postfix expression: ")
        input_expression_list = input_expression.split() # turns expression string input into a list 
        _expression = Postfix(input_expression_list)
        print()
        print("Your Postfix Expression:", input_expression) 
        print("Answer:", _expression.evaluate())
        print()
    
    else:
        return "Invalid type of expression! Please try again! :("  


if __name__ == '__main__':
  main()
      
