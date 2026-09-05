import speech_recognition as sr

class MorkEars:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        
    def listen(self):
        """
        Listens to the microphone, adjusts for background noise, 
        and converts speech to text using Google's free API.
        """
        with sr.Microphone() as source:
            print("\n[Mork's Ears]: Calibration to background noise...")
            self.recognizer.adjust_for_ambient_noise(source,duration=1.0)
            print("[Mork's Ears]: Listening... Speak now.")
            try:
                audio_data = self.recognizer.listen(source,timeout=5,phrase_time_limit=10)
                print("[Mork's Ears]: Processing audio...")
                recognize_method = getattr(self.recognizer, "recognize_google")
                text = recognize_method(audio_data)
                print(f"[You said]: {text}")
                return text.lower()
            except sr.WaitTimeoutError:
                print("[Mork's Ears]: Listening timed out. No speech detected.")
                return ""
            except sr.UnknownValueError:
                print("[Mork's Ears]: Audio received, but could not understand what was said.")
                return ""
            except sr.RequestError as e:
                print(f"[Error]: Could not request results from speech service; {e}")
                return ""
            
if __name__ == "__main__":
    ears = MorkEars()
    while True:
        command = ears.listen()
        if command == "exit":
            print("Shutting down ears. ")
            break
                
            