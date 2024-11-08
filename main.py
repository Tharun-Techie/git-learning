a = 10
b = 20

a,b = b,a

print(a)
print(b)


# also we can do this

def swap(a,b):
    return b,a

# orrrr

temp = a
a = b
b = temp