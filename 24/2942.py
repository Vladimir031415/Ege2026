from re import finditer
data = input()
pattern = "(A[BC])+"

matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len))//2)
