data = input()

ans = cnt = l = r = 0

while r < len(data):
    if cnt <= 150:
        while cnt <= 150:
            r += 1
            if data[r] == 'Y': cnt += 1
    else:
        ans = max(ans, r-l)
        while cnt > 150:
            l += 1
            if data[l] == "Y": cnt -= 1