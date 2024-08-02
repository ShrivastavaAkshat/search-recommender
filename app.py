import streamlit as st
import pandas as pd
import numpy as np 
import pickle
from PIL import Image
import requests
from io import BytesIO


similarity = pickle.load(open('similarity.pkl', 'rb'))
electronics = pickle.load(open('data.pkl', 'rb'))

def recommender(product):
    product_index = electronics[electronics['name'] == product].index[0]
    similarity_list = list(enumerate(similarity[product_index]))
    top_10_similar_product = sorted(similarity_list, key=lambda x: x[1], reverse=True)[1:11]
    
    similar_products = []
    for product_index, similarity_score in top_10_similar_product:
        product_info = {
            'name': electronics.loc[product_index]['name'],
            'image': electronics.loc[product_index]['image']
        }
        similar_products.append(product_info)
    return similar_products

def is_image_loaded(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False

st.title('Similar Electronic Product Finder ')


product_name = st.sidebar.selectbox('Select a product:', electronics['name'])

if st.sidebar.button('Search'):
    recommendations = recommender(product_name)
    st.write(f"Top recommendations for {product_name}:")

    valid_recommendations = [rec for rec in recommendations if is_image_loaded(rec['image'])]

    num_recommendations = len(valid_recommendations)
    num_rows = (num_recommendations + 1) // 2  

    for row in range(num_rows):
        cols = st.columns(2)  
        start_index = row * 2
        end_index = min(start_index + 2, num_recommendations) 

        for idx in range(start_index, end_index):
            with cols[idx - start_index]:
                st.image(valid_recommendations[idx]['image'], width=150)
                st.write(f"**{valid_recommendations[idx]['name']}**")