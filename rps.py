import streamlit as st
import random

def main():
    st.title("Rock, Paper, Scissors Game")

    st.write("Let's play Rock, Paper, Scissors!")

    user_choice = st.radio("Choose your move:", ("Rock", "Paper", "Scissors"))

    computer_moves = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(computer_moves)

    st.write(f"You chose: {user_choice}")
    st.write(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)

    if result == "Win":
        st.success("You win!")
    elif result == "Lose":
        st.error("You lose!")
    else:
        st.info("It's a tie!")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    if (user_choice == "Rock" and computer_choice == "Scissors") or (user_choice == "Paper" and computer_choice == "Rock") or (user_choice == "Scissors" and computer_choice == "Paper"):
        return "Win"
    return "Lose"

if __name__ == "__main__":
    main()
