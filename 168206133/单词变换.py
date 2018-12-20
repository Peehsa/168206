def isOneDiff(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    if count == 1:
        return True
    else:
        return False

def findLadders(start, end, dt):
    ret = []
    def loop(wa, wb, lt, res=[]):
        for i in lt:
            if isOneDiff(wa, i)  and  isOneDiff(i, wb): 
                r = res.copy()
                r.append(wa)
                r.append(i)
                r.append(wb)
                ret.append(r)
            if isOneDiff(wa, i) and not isOneDiff(i, wb):
                r = res.copy()
                r.append(wa)
                lt_copy = lt.copy()
                try:
                    lt_copy.remove(wa)  
                except:
                    pass
                loop(i, wb, lt_copy, r)
    loop(start, end, dt)
    return ret

print(findLadders('hit', 'cog', ["hot","dot","dog","lot","log"]))
