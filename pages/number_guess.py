import streamlit as st
import random

def main():
    st.title("Number Guessing Game")

    st.write("I'm thinking of a number. Use the buttons to guess if it's odd or even.")

    computer_choice = random.randint(1, 10)
    is_even = computer_choice % 2 == 0


    st.write("Your Choice:")
    even_button = st.button("Even")
    odd_button = st.button("Odd")

    user_choice = None

    if even_button:
        user_choice = "Even"
    elif odd_button:
        user_choice = "Odd"

    if user_choice is not None:
        if (is_even and user_choice == "Even") or (not is_even and user_choice == "Odd"):
            st.write("You guessed correctly! 🎉")
            st.write(f"Computer's Number was: {computer_choice}")
        else:
            st.write("You guessed wrong! 😔")
            st.write(f"Computer's Number was: {computer_choice}")

if __name__ == "__main__":
    main()