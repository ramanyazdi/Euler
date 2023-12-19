            
def prime_factors(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            # print('n=',n)
            # print('divisor',divisor)
            factors.append(divisor)
            # print(factors)
            n /= divisor
            # print('new n=',n)
        divisor += 1
        # print('new divisor', divisor )

    return factors

number = 600851475143 
result = prime_factors(number)

print(f"The prime factors of {number} are: {result}")

