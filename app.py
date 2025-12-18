import streamlit as st
import pandas as pd
import plotly.express as px

# 1. 페이지 설정 및 가독성 테마 적용
st.set_page_config(page_title="모두의 AI 공론장", layout="wide")

# 배경색과 글자색의 충돌을 방지하는 커스텀 CSS
st.markdown("""
    <style>
    /* 전체 배경은 흰색, 글자는 짙은 회색으로 고정 */
    .stApp {
        background-color: #FFFFFF;
        color: #262730;
    }
    /* 정보 카드의 가독성 확보 */
    .info-card {
        background-color: #F0F4F8;
        color: #1A1C20;
        padding: 25px;
        border-radius: 12px;
        border-left: 6px solid #005BAA;
        margin-bottom: 20px;
        line-height: 1.6;
    }
    /* 탭 메뉴 글자 크기 및 색상 */
    .stTabs [data-baseweb="tab"] {
        font-size: 18px;
        font-weight: 700;
        color: #4A4A4A;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. 사이드바 (기관명 제외)
with st.sidebar:
    st.title("🌈 모두의 AI 공론장")
    st.write("AI 시대를 함께 디자인하는 시민들의 공간입니다.")
    st.divider()
    
    current_issue = st.selectbox(
        "현재 진행 중인 숙의",
        ["AI 산업 주 52시간제 특례 도입", "AI 학습데이터와 창작자 권리", "공공부문 AI 책임 가이드라인"]
    )
    st.success("지금 '대안 조합' 단계가 한창이에요! 😊")

# 3. 메인 화면 구성
st.title(f"✨ {current_issue}")

# 파이프라인을 시각적으로 보여주는 단계 안내
st.markdown("""
[제안] → [숙의] → [실증사업] → [정책화]
""")

# 탭 구성: 제안 -> 숙의 -> 실증 -> 정책화 (액션플랜 구조 반영)
tab1, tab2, tab3, tab4 = st.tabs(["🔍 쟁점 정의", "💬 시민 숙의", "🚀 실증 실험", "📂 우리들의 기록"])

# TAB 1: 쟁점 정의
with tab1:
    st.subheader("이 문제는 왜 중요한가요?")
    st.markdown(f"""
    <div class="info-card">
    AI 기술이 빠르게 발전하면서 기존의 규칙으로는 담기 어려운 고민들이 생겨나고 있어요. <br>
    성장과 안전, 효율과 권리 사이의 균형점을 찾는 과정입니다.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("💡 **혁신과 기회**\n\n- 국가 기술 경쟁력 확보\n- 산업 전반의 효율성 증대")
    with col2:
        st.warning("⚠️ **보호와 안전**\n\n- 노동자의 건강권 및 휴식권\n- 기술 오남용 방지 및 책임 소재")

# TAB 2: 시민 숙의 (조건부 합의 수집)
with tab2:
    st.subheader("나의 생각 보태기")
    st.write("단순한 찬반을 넘어, 우리가 합의할 수 있는 '최소 조건'을 찾아주세요.")
    
    col_in, col_viz = st.columns([4, 6])
    with col_in:
        with st.form("delib_form"):
            pos = st.radio("나의 입장", ["찬성", "반대", "유보"], horizontal=True)
            st.write("어떤 약속이 전제되어야 할까요?")
            c1 = st.checkbox("연속 휴식 시간 의무화")
            c2 = st.checkbox("성과에 대한 공정한 배분 체계")
            c3 = st.checkbox("문제가 생겼을 때의 책임 주체 명시")
            
            opinion = st.text_area("구체적인 제안을 적어주세요.")
            if st.form_submit_button("의견 전달하기"):
                st.balloons()
                st.success("소중한 의견이 리포트에 반영됩니다!")

    with col_viz:
        st.write("현재까지 모인 숙의 현황 (AI 분석)")
        df = pd.DataFrame({"항목": ["휴식보장", "배분체계", "책임명시"], "합의도": [85, 62, 94]})
        fig = px.bar(df, x="항목", y="합의도", color="합의도", color_continuous_scale="Blues")
        st.plotly_chart(fig, use_container_width=True)

# TAB 3: 실증 실험 (26년 4Q 목표)
with tab3:
    st.subheader("행동으로 이어지는 실증 프로젝트")
    st.write("숙의를 통해 도출된 해결책을 현장에서 직접 검증합니다.")
    
    
    
    st.table(pd.DataFrame([
        {"분야": "노동", "실증 과제": "AI 개발자 유연근로 실험", "상태": "준비 중"},
        {"분야": "저작권", "실증 과제": "학습데이터 수익배분 모델", "상태": "참여 모집"},
        {"분야": "복지", "실증 과제": "돌봄 로봇 현장 프로토콜 적용", "상태": "의제 선정"}
    ]))

# TAB 4: 우리들의 기록 (정책 반영 아카이브)
with tab4:
    st.subheader("정책 반영 및 환류")
    with st.expander("📂 완료된 공론장 결과 보기"):
        st.markdown("### 주제: 학교 AI 도구 도입 가이드라인")
        st.write("- **최종 합의**: 학생/교사 동의 절차 필수화 (조건부 수용)")
        st.write("- **결과**: 관련 지침 제5조 개정안에 반영 완료")
        st.success("정부 수용률: 85% (부분 수용 포함)")
