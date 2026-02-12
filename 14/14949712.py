for x in range(8):
    a = x * 16**2 + int(f"1{x}", 16) + int(f"{x}3{x}3", 8)
    for i in range(20):
        if a == 2**i:
            print(x)
            break
