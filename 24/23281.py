with open(r"C:\Users\vova55555\Desktop\Ege2026\24\24_23281.txt") as file:
    data = file.readline()
data = data.split("Y")
for i in range(len(data) - 80):
    line = "Y".join(data[i:i+81])
    if line.count("2025") >= 90:
        ans = max(ans, len(line))
