import streamlit as st
import pandas as pd

st.set_page_config(layout = 'wide')
df = pd.read_excel("./pages/Source.xlsx")

s,c,p,pr = st.columns(4)
with s:
    selection_store = st.multiselect("Select store", 
                                     options=df['Store'].unique(),
                                    default=df['Store'].unique())

    df = df[df['Store'].isin(selection_store)]

with c:
    selection_category = st.multiselect("Select food category",
                                        options=df['Category'].unique(),
                                       default=df['Category'].unique())

    df = df[df['Category'].isin(selection_category)]

with p:
    selection_product = st.multiselect("Select Product Name", 
                                       options=df['Product_Name'].unique(),
                                      default=df['Product_Name'].unique())

    df = df[df['Product_Name'].isin(selection_product)]

with pr:
    lowest_price = (df['Price'].min())
    highest_price = (df['Price'].max())
    selection_price = st.slider("Price Range", min_value = lowest_price, max_value = highest_price)

num_of_columns = st.number_input("How many columns:",value = 4,step=1) # create variable to set the column
columns = st.columns(num_of_columns) # create the column
data_length = len(df)
#num_of_rows = int(data_length / num_of_columns)

for i in range(data_length):
    for r in range(num_of_columns):
        if i%num_of_columns == r:
            col = columns[r]
            
            with col:
                with st.container(border=True):
                    record = df.iloc[i]
                    st.image(f'{record['Picture']}',width=250)
                    st.write(f'{record['Product_Name']}')
                    st.write(f'{record['Price']}')
                    st.write(f'{record['Description']}')
                    if st.button("Add to Cart",key=f'{i}'):
                        st.write("Added to Cart")
                    if st.button("Buy",key=f'buy{i}'):
                        st.write("Thank You :D")

# st.dataframe(df)
