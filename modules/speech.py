import speech_recognition as sr

def recognize_speech():
    """Recognizes speech from the microphone using Google Speech Recognition API."""
    recognizer = sr.Recognizer()
    
    # Set up microphone
    with sr.Microphone(device_index=0) as source:
        print("Listening... (speak anytime)")
        
        # Adjust for background noise
        recognizer.adjust_for_ambient_noise(source)  
        
        while True:
            try:
                # Capture audio
                audio = recognizer.listen(source)
                
                print("Recognizing...")
                text = recognizer.recognize_google(audio, language="en-US")  # Speech recognition
                
                print(f"You said: {text}")  # Debugging output
                
                # Exit command
                if "shut down" in text.lower():
                    print("Process terminated.")
                    return None  # Exit function

                return text  # Return recognized speech

            except sr.UnknownValueError:
                print("Could not understand audio, please repeat.")
                continue  # Keep listening
            except sr.RequestError as e:
                print(f"Connection error: {e}")
                return None  # Exit on API error
