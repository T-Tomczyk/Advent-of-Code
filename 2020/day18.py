with open('day18input2.txt') as f:
    data = [l[:-1] for l in f.readlines()]

# Part 1
# def solve_no_parents(expr):
#     expr = expr.split()
#
#     for index in range(2, len(expr), 2):
#         if expr[index-1] == '+':
#             expr[index] = int(expr[index-2]) + int(expr[index])
#         else:
#             expr[index] = int(expr[index-2]) * int(expr[index])
#
#     return str(expr[len(expr)-1])

# Part 2
def solve_no_parents(expr):
    expr = expr.split()

    for index in range(len(expr)-2, 0, -1):
        if expr[index] == '+':
            expr[index-1] = int(expr[index-1]) + int(expr[index+1])
            del(expr[index+1])
            del(expr[index])

    for index in range(len(expr)-2, 0, -1):
        if expr[index] == '*':
            expr[index-1] = int(expr[index-1]) * int(expr[index+1])
            del(expr[index+1])
            del(expr[index])

    return str(expr[len(expr)-1])

def solve(expr):
    if '(' not in expr:
        return solve_no_parents(expr)
    else:
        closing_parent_idx = expr.index(')')

        i = closing_parent_idx - 1
        while True:
            if expr[i] == '(':
                opening_parent_idx = i
                break
            else:
                i -= 1

        sub_expr = expr[opening_parent_idx+1:closing_parent_idx]
        return solve(
            expr[:opening_parent_idx] +
            solve_no_parents(sub_expr) +
            expr[closing_parent_idx+1:]
            )

total = 0
for expr in data:
    total += int(solve(expr))
print(total)
