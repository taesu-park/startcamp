"""
Python dictionary 연습 문제
"""

# # # 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# # # 아래에 코드를 작성해 주세요.

# # average = sum(score.values()) / len(score)
# # print(average)

# # # 선생님답
result = 0
count = 0
for score_value in score.values():
    result = result + score_value   # result += score_value
    count = count + 1   # count += 1
print(result/count)




# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# # 아래에 코드를 작성해 주세요.

# a1 = sum(scores['a'].values()) / len(scores['a'])
# b1 = sum(scores['b'].values()) / len(scores['b'])
# c = sum(a1+b1) / len(scores())
# print(c)

# # 선생님 답
total_score = 0
count = 0
for person_scores in scores.values():
    for score in person_scores.values():
        total_score += score
        count += 1
print(total_score/count)

# # 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# # 3-1. 도시별 최근 3일의 온도 평균은?

# # 아래에 코드를 작성해 주세요.

for name, temp in city.items():
    avg = sum(temp)/len(temp)
    print(f'{name} : {avg:.2f}')    # f-string : 3.6+
    print('{} : {:.2f}'.format(name,avg))

  

# seoul = 


# print('==== Q3-1 ====')
# """
# 출력 예시)
# 서울 : 값
# 대전 : 값
# 광주 : 값
# 부산 : 값
# """





# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')


min_temp = 0
max_temp = 0
min_city = ''
max_city = ''

count = 0


for name, temp in city.items():
    # 첫번째 반복때는 모두 다 저장해!
    if count == 0:
        min_city = name
        max_city = name
        min_temp = min(temp)
        max_temp = max(temp)
        count += 1
# 가장 추우면, 해당 도시와 기온을 기록
    if min(temp) < min_temp:
        min_city = name
        min_temp = min(temp)
# 더울 때도, 해당 도시와 기온을 기록
    if max(temp) > max_temp:
        max_city = name
        max_temp = max(temp)
print(f'추운곳은 {name} : {min_temp}, 더운곳은 {name}:{max_temp}')

# 모든 지역의 온도를 모두 확인하면서,

# 가장 추우면, 해당 도시와 기온을 기록
# 더울 때도, 해당 도시와 기온을 기록





# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
# print('==== Q3-3 ====')
if 2 in city['서울']:
    print('네!')
else:
    print('ㄴ')
