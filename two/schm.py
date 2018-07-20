import aiy.assistant.grpc
import aiy.audio
import aiy.voicehat
import os
from gtts import gTTS


def first_vowel(s):
    for index, char in enumerate(s):
        if char in 'aeiou':
            return index


def main():
    status_ui = aiy.voicehat.get_status_ui()
    status_ui.status('starting')
    assistant = aiy.assistant.grpc.get_assistant()
    button = aiy.voicehat.get_button()
    with aiy.audio.get_recorder():
        while True:
            status_ui.status('ready')
            print('Press the button and speak')
            button.wait_for_press()
            status_ui.status('listening')
            print('Listening...')
            text, audio = assistant.recognize()
            if text:
                if text == 'goodbye':
                    status_ui.status('stopping')
                    print('Bye!')
                    break
                index = first_vowel(text)
                new_text = '%s%s' % ('schm', text[index:])
                obj = gTTS(text='%s, %s' % (text, new_text), lang='en', slow=False)
                obj.save('schm/output.mp3')

                os.system('mpg321 schm/output.mp3')


if __name__ == '__main__':
    main()