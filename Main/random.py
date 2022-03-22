x = input("Enter input: ")
y = 0
for i in range(len(x)):
    if x[i] == 'i':
        y += 1
    else:
        i += 1
print(y)

