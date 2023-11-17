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

    send_A(A)

    B = get_B()

    return power_mod(B, a, p)