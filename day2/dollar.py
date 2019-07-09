import requests
from bs4 import BeautifulSoup


# 1. url 설정
url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%8B%AC%EB%9F%AC'
# 2. 요청 보내기
response = requests.get(url).text
# 3. HTML 문서로 바꾸기
soup = BeautifulSoup(response,'html.parser')
# 4. 원하는 내용 선택자로 뽑아내기

dollar = soup.select_one('body > div > table > tbody > tr').text
# body > div > table > tbody > tr:nth-child(1) > td.sale
print(dollar)

