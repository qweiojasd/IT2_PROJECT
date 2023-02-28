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

outfile.close()