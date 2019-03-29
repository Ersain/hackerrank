def countApplesAndOranges(s, t, a, b, apples, oranges):
    print(len([i for i in apples if a+i in range(s, t+1)]))
    print(len([i for i in oranges if b+i in range(s, t+1)]))
