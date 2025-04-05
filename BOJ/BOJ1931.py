N = int(input())
meeting = []
count = 1

for _ in range(N):
    meeting.append(list(map(int,input().split())))

# meeting.sort()
meeting.sort(key=lambda x:x[1])

# meeting.sort(key=lambda x:(x[1],x[0])

end = meeting[0][1]
for i in range(1,N):
    if end <= meeting[i][0]:
        end = meeting[i][1]
        count += 1

print(count)


'''
3
2 2
1 2
2 3
ans = 3
'''