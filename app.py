import streamlit as st
import pandas as pd
from encryption import encrypt_message, decrypt_message
from emotion_model import detect_emotion

emotion_emoji = {
    "joy": "😊",
    "sadness": "😢",
    "anger": "😡",
    "fear": "😨",
    "surprise": "😲",
    "love": "❤️"
}
st.title("Emotion Cipher")

# encrypt section
st.header("Encrypt Message")

message = st.text_area("Enter message")

if st.button("Encrypt"):
    if message.strip() == "":
        st.warning("Please enter a message first")
    else:
        encrypted = encrypt_message(message)
        emotions = detect_emotion(message)

        st.success("Message encrypted successfully")

        st.write("Encrypted Text")
        st.code(encrypted)

        st.write("Emotion")

        for e, score in emotions:
            emoji = emotion_emoji.get(e.lower(), "")
            st.write(f"{emoji} {e} : {score}")

        emotion_data = pd.DataFrame(emotions, columns=["Emotion", "Score"])
        st.bar_chart(emotion_data.set_index("Emotion"))


# decrypt section
st.header("Decrypt Message")

encrypted_input = st.text_area("Paste encrypted text")

if st.button("Decrypt"):
    if encrypted_input.strip() == "":
        st.warning("Please paste an encrypted message first")
    else:
        try:
            decrypted = decrypt_message(encrypted_input)
            emotions = detect_emotion(decrypted)

            st.success("Message decrypted successfully")

            st.write("Original Message")
            st.write(decrypted)

            st.write("Emotion")

            for e, score in emotions:
                emoji = emotion_emoji.get(e.lower(), "")
                st.write(f"{emoji} {e} : {score}")

            emotion_data = pd.DataFrame(emotions, columns=["Emotion", "Score"])
            st.bar_chart(emotion_data.set_index("Emotion"))

        except:
            st.error("Invalid encrypted message")