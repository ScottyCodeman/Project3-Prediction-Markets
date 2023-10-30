import streamlit as st

github_link = "https://github.com/Narimanhx/Project3-Prediction-Markets"
st.title("frequently asked questions")

st.markdown("### How do I become a registered user?")
with st.expander("Answer"):
    st.markdown("#### Click the Registration tab and Choose your username, and password" )

st.markdown("### Is my password safe?")
with st.expander("Answer"):
    st.markdown("#### Yes, your password is hashed so no one will know what it is but you.")
    
st.markdown("### How do I update my user info?")
with st.expander("Answer"):
    st.markdown("#### There is a pop up sidebar that will have updates for your user information.")

st.markdown("### What kind of documentation do I need?")
with st.expander("Answer"):
    st.markdown("#### None!")

st.markdown("### What if I forget my private key?")
with st.expander("Answer"):
    st.markdown("#### You wont be able to recover any of your funds, we don't store your private key, keep it somewhere safe, offline and online.")

st.markdown("### Is there any minimum amount to bet")
with st.expander("Answer"):
    st.markdown("#### No,there is no minimum amount of Eth needed to bet")

st.markdown("### Can anyone start a game to bet on? ")
with st.expander("Answer"):
    st.markdown("#### Only the Admin's are able to create a game for betting.")
st.markdown("### Github")    
with st.expander("github link"):
    #st.markdown("[Github](https://github.com/Narimanhx/Project3-Prediction-Markets))
    st.write(github_link)

