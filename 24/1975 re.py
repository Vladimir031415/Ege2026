from re import finditer
data = input()
pattern = "[^P]*(P[^P]+)*P?"

matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))