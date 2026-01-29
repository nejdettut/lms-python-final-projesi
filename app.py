import streamlit as st
from database import *
from api import analyze_text
create_tables()
st.title("Python Final Projesi LMS Sistemi")
menu = st.selectbox("Menü", ["Giriş", "Kayıt", "Kurslar", "Admin"])
if menu == "Kayıt":
    u = st.text_input("Kullanıcı Adı")
    p = st.text_input("Şifre", type="password")
    if st.button("Kayıt Ol"):
        if register_user(u, p):
            st.success("Kayıt başarılı")
        else:
            st.error("Kullanıcı zaten var")
elif menu == "Giriş":
    u = st.text_input("Kullanıcı Adı")
    p = st.text_input("Şifre", type="password")
    if st.button("Giriş Yap"):
        if login_user(u, p):
            st.success("Hoş geldiniz")
        else:
            st.error("Hatalı giriş")
elif menu == "Admin":
    title = st.text_input("Kurs Başlığı")
    desc = st.text_area("Açıklama")
    if st.button("Kurs Ekle"):
        add_course(title, desc)
        st.success("Kurs eklendi")
elif menu == "Kurslar":
    courses = get_courses()
    for c in courses:
        st.subheader(c["title"])

        st.write(c["description"])
