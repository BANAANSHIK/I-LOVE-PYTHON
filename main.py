import random

print('hi world',50*10,'lol','10')

hp = 100
damage = 40
intellect = 5
aggility = 5
lvl = 1
doing = (hp - random.randint(30,50))
print(doing)
if doing >= 60:
    print("cool")
else:
    print("bad")
name = input('name of your hero:')

_class = input("take a class: viking,varvar,ork:")

if _class == 'viking':
    damage = damage * 2
    aggility = aggility / 1,5
elif _class == "varvar":
    damage *= 4
    aggility *= 1,3
    intellect *= 2
elif _class == "ork":
    damage *= 1,7
    intellect /= 2,5
else:
    print('the wrongest mistake you are NOOB')
    damage = 0
    aggility = 0
    intellect = 0
    _class = "NOOB"


print(f' hp {hp}\n damage {damage}\n intellect {intellect}\n aggility {aggility}\n lvl {lvl}')