import speech_recognition as sr

# # For Printing names of microphones
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print(f"Microphone with index {index} available: {name}")

def main():
    r = sr.Recognizer()
    with sr.Microphone(device_index = 0) as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="en-in")
            print(f"user said:{text}")
        except Exception as e:
            print("Some Error occurred . Sorry")
if __name__ == "__main__":
    while 1:
        main()
