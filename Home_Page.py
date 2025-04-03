import streamlit as st

st.title("Web Development Lab03")

st.header("CS 1301")
st.subheader("Team 52, Web Development - Section A")
st.subheader("Gustavo F. Scherrer, Gracelynn Xia")

st.write("""
Welcome to our Streamlit Web Development Lab03 app! You can navigate between the pages using the sidebar to the left. The following pages are:

1. **Home Page**: Provides an overview of our Hunger Games-themed app and what each page offers.
2. **Victors**: Explore a searchable database of past Hunger Games victors. Filter by district, weapon of choice, and survival status.
3. **Arena Battler**: Simulate battles between two tributes using their kill counts, injuries, and weapons.
4. **CapitolBot**: Chat with an AI bot trained on Hunger Games data to answer questions about Panem’s deadliest.

Happy Hunger Games and may the odd be ever in your favor!
""")

st.image("Images/hungergamesreaping.jpg", width=800)

