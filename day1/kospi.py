# 0. requests 패키지를 불러온다.
# pip install requests : 요청을 보내주는 패키지
# pip install bs4 : 문서를 찾기 편하게 바꿔주는 패키지(파싱)

import requests
from bs4 import BeautifulSoup


# 1. url로 요청(requests.get)을 보내고, response에 저장한다.
url = 'https://finance.naver.com/sise/'
response = requests.get(url).text
#print(response.text)
#print(type(response.text))

# 2. python이 찾기 편한 방식으로 문서를 변경한다.
soup = BeautifulSoup(response, 'html.parser')
print(soup)
print(type(response))
print(type(soup))

# 3. KOSPI 값을 찾는다
kospi = soup.select_one('#KOSPI_now').text
print(kospi)

