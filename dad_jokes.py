import aiy.voicehat
from gtts import gTTS
import requests
import os


def main():

    if os.path.exists('dad_jokes/instructions.mp3') is False:
        obj = gTTS(text="Press the button for a dad joke!", lang='en', slow=False)
        obj.save('dad_jokes/instructions.mp3')

    if os.path.exists('dad_jokes/thinking.mp3') is False:
        obj = gTTS(text="Let me see if I can think of one.", lang='en', slow=False)
        obj.save('dad_jokes/thinking.mp3')

    button = aiy.voicehat.get_button()
  #  os.system('mpg321 dad_jokes/instructions.mp3')

    while True:
     #   button.wait_for_press()
       # os.system('mpg321 dad_jokes/thinking.mp3')

        joke_package = requests.get('https://icanhazdadjoke.com/')
        text = joke_package.json
        pass

if __name__ == '__main__':
    main()