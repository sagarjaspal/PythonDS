f = open('new.txt', 'r+')
print(f)
print(type(f))
var = "this is a sample file containing demo information\n"

#for x in range(10):
#    f.write(var)

# printing file contents line by line
# file handle (f here) is treated as sequence of strings
# for loop iterates through each string

#for line in f:
#    print(line.rstrip())

# printing file contents all at once
var1 = f.read()
print(var1)
print(var1[:70])
f.close()

with open('new.txt') as f:
    while f.readline() != '':
        print(f.readline().rstrip())
