import random
import pandas as pd
import matplotlib.pyplot as plt


def castSpell(n):
    damagelst = []
    for i in range(n):
        damage = 0
        damage6 = 0
        damage5 = 0
        damage4 = 0
        damage3 = 0
        damage2 = 0
        for j in range(10):
            roll = random.randint(1, 6)
            if roll == 6:
                damage6 += 1
                roll2 = random.randint(1, 6)
                if roll2 == 5 or roll2 == 6:
                    damage5 += 1
                    roll3 = random.randint(1, 6)
                    if roll3 in [6, 5, 4]:
                        damage4 += 1
                        roll4 = random.randint(1, 6)
                        if roll4 in [6, 5, 4, 3]:
                            damage3 += 1
                            roll5 = random.randint(1, 6)
                            while roll5 in [6, 5, 4, 3, 2]:
                                damage2 += 1
                                roll5 = random.randint(1, 6)
        damageByDice = [damage6, damage5, damage4, damage3, damage2]
        print(damageByDice)
        for value in damageByDice:
            damage += value
        damagelst.append(damage)
    return damagelst


datalist = castSpell(10)
print(datalist)
df = pd.DataFrame({"Damage": datalist})

Mean = float(df.mean())
Median = int(df.median())
Max = int(df.max())

print(f"Mean:{Mean}")
print(f"Median:{Median}")
print(f"Max:{Max}")

ax = df.plot.hist(bins=Max)
plt.show()
