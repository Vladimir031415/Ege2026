from re import*
data = input()
pat = r"([1-9][0-9]*=)+[1,9][0-9]*"
matches = [match.group() for match in finditer(pat, data)]
ans = 0
for line in matches:
    ii = line.split('=')
    for i in range(len(ii)-1):
        if ii[i] == ii[i+1]:
            ans = max(ans, len(line))
            break


print(ans)