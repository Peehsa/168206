thieves=['A','B','C','D']
for i in range(len(thieves)):
    thief=thieves[i]
    if ((thief!='A')+(thief=='D')+(thief=='B')+(thief!='D')==1):
        print('偷走钻石的是',thieves[i])
        if (thief!='A')==1:
            print('说真话的是A')
        if (thief=='D')==1:
            print('说真话的是B')
        if (thief=='B')==1:
            print('说真话的是C')
        if (thief!='D')==1:
            print('说真话的是D')
