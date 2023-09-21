import streamlit as st
import random 
st.title("おみくじアプリ")
if st.button("おみくじを引く"):
    results=["lucky","civil","matter","negrect","papa","mama"]
    result=random.choice(results)
    st.write(f"結果：{result}")
