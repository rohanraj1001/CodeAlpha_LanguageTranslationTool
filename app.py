import streamlit as st
from googletrans import Translator
from gtts import gTTS

st.title("🌐 Language Translation Tool")
text = st.text_area("Enter text to translate:")

languages = {
    'Auto Detect': 'auto',
    'English': 'en',
    'French': 'fr',
    'German': 'de',
    'Spanish': 'es',
    'Hindi': 'hi',
    'Chinese (Simplified)': 'zh-cn',
    'Arabic': 'ar'
}
src_lang = st.selectbox('Source Language', list(languages.keys()))
tgt_lang = st.selectbox('Target Language', list(languages.keys()))

if st.button("Translate"):
    if text.strip():
        translator = Translator()
        output = translator.translate(text, src=languages[src_lang], dest=languages[tgt_lang])
        st.subheader("Translated Text:")
        st.success(output.text)

        if st.checkbox("Play Translated Audio"):
            tts = gTTS(output.text, lang=languages[tgt_lang])
            tts.save("translated_audio.mp3")
            st.audio("translated_audio.mp3")
    else:
        st.warning("Please enter text to translate.")
