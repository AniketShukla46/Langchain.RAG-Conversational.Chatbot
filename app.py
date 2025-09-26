import streamlit as st
from langchain_core.messages import AIMessage
from langchain.schema import HumanMessage

from my_rag_pipeline import conversational_qa_chain, store  

# -------------------------------
# Streamlit Chatbot UI
# -------------------------------

st.set_page_config(page_title="LionO Chatbot")
st.title("LionO Chatbot")

# Initialize session state for chat history
if "session_id" not in st.session_state:
    st.session_state["session_id"] = "chat1"

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display past chat messages
for msg in st.session_state["messages"]:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

# Chat input for user
if query := st.chat_input("Type your question here..."):
    # Save user query
    st.session_state["messages"].append(HumanMessage(content=query))
    with st.chat_message("user"):
        st.markdown(query)

    # Get response from RAG chain
    response = conversational_qa_chain.invoke(
        {"query": query},
        config={"configurable": {"session_id": st.session_state["session_id"]}},
    )

    # Extract answer
    answer = response["result"]

    # Save and display AI response
    st.session_state["messages"].append(AIMessage(content=answer))
    with st.chat_message("assistant"):
        st.markdown(answer)
