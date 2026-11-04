x, y, z = 1, 2, 3
print(x, y, z)

a = b = 0
print(a, b)

a = "apple"
b = "banana"
a = b
b = a
print(a, b)

a = "apple"
b = "banana"
a, b = b, a
print(a, b)

a = 1
b = 2
temp = a
a = b
b = temp
print(a, b)

width = 4
height = 6
print(width * height)

left = "L"
right = "R"
# Swap them here
left, right = right, left
