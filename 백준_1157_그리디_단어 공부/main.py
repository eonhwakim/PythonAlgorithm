
# 빈 리스트를 생성하고 개수를 센 수를 리스트에 추가 -> 리스트에서 가장 큰 수를 출력
# 출력 : 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.


word = input().upper()
# 입력받은 문자열에서 중복값을 제거
uniq_word = list(set(word))

cnt_list = []
for i in uniq_word:
    cnt = word.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1: # 숫자 최댓값이 중복되면
    print('?')
else:
    # 숫자 최댓값 인덱스(위치)에 위치한 문자열 출력
    max_index = cnt_list.index(max(cnt_list))
    print(uniq_word[max_index])

