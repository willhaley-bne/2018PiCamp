import aiy.assistant.grpc
import aiy.audio
import aiy.voicehat
import alsaaudio
import os
import time
from gtts import gTTS


def main():
    m = alsaaudio.Mixer()

    status_ui = aiy.voicehat.get_status_ui()
    status_ui.status('starting')

    assistant = aiy.assistant.grpc.get_assistant()
    
    button = aiy.voicehat.get_button()

    if os.path.exists('translator/instructions.mp3') is False:
        obj = gTTS(
            text="I can translate any short english phrase into any other language.  Press the button to start.",
            lang='en',
            slow=False
        )
        obj.save('translator/instructions.mp3')

    if os.path.exists('translator/language.mp3') is False:
        obj = gTTS(
            text="What language do you want something translated into?",
            lang='en',
            slow=False
        )
        obj.save('translator/language.mp3')

    if os.path.exists('translator/phrase.mp3') is False:
        obj = gTTS(
            text="What is the short phrase?",
            lang='en',
            slow=False
        )
        obj.save('translator/phrase.mp3')
    print('instructions')
    os.system('mpg321 translator/instructions.mp3')

    with aiy.audio.get_recorder():
    
        while True:

            current_volume = m.getvolume()  # Get the current Volume

            status_ui.status('ready')
            button.wait_for_press()

            print('what language')
            os.system('mpg321 translator/language.mp3')
            time.sleep(2)
            os.system('mpg321 translator/phrase.mp3')
            status_ui.status('listening')
            print('what phrase')
            text, audio = assistant.recognize()
            print('returned with text: %s' % text)
            if text:
                if text == 'goodbye':
                    status_ui.status('stopping')
                    print('Bye!')
                    break

                words = str(text).split(' ')
                rendered_words = []

                for word in words:
                    file = 'translator/output/%s.mp3' % word
                    rendered_words.append(file)
                    print(file)
                    obj = gTTS(text='%s' % word, lang='en', slow=True)
                    obj.save(file)

                m.setvolume(95)

                for rendered in rendered_words:
                    print(rendered)
                    os.system('mpg321 %s' % rendered)
                    os.remove(rendered)

                m.setvolume(current_volume[0])


if __name__ == '__main__':
    main()
