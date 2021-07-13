#전위순회방식
def DFS(v):
    if v > 7:
        return
    else:
        print(v, end=" ")
        #왼쪽 자식 노드
        DFS(v*2)
        #오른쪽 자식 노드
        DFS(v*2+1)

#중위순회방식
def DFS2(v):
    if v > 7:
        return
    else:
        #왼쪽 자식 노드
        DFS2(v*2)
        print(v, end=" ")
        #오른쪽 자식 노드
        DFS2(v*2+1)

#후위순회방식
def DFS3(v):
    if v > 7:
        return
    else:
        #왼쪽 자식 노드
        DFS3(v*2)
        #오른쪽 자식 노드
        DFS3(v*2+1)
        print(v, end=" ")

DFS(1)
print()
DFS2(1)
print()
DFS3(1)