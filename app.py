# 영화 정보
movies = {
    "1": {
        "title": "해리포터: 마법사의 돌",
        "rating": "전체관람가",
        "min_age": 0,
        "선정성": "낮음",
        "폭력성": "낮음",
        "언어": "낮음"
    },
    "2": {
        "title": "듄",
        "rating": "12세 이상 관람가",
        "min_age": 12,
        "선정성": "낮음",
        "폭력성": "보통",
        "언어": "낮음"
    },
    "3": {
        "title": "오디세이",
        "rating": "15세 이상 관람가",
        "min_age": 15,
        "선정성": "보통",
        "폭력성": "높음",
        "언어": "보통"
    },
    "4": {
        "title": "범죄도시",
        "rating": "청소년 관람불가",
        "min_age": 19,
        "선정성": "높음",
        "폭력성": "높음",
        "언어": "높음"
    }
}

# 1. 영화 선택
print("===== 영화 목록 =====")

for number, movie in movies.items():
    print(number + ".", movie["title"], "-", movie["rating"])

choice = input("보고 싶은 영화의 번호를 입력하세요 >> ")

if choice not in movies:
    print("잘못된 영화 번호입니다.")

else:
    movie = movies[choice]

    # 2. 나이 입력
    try:
        age = int(input("나이를 입력하세요 >> "))

        if age < 0:
            print("올바른 나이를 입력하세요.")

        else:
            # 3. 보호자 입장 여부
            guardian = input("보호자와 함께 입장하시나요? (예/아니오) >> ")

            # 4. 관람 가능 여부 판단
            if age >= movie["min_age"]:
                can_watch = True

            elif movie["min_age"] == 19:
                can_watch = False

            elif guardian == "예":
                can_watch = True

            else:
                can_watch = False

            # 결과 출력
            print("\n===== 관람 결과 =====")

            if can_watch:
                print(movie["title"], "영화는 보실 수 있습니다.")

            else:
                print(movie["title"], "영화는 보실 수 없습니다.")

            # 영화 선정 기준 출력
            print("\n===== 영화 선정 기준 =====")
            print("관람 등급 :", movie["rating"])
            print("선정성 :", movie["선정성"])
            print("폭력성 :", movie["폭력성"])
            print("언어 :", movie["언어"])

    except ValueError:
        print("나이는 숫자로 입력해주세요.")
