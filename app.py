
import streamlit as st

st.title("🎬 영화 관람 가능 여부 확인 프로그램")

# 영화 정보
movies = {
    "영화 A": {
        "rating": "해리포터와 마법사의 돌",
        "min_age": 0,
        "선정성": "낮음",
        "폭력성": "낮음",
        "언어": "낮음"
    },
    "듄": {
        "rating": "12세 이상 관람가",
        "min_age": 12,
        "선정성": "낮음",
        "폭력성": "보통",
        "언어": "낮음"
    },
    "오디세이": {
        "rating": "15세 이상 관람가",
        "min_age": 15,
        "선정성": "보통",
        "폭력성": "높음",
        "언어": "보통"
    },
    "범죄도시": {
        "rating": "청소년 관람불가",
        "min_age": 19,
        "선정성": "높음",
        "폭력성": "높음",
        "언어": "높음"
    }
}

# 1. 영화 선택
st.subheader("1. 보고 싶은 영화를 선택하세요.")

choice = st.selectbox(
    "영화 목록",
    list(movies.keys())
)

movie = movies[choice]

# 영화 관람 등급 표시
st.info("관람 등급: " + movie["rating"])

# 2. 나이 입력
st.subheader("2. 나이를 입력하세요.")

age = st.number_input(
    "나이",
    min_value=0,
    max_value=100,
    value=17,
    step=1
)

# 3. 보호자 동반 여부
st.subheader("3. 보호자와 함께 입장하시나요?")

guardian = st.radio(
    "보호자 입장 여부",
    ["예", "아니오"],
    horizontal=True
)

# 4. 결과 확인
if st.button("관람 가능 여부 확인"):

    if age >= movie["min_age"]:
        can_watch = True

    elif movie["min_age"] == 19:
        can_watch = False

    elif guardian == "예":
        can_watch = True

    else:
        can_watch = False

    # 관람 결과 출력
    st.subheader("🎥 관람 결과")

    if can_watch:
        st.success(choice + " 영화는 보실 수 있습니다.")
    else:
        st.error(choice + " 영화는 보실 수 없습니다.")

    # 영화 선정 기준 출력
    st.subheader("📋 영화 선정 기준")

    st.write("관람 등급 :", movie["rating"])
    st.write("선정성 :", movie["선정성"])
    st.write("폭력성 :", movie["폭력성"])
    st.write("언어 :", movie["언어"])

