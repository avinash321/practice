l = [2,5,7,3,10,1,22,99,12,14,19]
n1 = 0
n2 = 0
for i in l:
    if i > n1:
        n2 = n1
        n1 = i
print(f"Second Largest Number {n2}")