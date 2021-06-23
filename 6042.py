# 실수 1개를 입력받아 소숫점 이하 두 번째 자리까지의 정확도로 반올림한 값을 출력해보자.

a = float(input())

print(round(a,2))
print(f'{a:.2f}')
print(format(a,".2f"))

# 세 가지 모두 결과는 동일하다.
