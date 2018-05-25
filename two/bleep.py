import aiy.assistant.grpc
import aiy.audio
import aiy.voicehat
import random
import os
from gtts import gTTS


def main():
    status_ui = aiy.voicehat.get_status_ui()
    status_ui.status('starting')

    assistant = aiy.assistant.grpc.get_assistant()
    button = aiy.voicehat.get_button()
    with aiy.audio.get_recorder():

        while True:

            status_ui.status('ready')
            print('ready')
            button.wait_for_press()
            status_ui.status('listening')
            print('listening')
            text, audio = assistant.recognize()
            if text:

                if text == 'goodbye':
                    status_ui.status('stopping')
                    print('Bye!')
                    break
                print(text)
                words = str(text).split(' ')
                count = len(words)
                replace_with_beep = random.randint(2, count-1)
                print(replace_with_beep)

                first = words[:replace_with_beep]
                last = words[replace_with_beep:]
                print(first, last)
                obj = gTTS(text=' '.join(first), lang="en", slow=False)
                obj.save('bleep/first.mp3')

                obj = gTTS(text=' '.join(last), lang="en", slow=False)
                obj.save('bleep/last.mp3')

                os.system("mpg321 bleep/first.mp3 && mpg321 bleep/beep.mp3 && mpg321 bleep/last.mp3")


if __name__ == '__main__':
    main()
