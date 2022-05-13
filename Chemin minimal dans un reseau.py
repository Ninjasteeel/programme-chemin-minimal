def chemopti(A,B,C,P1,P2,P3,s0):
    val=A*P1+B*P2+C*P3
    return cheminmin(val,s0)
def plusCourt(ld,ls):
    lmin=ls[0]
    for i in ls:
        if ld[i] <ld[lmin]:
             lmin=i
    return lmin
def cheminmin(adj,s0):
    n=len(adj)
    inf=float("inf") #inf egal l'infini
    dist=[inf for i in range(n)]
    pere=[-1 for i in range(n)]
    dist[s0]=0
    nonmarques=[k for k in range(n)]
    marques=[]
    while len(marques)<n:
        i=plusCourt(dist,nonmarques)
        marques.append(i)
        nonmarques.remove(i)
        for k in nonmarques:
            if dist[i]+adj[i,k]<dist[k]:
                dist[k]=dist[i]+adj[i,k]
                pere[k]=i
    return dist,pere

