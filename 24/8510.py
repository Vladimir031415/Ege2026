a = input()
a = a.replace('N', '*').replace('O', '*').replace('P', '*')
b = map(len, a.split("**"))
print(max(b)+2)