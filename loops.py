#!/Users/danny.molnar/.pyenv/shims/python

# demonstrating basics of loops

my_list = []
planets = ["mercury", "venus", "earth"]

i = 1
while i<5:
    my_list.append(i)
    i += 1

for i in my_list:
    print(i)

for count, value in enumerate(planets):
    print((count+1), value)


distance = {
    "mercury" : 1,
    "venus" : 2,
    "earth" : 3
}
    
print(distance['earth'])

def sum(a:int, b:int) -> int:
    return a+b

print(sum(2,3))