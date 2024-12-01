from math import comb
N = 21
K = 11
M = 9

combs = comb(N,K)
cor = 0
for i in range(M,K+1):
    cor+= comb(K,i) * comb(N-K,K-i)
l = round((cor/combs)*100,4)
print(f"шанс выигрыша - {l}%")