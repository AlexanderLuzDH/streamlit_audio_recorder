# streamlit_audio_recorder by stefanrmmr (rs. analytics) - version April 2022

import os
import numpy as np
import streamlit as st
from io import BytesIO
import streamlit.components.v1 as components

import speech_recognition as sr
import pyaudio

############################################################
if 'mic_input' not in st.session_state:
    st.session_state.mic_input = ""
    

if 'val' not in st.session_state:
    st.session_state.val = ""

    
#########################################################################

# DESIGN implement changes to the standard streamlit UI/UX
st.set_page_config(page_title="streamlit_audio_recorder")
# Design move app further up and remove top padding
st.markdown('''<style>.css-1egvi7u {margin-top: -3rem;}</style>''',
    unsafe_allow_html=True)
# Design change st.Audio to fixed height of 45 pixels
st.markdown('''<style>.stAudio {height: 45px;}</style>''',
    unsafe_allow_html=True)
# Design change hyperlink href link color
st.markdown('''<style>.css-v37k9u a {color: #ff4c4b;}</style>''',
    unsafe_allow_html=True)  # darkmode
st.markdown('''<style>.css-nlntq9 a {color: #ff4c4b;}</style>''',
    unsafe_allow_html=True)  # lightmode


def audiorec_demo_app():

    parent_dir = os.path.dirname(os.path.abspath(__file__))
    # Custom REACT-based component for recording client audio in browser
    build_dir = os.path.join(parent_dir, "st_audiorec/frontend/build")
    # specify directory and initialize st_audiorec object functionality
    st_audiorec = components.declare_component("st_audiorec", path=build_dir)

    
    # STREAMLIT AUDIO RECORDER Instance
    st.session_state.val = st_audiorec()
      
if __name__ == '__main__':

    # call main function
    audiorec_demo_app()


####################################################### SPEECH TO TEXT
 

# get audio from the microphone
r = sr.Recognizer()

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    st.session_state.mic_input = r.recognize_google(st.session_state.val) 
    st.write(st.session_state.mic_input)
except sr.UnknownValueError:
    st.write("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    st.write("Could not request results from Google Speech Recognition service; {0}".format(e))

