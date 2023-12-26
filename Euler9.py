

for a in range(1, 1000):
    for b in range(a, 1000 - a):
        c = 1000 - a - b
        if a**2 + b**2 == c**2 and a < b < c:
            print("Pythagorean triplet found: a =", a, ", b =", b, ", c =", c)
            product_abc = a * b * c
            print("Product abc =", product_abc)
            break

