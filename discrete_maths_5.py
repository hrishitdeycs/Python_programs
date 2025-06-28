def solve_polynomial(): 
    func = list(map(int, input("Enter Your Function coefficient Seperated With Space::").split()))
    num = int(input("Enter Value Of Your Variable::"))
    value = 0
    power = len(func) - 1
    for coeff in func:
        value += coeff * (num ** power)
        power -= 1
    return value
print(solve_polynomial())
