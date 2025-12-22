alf = "0123456789ABCDEFGHIJKL"
for i in alf:
    if (int(f"A23{i}AC0", 22) + int(f"GB{i}21670", 22)) % 21 == 0:
        print((int(f"A23{i}AC0", 22) + int(f"GB{i}21670", 22)) // 21)
