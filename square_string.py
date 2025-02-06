def find_square_sums(limit):
    import math
    combos={}
    for i in range(1,limit+1):
        combos[i]=[]
        for j in range(1,limit+1):
            if math.sqrt(i+j)%1==0 and not i==j:
                combos[i].append(j)
    return combos

#FIX/REDO GEN_STRING
def gen_string(d):
    final_list=[]
    i=1
    d_keys=list(d.keys())
    d_vals=list(d.values())
    while len(d[i])>1:
        i+=1
    final_list.append(i)
    final_list.append(d[i][0])
    while len(final_list)<15:
        d[d_keys.index(final_list[-1]+1)].pop(final_list[-2])
        final_list.append(d[d_keys.index(final_list[-1])+1][0])
    return final_list

print(gen_string(find_square_sums(15)))


