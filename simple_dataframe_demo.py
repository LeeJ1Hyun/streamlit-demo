import streamlit as st
import pandas as pd
 
st.write("""
# Stremlit을 활용한 도, 소매 rating data
아래 표를 봐주세요.
""")
 
DATA_PATH = '/home/ec2-user/data/ws_binary_rating_data.csv'
df = pd.read_csv(DATA_PATH)
df_selected = df.head(10)
st.dataframe(df_selected, use_container_width=True)