data = input()
from re import finditer

a = data.replace("NPO", "A").replace("PNO", "A")
pattern = "A+"
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))