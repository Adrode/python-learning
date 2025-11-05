fibo_elements = [0, 1]
for i in range(10):
    fibo_elements.append(fibo_elements[-1] + fibo_elements[-2])

print(fibo_elements)