
# Audio Generator with PlayHT

This project utilizes Streamlit and PlayHT to convert text to audio. Users can enter text, select from various voices, and generate audio files which can be played and downloaded directly through the web application.

## Features

- Enter text to generate audio.
- Select from a variety of voices with different accents.
- Play generated audio directly in the browser.
- Download the generated audio file in MP3 format.

## Getting Started

To run this project locally, ensure you have the required packages installed. You can do this by using the `requirements.txt` file provided in the repository.

### Prerequisites

- Python 3.7 or higher
- Streamlit
- PlayHT API credentials

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd audio_generator
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your PlayHT credentials in Streamlit's secrets:

   Create a `secrets.toml` file in the `.streamlit` directory with the following format:

   ```toml
   [PLAYHT]
   USER_ID = "your_user_id"
   API_KEY = "your_api_key"
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Navigate to the app in your browser after running the above command. By default, it will be available at `http://localhost:8501`.
2. Enter the text you want to convert to audio.
3. Select a voice from the dropdown menu.
4. Click the "Generate audio" button to create your audio file.
5. The generated audio can be played and downloaded directly from the app.

## Live Demo

You can also try the live version of the application here: https://text-to-speech-svz9vpqchvmfyvpegkbmfv.streamlit.app/
