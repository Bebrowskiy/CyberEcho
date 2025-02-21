from modules.speak import text_to_speech_run  # Converts text to speech
from modules.speech import recognize_speech  # Recognizes speech input
from modules.ai_interface import ai_response, process_special_commands  # AI response processing

while True:
    # Capture user's voice input
    prompt = recognize_speech()
    print(prompt)  # Display recognized text in the console

    # Generate AI response based on the recognized speech
    resp = ai_response(prompt)
    print(resp)
    # Process special commands (if any) within the AI's response
    response, system_response = process_special_commands(resp)

    # Convert AI response to speech
    text_to_speech_run(response)

    # Continue listening for the next input
    continue

    # If there is a system-related response, process it separately
    if system_response:
        text_to_speech_run(ai_response(system_response))
        continue
    