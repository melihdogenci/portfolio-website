import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# Import custom fonts and CSS for the title and text box
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;700&display=swap');
    .custom-font {
        font-family: 'Montserrat', sans-serif;
        font-size: 20px;
        line-height: 1.6;
        color: #3e1f7f; /* Dark purple for text */
        text-indent: 20px; /* Indent the first line of each paragraph */
    }
    .purple-text-box {
        background-color: #e0b3ff; /* Lighter purple background */
        border: 2px solid #d3a9f5; /* Purple border */
        border-radius: 8px;
        padding: 15px;
        margin: 8px 0;
    }
    .custom-title {
        font-family: 'Montserrat', sans-serif;
        color: #3e1f7f; /* Dark purple text */
        font-size: 36px; /* Adjust font size for the title */
        margin-bottom: 20px; /* Add margin below the title */
        padding: 10px 20px; /* Padding inside the title box */
        border: 4px solid #3e1f7f; /* Dark purple border */
        border-radius: 8px; /* Rounded corners for the border */
        background-color: #e0b3ff; /* Light purple background inside the border */
        display: inline-block; /* Ensure the border wraps tightly around the title */
    }
    .resizable-col {
        transition: flex 0.3s ease-in-out; /* Smooth transition for resizing */
    }
    .grow {
        flex: 1;
    }
    .shrink {
        flex: 0.5;
    }
    </style>
    """, unsafe_allow_html=True)

# Layout for the image and text
col1, col2 = st.columns([1, 1])

with col1:
    st.image("images/Image.png")

with col2:
    st.markdown('<h1 class="custom-title">Melih Döğenci</h1>', unsafe_allow_html=True)
    content = """
    <div class="purple-text-box">
        <p class="custom-font">
        A passionate Psychology student at Boğaziçi University, I've cultivated a strong academic foundation and a deep interest in technology. My technical proficiency extends to Python programming, where I excel in Object-Oriented Programming, SQL, NumPy, and Pandas.
        </p>
        <p class="custom-font">
        I've applied these skills to practical projects, which can be found on this page, demonstrating my ability to translate theoretical knowledge into tangible outcomes. My enthusiasm for data science and machine learning has led me to explore data analysis and predictive modeling, where I find great satisfaction in uncovering insights and patterns.
        </p>
        <p class="custom-font">
        I am eager to apply my technical skills and psychological knowledge to interdisciplinary research and projects.
        </p>
    </div>
    """
    st.markdown(content, unsafe_allow_html=True)

# Read the data from CSV
df = pd.read_csv("data.csv", sep=";")

# Display content in two columns
for i in range(len(df) // 2):
    with st.container():
        cols = st.columns([1.5, 0.3, 1.5])
        with cols[0]:
            st.header(df.iloc[i]["title"])
            st.markdown(df.iloc[i]["description"], unsafe_allow_html=True)
            st.image("images/" + df.iloc[i]["image"])
            st.write(f"[Source Code]({df.iloc[i]['url']})")

        with cols[2]:
            if i + len(df) // 2 < len(df):
                st.header(df.iloc[i + len(df) // 2]["title"])
                st.markdown(df.iloc[i + len(df) // 2]["description"], unsafe_allow_html=True)
                st.image("images/" + df.iloc[i + len(df) // 2]["image"])
                st.write(f"[Source Code]({df.iloc[i + len(df) // 2]['url']})")








