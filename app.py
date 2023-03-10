import streamlit as st
from PIL import Image
import numpy as np
import scipy.io.wavfile as wav
#import io

def main():
    st.set_page_config(page_title="KI Musik",page_icon="🎵",layout="centered")
    hide_streamlit_style = """
             <style>
              div.block-container{padding-top:1rem;}
               div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
             </style>
             """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.title("🎵 KI Musik")
    uploaded_file = st.file_uploader("Wähle ein Bild aus...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        try:
            img = Image.open(uploaded_file)
        except:
            st.write("Bitte anderes Bild auswählen.")
        try:
            if st.button("Sound genießen "):
                img_array = np.array(img)
                sound=np.reshape(img_array, (-1, 1))
                wav_bytes = wav.write("audio.wav", 44100, sound)
                audio_data = open("audio.wav", "rb").read()
                st.audio(audio_data, format="audio/wav")
                st.image(img, caption='Uploaded Image', use_column_width=True)
                #audio_bytes = io.BytesIO(audio_data)
                #st.download_button(label="Download Audio", data=audio_bytes, file_name="audio.wav", mime="audio/wav")
        except:
            st.write("Fehler beim Konvertieren, bitte App neu laden.") 
    else:
        st.write("Bitte Bild hochladen, um Musik zu erzeugen.")

if __name__ == '__main__':
      main()
