def cheese_and_crackers(cheese_count, box_of_cracker):
    print(f"you have {cheese_count} cheeses!")
    print(f"you have {box_of_cracker} boxes of crackers!")
    print("Man that's enought for a party!")
    print("Get a blanket.\n")

print("We can just give the functions numbers directly:")
cheese_and_crackers(20,30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_cracker = 20

cheese_and_crackers(amount_of_cheese, amount_of_cracker)
print("We can even do math inside too:")
cheese_and_crackers(10+20, 50+10)

print("And now we combine math and variables:")
cheese_and_crackers(amount_of_cheese + 1000, amount_of_cracker + 1000)
    