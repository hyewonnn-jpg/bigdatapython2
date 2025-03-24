from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# 셀레니움 설정
options = Options()
options.add_argument('--headless')  # 브라우저 창 안 띄움
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# 드라이버 실행 (크롬드라이버 경로는 본인 환경에 맞게 수정)
driver = webdriver.Chrome(options=options)

# 멜론 차트 페이지 접속
url = 'https://www.melon.com/chart/index.htm'
driver.get(url)
time.sleep(3)  # 페이지 로딩 대기

# iframe이 있을 경우 switch 필요 (2024년 기준 필요 없음)

# 제목과 아티스트 추출
titles = driver.find_elements(By.CSS_SELECTOR, 'div.ellipsis.rank01 a')
artists = driver.find_elements(By.CSS_SELECTOR, 'div.ellipsis.rank02 span a')

print("🎵 멜론 TOP 100 차트 🎵
