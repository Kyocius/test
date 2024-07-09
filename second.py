# 栈
def check_brackets(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                print('?', end='')
            else:
                stack.pop()
                if stack and stack[-1] != '(':
                    print('?', end='')
        else:
            print(char, end='')
    while stack:
        print('x', end='')
        stack.pop()

inputs = [
    'bge)))))))))',
    '((III))))))',
    '0000(uuu',
    '))))UUUU((()',
]
for input_str in inputs:
    print(f'输入: {input_str}')
    check_brackets(input_str)
    print()