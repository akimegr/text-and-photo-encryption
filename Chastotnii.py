import matplotlib
import matplotlib.pyplot as plt
import numpy as np

a = {chr(c):0 for c in range(ord("A"), ord("Z")+1)}
print(a)
file = open("Dangerous Liaisons.txt", "rb")   #взял ради интереса другую книгу
for i in file:
    m = i.decode("utf-8").upper()
    for z in m:
        if z in a:
            a[z]+=1
print(a)
xpoint = np.array([val for val, i in a.items()])
ypoint = np.array([i for val, i in a.items()])
print(xpoint)
plt.bar(xpoint,ypoint, color = "hotpink")
plt.show()
sum = 0
for i,v in a.items():
    sum+=v
for val, k in a.items():
    print(sum)
    print(k)
    print(f"{val} - {k/sum*100} %")

