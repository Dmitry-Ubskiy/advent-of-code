#!/usr/bin/env python3

def parse_newmath(tokens):
    stack = []
    ops = {'*': lambda a, b: a*b, '+': lambda a, b: a + b}
    for t in tokens:
        if type(t) == int:
            if not stack or stack[-1] == '(':
                stack.append(t)
                continue
            op_sym = stack.pop()
            stack.append(ops[op_sym](stack.pop(), t))
        elif t == ')':
            assert(stack[-2] == '(')
            stack = stack[:-2] + stack[-1:]
            if len(stack) > 1 and stack[-2] in ops:
                lhs, op_sym, rhs = stack[-3:]
                stack = stack[:-3] + [ops[op_sym](lhs, rhs)]
        else:
            stack.append(t)
    assert len(stack) == 1
    return stack[-1]

def tokenize(s):
    tokens = []
    buf = None
    for c in s:
        if c in ' ()+*':
            if buf is not None:
                tokens.append(int(buf))
                buf = None
            if c != ' ':
                tokens.append(c)
        elif c in '1234567890':
            if buf is None:
                buf = ''
            buf += c
        else:
            raise AssertionError
    if buf is not None:
        tokens.append(int(buf))
    return tokens

total = 0
with open('input') as f:
    for line in f:
        total += parse_newmath(tokenize(line.strip()))
print(total)
