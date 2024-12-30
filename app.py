import streamlit as st
from infer import DocumentSearch

# Initialize the document search class
search_engine = DocumentSearch()

st.title("Document Search and Retrieval")

query = st.text_input("Enter your search query:")

if st.button("Search"):
    if query:
        results = search_engine.search(query)
        st.write("Top Matching Documents:")
        for idx, row in results.iterrows():
            st.write(f"**Title:** {row['title']} \n **Content:** {row['content']} \n **Score:** {row['score']:.2f}")
    else:
        st.error("Please enter a query.")