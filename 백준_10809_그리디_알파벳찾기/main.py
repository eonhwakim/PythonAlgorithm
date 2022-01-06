# 예제 입력 : baekjoon
# 출력 : 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
# a b c 순서대로
# a = 1번째 순서
# b = 0번째 순서
# c = 없으므로 -1
# e = 2번재 순서 ...
#=> 즉 입력받은 문자열에서 알파벳이 있으면 그 문자열의 인덱스 출력

s = input()
alph = 'abcdefghijklmnopqrstuvwxyz'

for i in alph:
    if i in s: # 문
        print(s.index(i), end = ' ')
    else:
        print(-1, end=' ')


#==================================
print("")

# 아스키코드를 이용해서 푸는 법 ord(c) : 문자의 유니코드 값을 돌려주는 함수
# a = 97
# 문자를 아스키코드로 변환하여 97을 뺀 인덱스에 문자열 위치를 입력해준다

s = input()
check = [-1] * 26

for i in range(len(s)):
    if check[ord(s[i])-97] != -1:
        continue
    else:
        check[ord(s[i])-97] = i
for i in range(26):
    print(check[i], end = ' ')