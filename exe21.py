def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b

def divide (a, b):
    print(f"Deviding {a} / {b}")
    return a / b

print("Let's do dome math with just functions!")

age = float(input("Your age: "))
height = float(input("Your height: "))
weight = float(input("Your weight: "))
iq = float(input("Your IQ: "))

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here's a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq,2))))
print("That becomes: ", what, "Can you do it by hand?")
