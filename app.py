# ================================ Python Operators By M.Sameer Awan ============================== 


# 1. Arithmetic Operators: +, -, *, /, %, //, ** Used for Mathematical Operations

a = 10
b = 3

print(a + b)  # Addition: 13
print(a - b)  # Subtraction: 7
print(a * b)  # Multiplication: 30
print(a / b)  # Division: 3.3333
print(a // b) # Floor Division: 3
print(a % b)  # Modulus (remainder): 1
print(a ** b) # Exponentiation: 10^3 = 1000


# 2. Assignment Operators: (Used to assign Values)

x = 5    # Assign value
x += 3   # x = x + 3 → 8
x -= 2   # x = x - 2 → 6
x *= 4   # x = x * 4 → 24
x /= 6   # x = x / 6 → 4.0
x //= 2  # x = x // 2 → 2.0
x %= 3   # x = x % 3 → 2.0
x **= 2  # x = x ** 2 → 4.0
print(x)


# 3. Comaparison Operators: (Used to Compare Values)

a = 5
b = 8

print(a == b)  # False (checks equality)
print(a != b)  # True (checks inequality)
print(a > b)   # False
print(a < b)   # True
print(a >= b)  # False
print(a <= b)  # True


# 4. Logical Operators: (Used for Boolean logic)

x = True
y = False

print(x and y)  # False (both must be True)
print(x or y)   # True (at least one True)
print(not x)    # False (negates True to False)


# 5. Identity Operators: {These are used to compare object identity (whether they refer to the same memory location).}

a = [1, 2, 3]
b = a            # Both point to the same list
c = [1, 2, 3]    # A separate list with the same values

print(a is b)      # True (same object)
print(a is c)      # False (different objects)
print(a is not c)  # True


# 6. Membership Operators: (used to check if a value exists in a sequence.)

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)     # True
print("grape" not in fruits)  # True


# 7. Bitwise Operators {These work on bits (binary representation of numbers).}

x = 5  # 0101 in binary
y = 3  # 0011 in binary

print(x & y)   # 1 (0001) - AND
print(x | y)   # 7 (0111) - OR
print(x ^ y)   # 6 (0110) - XOR
print(~x)      # -6 (bitwise NOT)
print(x << 1)  # 10 (Left Shift, 1010 in binary)
print(x >> 1)  # 2 (Right Shift, 0010 in binary)


# ======================== Python Operators By M.Sameer Awan =============================