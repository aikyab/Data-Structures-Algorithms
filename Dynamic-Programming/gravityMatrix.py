print("Hello World!")

box = [['#', '#', '.', '.', '.', '#', '.'],
       ['#', '#', '#', '.', '.', '*', '.'],
       ['#', '#', '#', '*', '.', '#', '.']]

new_box = [['0'] * len(box) for _ in range(len(box[0]))]

#flag=True
# q = [1,0]

for i in range(len(box)):
    q = deque()
    flag = False
    for j in range(len(box[0])):
        
            
        if flag:
            if box[i][j]=='*':
                q.clear()
                flag = False
            elif box[i][j]=='#':
                q.append((i,j))
            else:
                val = q.popleft()
                x,y = val[0],val[1]
                box[i][j],box[x][y] = box[x][y],box[i][j]
                q.append((i,j))
            # if i==1:
            #     print(box[i],"q=",q)
            continue
        if box[i][j] == '#':
            flag = True
            q.append((i,j))
            # if i==1:
            #     print(box[i],"q=",q)

m,n = len(box),len(box[0])
for i in reversed(range(len(box))):
    for j in range(len(box[0])):
        # print('i=',i,'j=',j)
        # print('j=',j,'i=',m-1-i)
        new_box[j][m-1-i] = box[i][j]
print(new_box)

