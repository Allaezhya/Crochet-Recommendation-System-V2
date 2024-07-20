import streamlit as st
import pickle
import pandas as pd
from PIL import Image
import requests
import numpy as np
import io

def recommend(kerajinan):
    index = crochet[crochet['kerajinan'] == kerajinan].index[0]
    crochet_list = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]

    recommended_crochet = []
    base_url = './app/static/'
    for i in crochet_list:
        kerajinan_name = crochet.iloc[i[0]].kerajinan
        link = crochet.iloc[i[0]].link
        image_jalur = crochet.iloc[i[0]].gambar

        full_image_path = base_url + image_jalur

        recommended_crochet.append([kerajinan_name, link, full_image_path])
    return recommended_crochet

crochet_dict = pickle.load(open('crochet_dict.pkl', 'rb'))
crochet = pd.DataFrame(crochet_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Sistem Rekomendasi Kerajinan Rajut")

selected_crochet = st.selectbox("Mencari projek selanjutnya? Pilih salah satu",
crochet['kerajinan'].values)

if st.button("Rekomendasikan"):
    recommendations = recommend(selected_crochet)
    st.write(f"Rekomendasi untuk {selected_crochet}")

    for rec in recommendations:
        kerajinan_name, link, gambar = rec
        st.header(f'{kerajinan_name}')
        st.link_button("Tutorial", f"{link}")
        st.markdown(f"[![Click me]({gambar})]({link})")
        st.divider()
