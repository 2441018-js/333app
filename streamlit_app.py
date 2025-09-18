import streamlit as st

# 앱 제목 설정
st.title('간단 덧셈 계산기 ✨')

# 사용자로부터 숫자 두 개를 입력받습니다.
# st.number_input은 숫자 입력 필드를 만들어줍니다.
number1 = st.number_input('첫 번째 숫자를 입력하세요', value=0)
number2 = st.number_input('두 번째 숫자를 입력하세요', value=0)

# '더하기' 버튼을 만듭니다.
# 이 버튼을 클릭하면 if 문 안의 코드가 실행됩니다.
if st.button('결과 보기'):
    # 두 숫자를 더합니다.
    result = number1 + number2
    
    # 결과를 화면에 표시합니다.
    # f-string을 사용해 깔끔하게 출력합니다.
    st.subheader(f'결과: {number1} + {number2} = {result}')
    

