for i in range(2):   #i:01
    for a in range(5):
        if i == 1 and a > 3:
            break
        print("a={}".format(a))

    for b in range(5):
        if i == 1 and b > 3:
            break
        print("b={}".format(b))

    for c in range(5):
        if i == 1 and c > 3:
            break
        print("c={}".format(c))
    print(i)
