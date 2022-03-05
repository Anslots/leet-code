def is_valid(op, cl):
    print(f'checking if {op} is valid opener for {cl}')
    res = False
    if op == '[':
        res = True if cl == ']' else False

    if op == "{":
        res = True if cl == "}" else False
    
    if op == "(":
        res = True if cl == ")" else False
    print(f'decided {res}')


is_valid('[', ']')
print()
is_valid('{', '}')
print()
is_valid('(', ')')
print()
is_valid('(', '(')
