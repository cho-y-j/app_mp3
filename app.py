import openai
import streamlit as st

# API 키 설정
openai.api_key = "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"

st.title('조사장의 성우 서비스')
st.write('글쓰기 입니다')

options = ['alloy', 'echo', 'fable', 'nova', 'shimmer']
selected_option = st.selectbox('성우선택', options)

default_text = "안녕하세요 성우 서비스에 오신걸 환영합니다."
prompt = st.text_area('프롬프트 입력', value=default_text, height=150)

if st.button('mp3파일생성'):
    # 음성 생성 호출
    response = openai.Audio.create(
        model="tts-1-hd",
        voice=selected_option,
        input=prompt,
        response_format="mp3"
    )
    audio_content = response['audio']

    with open('audio.mp3', 'wb') as audio_file:
        audio_file.write(audio_content)
    
    st.audio('audio.mp3', format='audio/mp3')
