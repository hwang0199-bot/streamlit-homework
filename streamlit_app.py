import streamlit as st
import pandas as pd
import numpy as np

%%writefile streamlit_app.py
import streamlit as st
import pandas as pd

st.title("이번 학기 과목별 공부 부담 대시보드")
st.caption("10강 실습 과제")

st.markdown("""
이 대시보드는 이번 학기에 수강하는 과목별 공부 시간과 과제 부담도를 비교하기 위해 만들었습니다.  
과목을 선택하면 해당 과목의 주간 공부 시간, 과제 부담도, 시험 부담도, 만족도를 확인할 수 있습니다.
""")

# 데이터 만들기
data = {
    "과목": ["사회학개론", "통계학", "한국문학", "영화의 이해", "데이터과학"],
    "주간 공부 시간": [4, 7, 5, 3, 6],
    "과제 부담도": [3, 5, 4, 2, 5],
    "시험 부담도": [4, 5, 4, 2, 4],
    "수업 만족도": [5, 3, 4, 5, 4]
}

df = pd.DataFrame(data)

st.header("전체 데이터")
st.dataframe(df)

st.header("과목별 상세 보기")

selected_subject = st.selectbox("과목을 선택하세요", df["과목"])

selected_data = df[df["과목"] == selected_subject].iloc[0]

st.subheader(f"{selected_subject} 주요 지표")

col1, col2, col3, col4 = st.columns(4)

col1.metric("주간 공부 시간", f"{selected_data['주간 공부 시간']}시간")
col2.metric("과제 부담도", selected_data["과제 부담도"])
col3.metric("시험 부담도", selected_data["시험 부담도"])
col4.metric("수업 만족도", selected_data["수업 만족도"])

st.markdown("부담도와 만족도는 1점에서 5점 사이로 기록했습니다.")

st.header("과목별 주간 공부 시간 비교")
study_chart = df.set_index("과목")[["주간 공부 시간"]]
st.bar_chart(study_chart)

st.header("과목별 부담도 비교")

burden_type = st.radio(
    "비교할 부담도를 선택하세요",
    ["과제 부담도", "시험 부담도", "수업 만족도"]
)

burden_chart = df.set_index("과목")[[burden_type]]
st.bar_chart(burden_chart)

st.header("간단 해석")

if selected_data["과제 부담도"] >= 4:
    st.write(f"{selected_subject}은 과제 부담이 큰 편입니다.")
else:
    st.write(f"{selected_subject}은 과제 부담이 비교적 크지 않은 편입니다.")

if selected_data["수업 만족도"] >= 4:
    st.write(f"{selected_subject}은 수업 만족도가 높은 편입니다.")
else:
    st.write(f"{selected_subject}은 수업 만족도가 다소 낮은 편입니다.")
