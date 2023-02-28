import matplotlib.pyplot as plt
import random
import time

def gettemp():
    mintemp = 30
    maxtemp = 42
    randomtemp = mintemp + random.random() * (maxtemp - mintemp)
    return round(randomtemp, 2)

outfile = open("data.txt","w")  # ændre "w" til "a" for at tilføje 1000 temperature til

while True:
    temp = str(gettemp())
    outfile.write(temp + '\n')
    time.sleep(2)

X, Y = [], []
for line in open('data.txt', 'r'):
  values = [float(s) for s in line.split()]
  X.append(values[0])
  Y.append(values[1])

plt.plot(X, Y)
plt.show()
window.mainloop()