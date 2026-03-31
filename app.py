import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정 (브라우저 탭 이름 및 레이아웃)
st.set_page_config(page_title="태양광 수익 시뮬레이터", layout="wide")

# HTML 파일 읽기 (기존에 제가 드린 코드를 index.html로 저장했다고 가정)
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Streamlit 화면에 HTML 표시 (화면 너비에 맞춤)
components.html(html_code, height=1200, scrolling=True)
