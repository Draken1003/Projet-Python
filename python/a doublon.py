def a_doublon(liste):
    n = len(liste)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if liste[i] == liste[j]:
                return True
    return False