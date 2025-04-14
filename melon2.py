import requests
from bs4 import BeautifulSoup
import random
import time

# ======================== #
# 멜론 차트 데이터 수집
# ======================== #

headers = {
    "User-Agent": "Mozilla/5.0"
}

melon_url = "https://www.melon.com/chart/index.htm"
response = requests.get(melon_url, headers=headers)

# 멜론 차트는 JavaScript로 데이터를 렌더링하므로, 직접 요청으로는 데이터 수집이 어렵습니다.
# 여기서는 예시로 임의의 Top 10 데이터를 사용하겠습니다.

songs = [
    "IVE - HEYA",
    "ILLIT - Magnetic",
    "Zico - SPOT!",
    "BIBI - Bam Yang Gang",
    "NewJeans - OMG",
    "SEVENTEEN - MAESTRO",
    "(G)I-DLE - Fate",
    "LE SSERAFIM - Easy",
    "TAEYEON - To. X",
    "AKMU - Love Lee"
]

# 추가 음악 (임의)
extra_songs = [
    "Crush - Nappa", "Red Velvet - Psycho", "BTS - Dynamite", "IU - Love Poem",
    "BLACKPINK - How You Like That", "Heize - You, Clouds, Rain", "Jungkook - Seven",
    "Baekhyun - Candy", "BIGBANG - Still Life", "aespa - Spicy"
]
songs.extend(extra_songs)

# ======================== #
# 메뉴 출력
# ======================== #
print("==============================")
print("       🎵 멜론 추천 시스템")
print("==============================")
print("1. 멜론 차트 100 보기")
print("2. 인기곡 Top 5")
print("3. 랜덤 음악 추천")
print("4. 노래 검색")
print("==============================")

n = input("메뉴를 선택하세요 (1~4): ")

# ======================== #
# 메뉴 기능
# ======================== #

if n == "1":
    print("\n📌 멜론 차트 Top 100:")
    for i, song in enumerate(songs, 1):
        print(f"{i}. {song}")

elif n == "2":
    print("\n💎 인기곡 Top 5:")
    for i, song in enumerate(songs[:5], 1):
        print(f"{i}. {song}")

elif n == "3":
    print("\nAI야 노래 추천해줘!")
    print("""
    네!
    분석 중입니다...
    잠시만요 🎧
    """)
    dd = ["둠", "두둠", "두둠칫", "두둥탁"]
    for d in dd:
        print(d)
        time.sleep(1)
    recommended_song = random.choice(songs)
    print(f"✨ 추천 곡은: {recommended_song} 입니다!")

elif n == "4":
    keyword = input("🔍 검색할 노래 제목이나 가수를 입력하세요: ")
    results = [s for s in songs if keyword.lower() in s.lower()]
    if results:
        print("\n🔎 검색 결과:")
        for r in results:
            print(f"- {r}")
    else:
        print("😢 해당 노래를 찾을 수 없습니다.")

else:
    print("⚠️ 1~4 중에서 입력해주세요.")
