def solution(S):
    N = len(S)
    patches = 0
    i = 0

    if S[i] == "X":
        patches +=1
        i +=3
    else:
        i +=1

    return patches