import streamlit as st

books = [
  "Bilbo Begins",
  "1984",
  "Animal Farm",
  "Can't hurt me",
  "Fool"]

st.title("Library")
st.write("Check titles")

book = st.text_input("Book Title: ")

if st.button("Check Book"):
  if book.strip() = "":
  st.warning("Please enter a book!!!")
  elif book in books:
    st.success("I found one")
else:
st.error("Nowhere to be found")
