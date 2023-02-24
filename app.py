import streamlit as st
from PIL import Image
import numpy as np
import sounddevice as sd

def main():
    st.set_page_config(page_title="KI Musik",page_icon="🎵",layout="centered")
    hide_streamlit_style = """
             <style>
              div.block-container{padding-top:2rem;}
             </style>
             """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.title("🎵 KI Musik")
    uploaded_file = st.file_uploader("Wähle ein Bild aus...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        try:
            img = Image.open(uploaded_file)
            st.image(img, caption='Uploaded Image', use_column_width=True)
        except:
            st.write("Bitte anderes Bild auswählen.")
       # try:
      if st.button("Sound genießen "):
            img_array = np.array(img)
            sound=np.reshape(img_array, (-1, 1))
            fs = 44100
            sd.play(sound, fs)
       # except:
       #     st.write("Fehler beim Konvertieren, bitte App neu laden.")
    else:
        st.write("Bitte Bild hochladen, um Musik zu erzeugen.")

if __name__ == '__main__':
      main()
