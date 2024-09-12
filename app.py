import streamlit as st

# Title of the app
st.title("Task Selector App")

# Buttons for selecting tasks
task = st.selectbox("Choose a task", ["Select a task", "Sentiment Analysis", "Chat with Database"])

# Function to display the input chat box and submit button
def display_task_page(task_name):
    st.header(f"{task_name} Page")
    user_input = st.text_input("Enter your text here:")
    if st.button("Submit"):
        st.write(f"You entered: {user_input}")

# Display the appropriate page based on the selected task
if task == "Sentiment Analysis":
    display_task_page("Sentiment Analysis")
elif task == "Chat with Database":
    display_task_page("Chat with Database")
else:
    st.write("Please select a task from the dropdown above.")
