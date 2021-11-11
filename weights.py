#! /Users/danny.molnar/.pyenv/shims/python

amount = input("please add amount of apples: \n")
unit = input("what type of unit? k - kg, l - lb \n")

# 5 apples = 1kg

div5 = lambda num: num / 5

resp = None

if unit == 'k':
    resp = div5(int(amount))
    print(f"Weight is: {resp} kg")
elif unit == 'l':
    resp = div5(int(amount)) * 2.2
    print(f"Weight is: {resp} lb")
else:
    print("Wrong weight unit hs been given! Please rerun the script!")

