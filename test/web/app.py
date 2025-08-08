import streamlit as st

st.title("챗봇이야")

# streamlit에게 message_history 기억하게 하는 코드
if "message_history" not in st.session_state:
    st.session_state.message_history = []
# 사용자의 입력 데이터
# 사용자가 입력을 하지 않았다면 -> prompt = None
prompt = st.chat_input("무엇이든지 물어봐 주세요")

# prompt가 string이면서, 입력데이터가 존재할 때
if isinstance(prompt, str) and prompt.strip(): # 사용자의 입력 데이터가 만약 있다면
    st.session_state.message_history.append(
        ("user", prompt) # 사용자가 입력하게 되면, message_history 에 추가 
    )

    
for message in st.session_state.message_history: # 화면에 message_history 프린트
    with st.chat_message(message[0]): # 사용자 아이콘
        st.markdown(message[1]) # 사용자의 입력 메시지