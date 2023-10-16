if __name__ == '__main__':
    l = list()
    l2=list()
    l3=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        l_orginal = list()
        l_handle=list()
        l_orginal.append(name) , l_orginal.append(score)
        l_handle.append(score), l_handle.append(name)
        l.append(l_orginal), l2.append(l_handle)
        l3.append(score)
    min_score=min(l3)
    l2.sort()
    l3.sort()
    min_ind=l3.index(min_score)
    min_count=l3.count(min_score)
    second=l2[min_ind+min_count][0]
    namelists=[l2[i][1] for i in range(len(l2)) if l2[i][0]==second]
    for i in namelists:
        print(i)
