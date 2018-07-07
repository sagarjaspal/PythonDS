var = "102"
print(type(var), var)

var1 = chr(int(var))
print(type(var1), var1)

var2 = int(var)
print(type(var2), var2)

# looping through string
# for
for x in var:
    print(x)

# while
x = 0
while x < len(var):
    print(var[x])
    x += 1

string = "this is a string    "

print(string.upper())
print(string.capitalize())
print(string.strip())
print(string.split())
