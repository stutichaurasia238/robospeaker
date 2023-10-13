import win32com.client as win

if __name__ == '__main__':
    print("welcome to RoboSpeaker 1.1. Created by Stuti")
    speaker = win.Dispatch("SAPI.SpVoice")
    while True:
        x=input("enter what you want me to speak :")
        if x=="q":
            speaker.speak("bye bye friend")
            break

        speaker.Speak(x)

