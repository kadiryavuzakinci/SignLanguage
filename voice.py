import pyttsx3
import threading

class SpeechThread(threading.Thread):
    def __init__(self, text):
        super().__init__()
        self.text = text
        self.tts = pyttsx3.init()
        self.daemon = True  # Allow the thread to be killed when the main thread exits

    def run(self):
        try:
            self.tts.say(self.text)
            self.tts.runAndWait()
            self.tts.stop()
        except Exception as e:
            print(f"An error occurred during speech synthesis: {e}")

class SpeechConverter:
    def __init__(self):
        self.last_spoken_sentence = None

    def convert_words_to_speech(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                if lines:
                    last_sentence = lines[-1].strip()  # Get the last line
                    
                    if last_sentence != self.last_spoken_sentence:  # Check if the last sentence is different from the last spoken sentence
                        speech_thread = SpeechThread(last_sentence)
                        speech_thread.start()
                        self.last_spoken_sentence = last_sentence  # Update the last spoken sentence
        except Exception as e:
            print(f"An error occurred while converting words to speech: {e}")
        
        return self.last_spoken_sentence
