import math
score = 0
score += 5
print(score)
lives = 3
lives -= 1
print(lives)

print(round(3.7))
print(round(3.14159, 2))
print(abs(-8))
print(max(4, 9, 2))
print(min(4, 9, 2))


print(math.sqrt(16))
print(math.pi)
print(math.floor(4.8))
print(math.ceil(4.2))

print(0.1 + 0.2 == 0.3)
print(round(0.1 + 0.2, 2) == 0.3)
print(math.isclose(0.1 + 0.2, 0.3))

from decimal import Decimal

float_total = 0
exact_total = Decimal("0")
for _ in range(10):
    float_total += 0.1
    exact_total += Decimal("0.1")
print(float_total)
print(exact_total)
print(Decimal("19.99") * 3)

x = 10
x -= 4
print(x)

x = 3
x *= 2
x += 1
print(x)

steps = 1000
steps += 250
steps += 250
print(steps)

price = 49.987
rounded = round(price, 2)
print(round(price, 2))

a = -7
b = 3
print(abs(-7 - 3))
