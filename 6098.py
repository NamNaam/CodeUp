# 6098 : [기초-리스트] 성실한 개미(py)
'''
영일이는 생명과학에 관심이 생겨 왕개미를 연구하고 있었다.

왕개미를 유심히 살펴보던 중 특별히 성실해 보이는 개미가 있었는데,
그 개미는 개미굴에서 나와 먹이까지 가장 빠른 길로 이동하는 것이었다.

개미는 오른쪽으로 움직이다가 벽을 만나면 아래쪽으로 움직여 가장 빠른 길로 움직였다.
(오른쪽에 길이 나타나면 다시 오른쪽으로 움직인다.)

이에 호기심이 생긴 영일이는 그 개미를 미로 상자에 넣고 살펴보기 시작하였다.

미로 상자에 넣은 개미는 먹이를 찾았거나, 더 이상 움직일 수 없을 때까지
오른쪽 또는 아래쪽으로만 움직였다.

미로 상자의 구조가 0(갈 수 있는 곳), 1(벽 또는 장애물)로 주어지고,
먹이가 2로 주어질 때, 성실한 개미의 이동 경로를 예상해보자.

단, 맨 아래의 가장 오른쪽에 도착한 경우, 더 이상 움직일 수 없는 경우, 먹이를 찾은 경우에는
더이상 이동하지 않고 그 곳에 머무른다고 가정한다.

미로 상자의 테두리는 모두 벽으로 되어 있으며,
개미집은 반드시 (2, 2)에 존재하기 때문에 개미는 (2, 2)에서 출발한다.
'''

array = [[0]*10 for _ in range(10)] # 리스트 초기화

for i in range(10) : # 리스트 입력
    s = list(map(int,input().split()))
    for j in range(10) :
        array[i][j] = s[j]

# 길찾기
init = 1
fin = 0
for i in range(1, 10) :
    if fin == 1 : # 2단 루프 끝내기 위한 조건문
        break
    for j in range(init, 10) :
        if array[i][j] == 0 :
            array[i][j] = 9
        elif array[i][j] == 1 :
            init = j-1 # 이전 리스트의 마지막 인덱스를 이어서 시작
            if array[i+1][init] == 1 : # 길이 막혔을 때 종료
                fin = 1
            break
        else : # 먹이 발견했을 때 종료
            array[i][j] = 9
            fin = 1
            break

for i in range(10) : # 리스트 출력
    for j in range(10) :
        print(array[i][j],end = ' ')
    print()


'''
m=[]
for i in range(12) :
  m.append([])
  for j in range(12) :
    m[i].append(0)

for i in range(10) :
  a=input().split()
  for j in range(10) :
    m[i+1][j+1]=int(a[j])

x = 2
y = 2
while True :
  if m[x][y] == 0 :
    m[x][y] = 9
  elif m[x][y] == 2 :
    m[x][y] = 9
    break

  if (m[x][y+1]==1 and m[x+1][y]==1) or (x==9 and y==9) :
    break

  if m[x][y+1] != 1 :
    y += 1
  elif m[x+1][y] != 1 :
    x += 1
    

for i in range(1, 11) :
  for j in range(1, 11) :
    print(m[i][j], end=' ')
  print()
'''
