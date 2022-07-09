def gridSearch(G, P):
    # Write your code here
    
    for i in range(len(G)):
        found = G[i].find(P[0])
        while G[i].find(P[0]) != -1:
            matchingCoords = []#array of tuples
            if G[i].find(P[0]) != -1:
                matchingCoords.append((i, G[i].find(P[0])))
                print(matchingCoords[0])
                for j in range(i+1, i+len(P)):
                    print("j= %d"%j)
                    print("i= %d"%i)
                    print("cord = ",matchingCoords[j-i-1][1])
                    print(G[j].find(P[j-i]))
                    if(G[j].find(P[j-i]) != -1 and G[j].find(P[j-i]) == matchingCoords[j-i-1][1]):
                        matchingCoords.append((j, G[j].find(P[j-i])))
                        print("in")
                    else:
                        break
            if(len(matchingCoords) == len(P)):
                return "YES"
            k = 0
            newGatI = ""
            for l in G[i]:
                if(k == G[i].find(P[0]) or k == G[i].find(P[0])+1):
                    newGatI += "f"
                else:
                    newGatI += l
                k += 1
            G[i] = newGatI
            print(G)
            print(G[i].find(P[0]))
                
    return "NO"