from datetime import datetime

lambda_age = lambda x : datetime.now().year - int(x)

def calculate_age():
    return datetime.now().year - int(date)

date = input("Birth year?: ")
print(calculate_age())
print(lambda_age(date))

# added some comments to the bottom


