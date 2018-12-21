import os
thieves=['a','b','c','d']
for i in range(len(thieves)):
    thief=thieves[i]
    if ((thief!='a')+(thief=='d')+(thief=='b')+(thief!='d')==1):
        print('偷走钻石的是',thieves[i])
os.system('pause')
