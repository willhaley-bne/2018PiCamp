from gtts import gTTS
import aiy.voicehat
import os


def main():

    if os.path.exists('press_button/instructions.mp3') is False:
        obj = gTTS(text='I bet you cannot press the button', lang='en', slow=False)
        obj.save('press_button/instructions.mp3')

    if os.path.exists('press_button/repeat.mp3') is False:
        obj = gTTS(text='Well, I bet you cannot press it again', lang='en', slow=False)
        obj.save('press_button/repeat.mp3')

    if os.path.exists('press_button/give_up.mp3') is False:
        obj = gTTS(text='OK! OK!  I get it. You can push the button. Jeez.', lang='en', slow=False)
        obj.save('press_button/give_up.mp3')

    button = aiy.voicehat.get_button()
    os.system('mpg321 press_button/instructions.mp3')
    n = 0

    while True:
        button.wait_for_press()
        if n > 2:
            os.system('mpg321 press_button/give_up.mp3')
        else:
            os.system('mpg321 press_button/repeat.mp3')

        n = n+1


if __name__ == '__main__':
    main()
