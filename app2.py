import streamlit as st
from langchain import OpenAI, ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Initialize the OpenAI model
llm = OpenAI(model_name="text-davinci-003")

# Define a prompt template for the conversation
prompt_template = PromptTemplate(
    input_variables=["history", "input"],
    template="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\n{history}\nHuman: {input}\nAI:",
)

# Initialize the conversation chain with memory
conversation = ConversationChain(
    llm=llm,
    prompt=prompt_template,
    memory=ConversationBufferMemory()
)

# Streamlit frontend
st.title("Chat with Custom Database")

# Input box for user query
user_input = st.text_input("You: ")

# Display conversation history
if "history" not in st.session_state:
    st.session_state.history = ""

if user_input:
    # Generate response from the model
    response = conversation.predict(input=user_input)
    
    # Update conversation history
    st.session_state.history += f"Human: {user_input}\nAI: {response}\n"
    
    # Display the updated conversation
    st.write(st.session_state.history)
