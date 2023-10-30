import streamlit as st
from UserManager import UserManager  # Import the UserManager class from the user_manager module
import time
from apscheduler.schedulers.background import BackgroundScheduler

# Initialize the user manager
user_manager = UserManager()
game_link = "prediction-markets.streamlit.app"

# Initialize the scheduler
scheduler = BackgroundScheduler()
scheduler.start()

# Schedule the update_chat_messages function to run every 5 seconds
scheduler.add_job(user_manager.update_chat_messages, 'interval', seconds=5)

# Place the login, register, and page selection on the sidebar
st.sidebar.title("User Authentication")

if "username" not in st.session_state:
    st.session_state.username = None

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    
if "messages" not in st.session_state:
    st.session_state.messages = []

# Streamlit page selection
state = st.sidebar.radio("Select a state", ["Register", "Login"])

if state == "Register":
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Register"):
        user_manager.register_user(username, password)

if state == "Login":
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if user_manager.login_user(username, password, st.session_state):
            st.session_state.authenticated = True
            # st.experimental_rerun()

# Render chat interface if user is authenticated
if st.session_state.authenticated:
    st.title("💬Chatroom💬")
    st.write(f"Welcome, {username} to the chatroom!")

    # Chatbox to leave messages
    message = st.text_input("Leave a message:")
    if st.button("Send"):
        user_manager.store_chat_message(username, message)

    # Display chat messages
    with st.container():
        chat_messages = user_manager.get_chat_messages()
        for chat_message in chat_messages:
            st.write(f"{chat_message['username']}: {chat_message['message']}")

    if user_manager.is_admin(username):
        if st.button("Clear Chat"):
            user_manager.clear_chat_messages()
            st.success("Chat messages cleared by admin.")
            
    # Check if the user is an admin and display the button to create a game
    if user_manager.is_admin(username):
        if st.button("Create Game"):
            st.toast("🚨ADMIN is creating a game🚨")
            time.sleep(3)
            st.toast("🚨ADMIN is creating a game🚨")
            time.sleep(3)
            st.session_state.messages.append({"role": "🤖", "content": f"Click [here]({game_link}) to join the game!"}) 
    if "admin_creating_game" in st.session_state and st.session_state.admin_creating_game:
        st.session_state.admin_creating_game = False  # Reset the flag
        st.session_state.messages.append({"role": "🤖", "content": f"Click [here]({game_link}) to join the game!"})

            
