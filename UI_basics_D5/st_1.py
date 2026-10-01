import streamlit as st

st.set_page_config(page_title = "Streamlit Demo",page_icon="🤷‍♀️")
st.title("Streamlit Demo")
st.write("this is plain text")
st.markdown("This is **bold** , this is *italic*,this is :blue [coloured.]")
st.write("You can also include a divider.")
st.divider()
if st.button("Submit"):
    st.write("You clicked on submit!")
show_message = st.checkbox("Do you want an extra message?")   
if show_message:
    st.write("This is the message.Have a good day!") 

