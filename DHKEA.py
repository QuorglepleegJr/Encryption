def power_mod(A, n, p):

    total = 1

    operations = ""

    while n > 0:

        if n % 2 == 1:

            operations += "1"
            n -= 1
        
        else:
            
            operations += "0"
            n //= 2

    for op in reversed(operations):

        if op == "0":

            total *= total
            total %= p
        
        else:

            total *= A
            total %= p
    
    return total

def generate_key(a, p, get_B, send_A):

    A = power_mod(2, a, p)

    print("a:", a, "p:", p)

    send_A(A)

    B = get_B()

    print("A:", A, "B:", B)

    return power_mod(B, a, p)


if __name__ == "__main__":

    a = 11098147
    b = 10591923
    p = 10002031

    a_get = lambda: power_mod(2, a, p)
    b_get = lambda: power_mod(2, b, p)

    blank = lambda A: None

    print(generate_key(a, p, b_get, blank))
    print(generate_key(b, p, a_get, blank))