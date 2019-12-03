
def edit_distance(palavra1, palavra2):
    sizePalavra1=len(palavra1)+1
    sizePalavra2=len(palavra2)+1

    tbl = {}
    for i in range(sizePalavra1): tbl[i,0]=i
    for j in range(sizePalavra2): tbl[0,j]=j
    for i in range(1, sizePalavra1):
        for j in range(1, sizePalavra2):
            cost = 0 if palavra1[i-1] == palavra2[j-1] else 1
            tbl[i,j] = min(tbl[i, j-1]+1, tbl[i-1, j]+1, tbl[i-1, j-1]+cost)

    return tbl[i,j]

print(edit_distance("Guilherme Barbosa Ochikubo", "Guilerme barbosa Ochibuko"))