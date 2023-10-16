for _ in range(int(input())):
    a1, a2 = input().split()
    try:
        print(int(a1) // int(a2))
    except Exception as e:
        print("Error Code:", e)
