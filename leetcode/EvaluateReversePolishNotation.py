import copy


if __name__ == "__main__":
    #tokens = ["2", "1", "+", "3", "*"]
    #tokens = ["4", "13", "5", "/", "+"]
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    stack = []
    res = 0
    a = 0
    b = 0
    for t in tokens:
        if t not in ['+', '-', '*', '/']:
            stack.append(int(t))
        else:
            if t == '+':
                stack.append(stack.pop() + stack.pop())
            if t == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            if t == '*':
                stack.append(stack.pop() * stack.pop())
            if t == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(b / a)
    print stack.pop()
  
	
