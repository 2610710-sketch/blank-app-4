import streamlit as st

# 제목 세팅
st.title('놀이기구 탑승 확인')

# 키 입력 받기 (정수형)
height = st.number_input('키를 입력하세요', value=150, step=1)

# 질문자님이 작성한 조건문 로직 그대로 적용 (print만 st.write로 변경)
if height < 100:
    st.write('탑승 불가')
elif height < 130:
    st.write('보호자 탑승 시 탑승 가능')
elif height < 195:
    st.write('탑승 가능')
else:
    st.write('탑승 불가')
