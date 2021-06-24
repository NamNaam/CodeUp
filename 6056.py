# 2개의 정수값이 입력될 때, 그 불 값(True/False)이 서로 다를 때에만 True를 출력하는 프로그램을 작성해보자.
# XOR 연산

a, b = map(int,input().split())
c, d = map(bool,(a,b))
print((c and (not d)) or ((not c) and d))

'''
0 0
c = false d = false
(false and true) or (true and false)
false or false
false

0 1
c = false d = true
(false and false) or (true and ture)
false or true
true

1 0
c = true d = false
(true and ture) or (false and false)
true or false
ture

1 1
c = true d = ture
(true and false) or (false and true)
false or false
false
'''
