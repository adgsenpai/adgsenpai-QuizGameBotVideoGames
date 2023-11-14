
import streamlit as st

import g4f

st.title("🎮 Gaming Quiz Bot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Welcome to the Gaming Quiz Bot!"}
    ]

    st.write(
        '- This is quiz to humans about videos games. The bot will ask you questions about video games and you will have to answer them. \n'
        '- Type `start` to start the quiz'
    )

    st.write(
        '- Write `help` to see a list of commands'
    )

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})

    if prompt == 'help':
        st.write(
            """
            - Start the quiz by writing `start`                        
            """
        )
    else:
        st.chat_message("user").write(prompt)

        # get last 5 messages
        lastMessages = st.session_state.messages[-3:]

        if len(lastMessages) == 0:
            lastMessages = [{"role": "user", "content": " "}]


        # Set with provider
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",            
            messages=[
                {'role': 'system', 'content': 'You are a video game quiz bot. You are trying to quiz humans about video games.'},
                {'role': 'system', 'content': 'When the user types start you will ask them a question about video games. The user will then answer the question. You will then tell them if they are correct or not and explain why they are correct give another question. If the user unsure about the question then explain the answer and give them the answer.'},                
            ] + lastMessages + [{"role": "user", "content": prompt}]
        )
        st.session_state.messages.append(
            {"role": "assistant", "content": response})

        st.chat_message("assistant").write(response)
 
