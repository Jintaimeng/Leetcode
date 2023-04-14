while True:
    try:
        n, m, a, b = map(int, input().split(" "))
        if a > b:
            a, b = b, a
        maked_list = list(map(int, input().split(" ")))
        maked_list.sort()
        now_min = maked_list[0]
        now_max = maked_list[-1]
        if a == now_min and b == now_max:
            print("YES")
        elif (a < now_min and b == now_max and n > m) or (a == now_min and b >now_max and n > m) :
            print("YES")
        elif a < now_min and b > now_max and n-m >= 2:
            print("YES")
        else:
            print("NO")
    except:
        break