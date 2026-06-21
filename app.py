import streamlit as st
import pandas as pd
import pickle

# ----------------------------------
# Page Configuration
# ----------------------------------

st.set_page_config(
    page_title="Fashion Recommendation System",
    page_icon="🛍️",
    layout="wide"
)

# ----------------------------------
# Load Data
# ----------------------------------

@st.cache_data
def load_articles():
    with open("models/articles.pkl", "rb") as f:
        articles = pickle.load(f)
    return articles


@st.cache_data
def load_similarity():
    with open("models/top_similar.pkl", "rb") as f:
        top_similar = pickle.load(f)
    return top_similar


articles = load_articles()
top_similar = load_similarity()

# ----------------------------------
# Recommendation Function
# ----------------------------------

def recommend_products(article_id, top_n=5):

    if article_id not in top_similar:
        return []

    return top_similar[article_id][:top_n]


# ----------------------------------
# Sidebar
# ----------------------------------

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "Home",
        "Product Explorer",
        "Recommendation Engine"
    ]
)

# ----------------------------------
# HOME PAGE
# ----------------------------------

if page == "Home":

    st.title("🛍️ Fashion Recommendation System")

    st.markdown("---")

    st.markdown("""
    ## Project Overview

    This project recommends fashion products using
    Item-Based Collaborative Filtering.

    ### Technologies Used

    - Python
    - Pandas
    - Scikit-Learn
    - Streamlit

    ### Features

    - Product Explorer
    - Recommendation Engine
    - Similar Product Discovery

    ### Recommendation Technique

    - Customer Product Matrix
    - Cosine Similarity
    - Item-Based Collaborative Filtering
    """)

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Total Products",
            f"{articles['article_id'].nunique():,}"
        )

    with col2:
        st.metric(
            "Unique Product Names",
            f"{articles['prod_name'].nunique():,}"
        )

# ----------------------------------
# PRODUCT EXPLORER
# ----------------------------------

elif page == "Product Explorer":

    st.title("📦 Product Explorer")

    product_name = st.selectbox(
        "Select Product",
        sorted(articles["prod_name"].dropna().unique())
    )

    product = articles[
        articles["prod_name"] == product_name
    ].iloc[0]

    st.subheader("Product Information")

    st.write(
        {
            "Article ID": product["article_id"],
            "Product Name": product["prod_name"],
            "Product Type": product["product_type_name"],
            "Color": product["colour_group_name"],
            "Department": product["department_name"],
        }
    )

# ----------------------------------
# RECOMMENDATION ENGINE
# ----------------------------------

elif page == "Recommendation Engine":

    st.title("🤖 Recommendation Engine")

    product_name = st.selectbox(
        "Choose a Product",
        sorted(articles["prod_name"].dropna().unique())
    )

    selected_product = articles[
        articles["prod_name"] == product_name
    ].iloc[0]

    article_id = selected_product["article_id"]

    st.markdown("### Selected Product")

    st.write(
        {
            "Product Name": selected_product["prod_name"],
            "Type": selected_product["product_type_name"],
            "Color": selected_product["colour_group_name"],
            "Department": selected_product["department_name"],
        }
    )

    if st.button("Get Recommendations"):

        recommendations = recommend_products(
            article_id,
            top_n=5
        )

        if len(recommendations) == 0:

            st.error(
                "No recommendations available for this product."
            )

        else:

            st.success("Recommendations Generated!")

            rec_df = articles[
                articles["article_id"]
                .isin(recommendations)
            ][
                [
                    "prod_name",
                    "product_type_name",
                    "colour_group_name",
                    "department_name"
                ]
            ]

            st.subheader("Recommended Products")

            st.dataframe(
                rec_df,
                use_container_width=True
            )