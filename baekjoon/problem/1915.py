#[가장 큰 정사각형]- Gold 5

n,m=map(int,input().split())
rect=[]

for i in range(n):
    width=input()
    rect.append(list(map(int,list(width))))

dp=[[0 for _ in range(m+1)] for _ in range(n+1)]

mlen=0
for i in range(1,n+1):
    for j in range(1,m+1):
        if rect[i-1][j-1]==1:
            dp[i][j]=min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])+1
            
            if dp[i][j]>mlen:
                mlen=dp[i][j]

print(mlen**2)