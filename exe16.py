filename = "test.txt"

print(f"We are going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C)!")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, "w")
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask for three lines.")

l1 = input("Line 1: ")
l2 = input("Line 2: ")
l3 = input("Line 3: ")

print("I'm going to write this to the file.")
target.write(f"{l1}\n{l2}\n{l3}")

print("Finally, we'll close the file.")
target.close()

