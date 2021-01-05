# REFERENCE
# 1. Python Speech Recognition Tutorial for Beginners(https://geekscoders.com/python-speech-recognition-tutorial-for-beginners/)
# 2. Python Speech Recognition | Speech To Text Converter | Google Speech(https://www.youtube.com/watch?v=GluSLXFGfJ8)
import speech_recognition as sr
# from selenium import webdriver

# chrome = webdriver.Chrome

def main():
  r =  sr.Recognizer()
  with sr.Microphone() as source:
    r. adjust_for_ambient_noise(source)
    print("Please say something")
    audio = r.listen(source)
    print("Recognizing Audio Now...")

    try:
      textedAudio = r.recognize_google(audio)
      print("You have said : " + textedAudio)
      print("Audio Recorded Successfully( " + textedAudio + " )\n" )
    except Exception as e:
      print("Error :  " + str(e))

    # write audio to wav file
    # with open("textedAudio.wav", "wb") as f:
      # f.write(audio.get_wav_data())


if __name__ == "__main__":
    main()