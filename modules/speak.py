import asyncio
import edge_tts
import os
import subprocess

voice_male = "en-US-BrianMultilingualNeural"  # You can choose other voices
voice_female = "en-US-EmmaMultilingualNeural"

async def text_to_speech(text, voice=voice_male):
    """Generates speech from text and saves it to an audio file."""
    filename = "files/output.mp3"
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(filename)

async def play_audio():
    """Plays the generated audio file."""
    try:
        subprocess.run(["mpg123", "files/output.mp3"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        print("Error: mpg123 is not installed. Install it with 'sudo pacman -S mpg123'")

def text_to_speech_run(text):
    """Runs the text-to-speech conversion and plays the audio."""
    print(f"TTS: {text}")
    
    # Run TTS in the event loop
    asyncio.run(text_to_speech(text))

    # Play the generated audio
    asyncio.run(play_audio())
