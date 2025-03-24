import requests
from bs4 import BeautifulSoup

# 1. 타겟 사이트 접속
url = 'https://www.4flix.co.kr/netflixranking/animation'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 2. 순위별 콘텐츠 가져오기
titles = soup.select('div.col.rank-content div.tit')

print('🎬 넷플릭스 애니메이션 인기 TOP 10 (출처: 4FLIX)\n')
for i in range(10):
    rank = i + 1
    title = titles[i].get_text(strip=True)
    print(f'{rank}위: {title}')
