import streamlit as st
import pandas as pd
import plotly.express as px

# 1. 페이지 설정 및 다크모드 가독성 테마 적용
st.set_page_config(page_title="모두의 AI 공론장", layout="wide")

st.markdown("""
    <style>
    /* 검은 배경과 흰색 글씨 고정 */
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    /* 정보 카드 스타일 */
    .info-card {
        background-color: #262730;
        color: #FFFFFF;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #3498db;
        margin-bottom: 20px;
    }
    /* 탭 텍스트 색상 */
    .stTabs [data-baseweb="tab"] {
        color: #FFFFFF;
        font-weight: 600;
    }
    /* 입력창 및 폼 텍스트 색상 */
    label, p, span {
        color: #FFFFFF !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. 사이드바
with st.sidebar:
    st.title("🌈 모두의 AI 공론장")
    st.write("AI 시대를 함께 디자인하는 공간")
    st.divider()
    
    current_issue = st.selectbox(
        "현재 진행 중인 숙의",
        ["AI 산업 주 52시간제 특례 도입", "AI 학습데이터와 창작자 권리", "공공부문 AI 책임 가이드라인"]
    )
    st.success("대안 조합 단계 진행 중")

# 3. 메인 화면
st.title(f"✨ {current_issue}")

# 파이프라인 탭
tab1, tab2, tab3, tab4 = st.tabs(["🔍 쟁점 정의", "💬 시민 숙의", "🚀 실증 실험", "📂 정책 기록"])

# TAB 1: 쟁점 정의
with tab1:
    st.subheader("이 문제는 왜 중요한가요?")
    st.markdown("""
    <div class="info-card">
    AI 기술 발전에 따른 성장과 안전, 효율과 권리 사이의 균형점을 찾는 과정입니다.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("💡 **혁신과 기회**: 경쟁력 확보 및 효율성 증대")
    with col2:
        st.warning("⚠️ **보호와 안전**: 노동권 보호 및 책임 소재 명확화")

# TAB 2: 시민 숙의
with tab2:
    st.subheader("나의 생각 보태기")
    col_in, col_viz = st.columns([4, 6])
    with col_in:
        with st.form("delib_form"):
            pos = st.radio("나의 입장", ["찬성", "반대", "유보"], horizontal=True)
            st.write("합의를 위한 필수 조건")
            c1 = st.checkbox("연속 휴식 시간 의무화")
            c2 = st.checkbox("성과 배분 체계 수립")
            c3 = st.checkbox("책임 주체 명시")
            if st.form_submit_button("의견 제출"):
                st.success("반영되었습니다.")

    with col_viz:
        st.write("숙의 현황 (AI 분석)")
        df = pd.DataFrame({"조건": ["휴식보장", "배분체계", "책임명시"], "합의도": [85, 62, 94]})
        fig = px.bar(df, x="조건", y="합의도", template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)

# TAB 3: 실증 실험
with tab3:
    st.subheader("실증 프로젝트 (PoC) 현황")
    st.table(pd.DataFrame([
        {"분야": "노동", "과제": "AI 근로시간 유연화 실험", "상태": "준비 중"},
        {"분야": "저작권", "과제": "수익배분 모델 테스트", "상태": "참여 모집"}
    ]))

# TAB 4: 정책 기록
with tab4:
    st.subheader("정부 답변 및 아카이브")
    with st.expander("📂 가이드라인 개정 결과 보기"):
        st.write("최종 합의: 학생/교사 동의 절차 필수화")
        st.success("정부 정책 반영 완료")
