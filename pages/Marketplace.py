import streamlit as st
import pandas as pd

df = pd.read_excel("./pages/Source.xlsx")

s,c,p,pr = st.columns(4)
with s:
    selection_store = st.selectbox("Select store", df['Store'].unique())

    df = df[df['Store'] == selection_store]

with c:
    selection_category = st.selectbox("Select food category", df['Category'].unique())

    df = df[df['Category'] == selection_category]

with p:
    selection_product = st.selectbox("Select Product Name", df['Product_Name'].unique())

    df = df[df['Product_Name'] == selection_product]

with pr:
    lowest_price = (df['Price'].min())
    highest_price = (df['Price'].max())
    selection_price = st.slider("Price Range", min_value = lowest_price, max_value = highest_price)

num_of_columns = 4 # create variable to set the column
columns = st.columns(num_of_columns) # create the column


for i in range(len(df)):
    record = df.iloc[i]
    with columns[i]:
        st.image(f'{record['Picture']}',width=250)
        st.write(f'{record['Product_Name']}')
        st.write(f'{record['Price']}')

st.dataframe(df)

#st.write(df.columns)
#st.write(df['Category'].unique())
#st.write(df['Store'].unique())
