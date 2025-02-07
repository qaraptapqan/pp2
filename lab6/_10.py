s = input()
low, uper = 0, 0

for _ in s:
    if _.isupper():
        uper+=1
    elif _.islower():
        low+=1

print(f'lower case letter count = {low}, upper case letter count = {uper}')
