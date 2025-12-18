import streamlit as st
import pandas as pd
import plotly.express as px

# 1. 페이지 설정 및 다크모드 가독성 테마
st.set_page_config(page_title="모두의 AI 공론장", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    .stTabs [data-baseweb="tab"] { color: #FFFFFF; font-weight: 700; font-size: 16px; }
    .status-card { 
        background-color: #262730; 
        padding: 15px; 
        border-radius: 10px; 
        border-left: 5px solid #3498db;
        margin-bottom: 10px;
    }
    .status-tag {
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: bold;
        margin-right: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. 사이드바 및 상태 관리
with st.sidebar:
    st.title("🌈 모두의 AI 공론장")
    st.write("제안에서 정책화까지, AI 시대를 함께 만듭니다.")
    st.divider()
    
    # 의제 선택 (프로토타입 3종 반영)
    issue_options = [
        "AI 업종 주 52시간제 특례 도입 [숙의중]", 
        "AI 학습데이터 저작권 배분 [PoC중]", 
        "돌봄 현장 AI 적용 가이드 [제안중]"
    ]
    selected_full = st.selectbox("현재 다루고 있는 의제", issue_options)
    selected_issue = selected_full.split(" [")[0]

# 3. 메인 화면 - 실시간 통합 타임라인 (Dashboard)
st.title("🚀 실시간 정책 추진 타임라인")
st.write("국가 AI 정책들이 현재 어떤 단계에 있는지 한눈에 확인하세요.")

timeline_data = [
    {"의제": "AI 주 52시간 특례", "단계": "숙의 중", "진행도": 60, "색상": "#3498db"},
    {"의제": "AI 저작권 모델", "단계": "실증(PoC) 중", "진행도": 85, "색상": "#f1c40f"},
    {"의제": "돌봄 AI 가이드", "단계": "의제 제안", "진행도": 20, "색상": "#e67e22"},
    {"의제": "공공 AI 챗봇", "단계": "정책화 완료", "진행도": 100, "색상": "#2ecc71"}
]

cols = st.columns(len(timeline_data))
for i, item in enumerate(timeline_data):
    with cols[i]:
        st.markdown(f"""
        <div class="status-card">
            <span class="status-tag" style="background-color:{item['색상']};">{item['단계']}</span>
            <div style="margin-top:10px; font-weight:bold;">{item['의제']}</div>
        </div>
        """, unsafe_allow_html=True)
        st.progress(item['진행도']/100)

st.divider()

# 4. 의제별 상세 프로세스 탭
tab1, tab2, tab3, tab4 = st.tabs(["📝 의제 제안", "💬 집중 숙의", "🧪 실증 실험실(PoC)", "📂 정책 아카이브"])

# TAB 1: 의제 제안 (직접 의견 작성 및 AI 분류)
with tab1:
    st.header("💡 새로운 제안과 현장의 목소리")
    st.write("AI 전환 과정에서 느끼는 불편함이나 아이디어를 자유롭게 적어주세요.")
    
    with st.form("suggestion_form"):
        user_id = st.text_input("닉네임 또는 단체명")
        subject = st.text_input("제안 제목")
        content = st.text_area("제안 내용 (상세히 작성해주세요)")
        category = st.selectbox("관련 분야", ["노동/산업", "저작권/창작", "윤리/안전", "교육/복지"])
        
        if st.form_submit_button("제안 제출하기"):
            st.success("제안이 접수되었습니다! AI가 유사 의제를 통합하여 숙의 트랙으로 연결합니다.")

# TAB 2: 집중 숙의 (조건부 합의 및 토론)
with tab2:
    st.header(f"💬 {selected_issue}")
    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        st.subheader("숙의 참여 (조건부 입장)")
        st.write("단순 찬반을 넘어, 정책 설계에 필요한 '조건'을 조율합니다.")
        with st.form("delib_form"):
            position = st.radio("나의 입장", ["찬성", "반대", "유보"], horizontal=True)
            st.write("필수 전제 조건 (중복 선택 가능)")
            st.checkbox("연속 휴식 시간 의무화 (노동권 보호)")
            st.checkbox("수익 배분 알고리즘 공개 (투명성)")
            st.checkbox("사고 발생 시 책임 소재 명문화 (안전)")
            
            st.text_area("추가적인 보완책이나 반론을 적어주세요.")
            if st.form_submit_button("숙의 결과에 반영하기"):
                st.balloons()
                st.success("귀하의 의견이 숙리 리포트 초안에 반영되었습니다.")

    with col_right:
        st.subheader("실시간 숙의 분석 리포트 (AI)")
        # 합의 지점 시각화 [cite: 1510, 1584]
        analysis_df = pd.DataFrame({
            "조건": ["휴식보장", "수익투명", "책임명시"],
            "합의 가능성(%)": [82, 65, 91]
        })
        fig = px.bar(analysis_df, x="조건", y="합의 가능성(%)", template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)

# TAB 3: 실증 실험실 (PoC 현황)
with tab3:
    st.header("🧪 실증 파이프라인 (PoC)")
    st.write("숙의를 통해 도출된 최소 합의안이 현장에서 어떻게 작동하는지 검증합니다.") 
    
    poc_table = pd.DataFrame([
        {"의제": "AI 주 52시간 특례", "실증 과제": "연속휴식제 준수 사업장 생산성 측정", "상태": "계획 수립", "기간": "26.4Q~"},
        {"의제": "AI 저작권 모델", "실증 과제": "표준 계약 기반 수익배분 시스템 PoC", "상태": "실행 중", "기간": "26.3Q~"},
        {"의제": "돌봄 AI 가이드", "실증 과제": "현장 오탐 대응 프로토콜 테스트", "상태": "의제 선정", "기간": "-"}
    ])
    st.table(poc_table)

# TAB 4: 정책 아카이브 (환류 및 정책화)
with tab4:
    st.header("📂 정책 아카이브 및 환류")
    st.write("숙의와 실증을 거쳐 최종 결정된 정책 내용을 투명하게 공개합니다.")
    
    with st.expander("✅ [완료] 공공 AI 가이드라인 적용 결과"):
        st.info("정부 답변: 수용 (시행령 제5조 반영 완료)")
        st.write("- 숙의 결과: 책임 주체를 '운영사'로 명문화하기로 합의함.")
        st.write("- 실증 성과: 3개월간의 시범 운영 결과 행정 효율 25% 향상 확인.")
        st.download_button("최종 리포트 다운로드 (PDF)", "Sample Content", file_name="AI_Policy_Final.pdf")
