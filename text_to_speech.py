import streamlit as st
import os
import requests
from pyht import Client, TTSOptions, Format
from dotenv import load_dotenv, find_dotenv

# Load credentials from .env if running locally
load_dotenv(find_dotenv())

# Initialize PlayHT with your credentials
playht_user_id = st.secrets.get("PLAYHT_USER_ID") or os.getenv("PLAYHT_USER_ID")
playht_api_key = st.secrets.get("PLAYHT_API_KEY") or os.getenv("PLAYHT_API_KEY")
client = Client(playht_user_id, playht_api_key)

# Function to obtain voices from the PlayHT API
def get_voices():
    url = "https://api.play.ht/api/v2/voices"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {playht_api_key}",
        "X-User-ID": playht_user_id,
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Return the JSON response directly
    else:
        st.error(f"Failed to load voices. Status code: {response.status_code}")
        return []

# Get the list of voices
available_voices = get_voices()

# Create a sorted list of voice names with the accent in parentheses
voice_names = sorted(
    [f"{voice['name']} ({voice.get('accent', 'Not available')})" for voice in available_voices],
    key=lambda x: x.lower()  # Sort case insensitively
) if available_voices else []

st.title("Audio Generator with PlayHT")

text = st.text_area("Enter text:", height=200)
voice = st.selectbox("Select voice:", voice_names)

# Button to generate audio
if st.button("Generate audio"):
    if text:
        selected_voice_name = voice.split(" (")[0]
        selected_voice = next((v for v in available_voices if v['name'] == selected_voice_name), None)
        
        if selected_voice:
            voice_id = selected_voice['id']
            
            # Configure TTS options
            options = TTSOptions(
                voice=voice_id,
                sample_rate=44_100,
                format=Format.FORMAT_MP3,
                speed=1,
            )

            # Generate and save the audio
            audio_path = "audio.mp3"
            try:
                with open(audio_path, "wb") as output_file:
                    for chunk in client.tts(text=text, voice_engine="PlayHT2.0-turbo", options=options):
                        if chunk:
                            output_file.write(chunk)
                
                st.success(f"Audio generated and saved as {audio_path}")

                # Play the audio file
                audio_file = open(audio_path, "rb")
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format='audio/mp3')

                # Download button for the audio file
                st.download_button(
                    label="Download Audio",
                    data=audio_bytes,
                    file_name="audio.mp3",
                    mime="audio/mp3",
                    key="download_audio"
                )
            except Exception as e:
                st.error(f"An error occurred while generating audio: {e}")
        else:
            st.error("Could not select the voice.")
    else:
        st.error("Please enter some text.")
