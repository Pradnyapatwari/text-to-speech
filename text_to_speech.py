import streamlit as st
import speech_recognition as sr

# Initialize Speech Recognizer
recognizer = sr.Recognizer()

st.title("Voice-to-Text Converter")

if st.button("Speak"):
    with sr.Microphone() as source:
        st.write("Listening...")
        audio_data = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio_data)
            st.success(f"You said: {text}")
        except sr.UnknownValueError:
            st.error("Sorry, I could not understand audio.")
        except sr.RequestError as e:
            st.error(f"Could not request results from Google Speech Recognition service; {e}")
