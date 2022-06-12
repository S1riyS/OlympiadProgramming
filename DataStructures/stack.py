# Стэк для проверки правильности расставления скобок

from collections import deque

def check_brackets(brackets):
    stack = deque()
    open_brackets_stack = deque()
    brackets_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    for index, bracket in enumerate(brackets):
        if bracket in brackets_dict.values():
            stack.append(bracket)
            open_brackets_stack.append(index + 1)


        elif bracket in brackets_dict.keys():
            if not (bool(stack)):
                return index + 1
            else:
                if stack[-1] == brackets_dict[bracket]:
                    stack.pop()
                    open_brackets_stack.pop()
                else:
                    return index + 1


    return open_brackets_stack.pop() if bool(stack) else 'Success'

brackets_string = '([]){([][])}'
print(check_brackets(brackets_string))
