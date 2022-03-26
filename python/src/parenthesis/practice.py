from collections import defaultdict
complements = defaultdict(lambda: '', {
    '[': ']',
    '{': '}',
    '(': ')',
    })
def is_valid(op, cl):
    print(f'checking if {op} is valid opener for {cl}')
    res = False
    # start ans code ####################
    res = True if complements[op] == cl else False

    # end ans code ####################
    print(f'decided {res}')


is_valid('[', ']')
print()
is_valid('{', '}')
print()
is_valid('(', ')')
print()
is_valid('(', '(')
