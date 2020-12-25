#!/usr/bin/env python3

def parse_newmath(tokens):
    def shunting_yard():
        stack = []
        for t in tokens:
            if type(t) == int:
                yield t
            elif t == '+':  # high precedence
                while stack and stack[-1] == '+':
                    yield stack.pop()
                stack.append(t)
            elif t == '*':
                while stack and stack[-1] in '*+':
                    yield stack.pop()
                stack.append(t)
            elif t == '(':
                stack.append(t)
            elif t == ')':
                while stack[-1] != '(':
                    yield stack.pop()
                stack.pop()
        while stack:
            yield stack.pop()
    stack = []
    ops = {'*': lambda a, b: a*b, '+': lambda a, b: a + b}
    for t in shunting_yard():
        if type(t) == int:
            stack.append(t)
        else:
            rhs = stack.pop()
            lhs = stack.pop()
            stack.append(ops[t](lhs, rhs))
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
