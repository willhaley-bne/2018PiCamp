from gtts import gTTS
import os
import netifaces as ni
import aiy.voicehat


def main():

    ni.ifaddresses('wlan0')
    ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
    language = 'en'

    if os.path.exists('startup/instructions.mp3') is False:
        obj = gTTS(text='Press the button for your ip address', lang=language, slow=False)
        obj.save('startup/instructions.mp3')

    if os.path.exists('startup/ip_address_is.mp3') is False:
        obj = gTTS(text='IP Address Is', lang=language, slow=False)
        obj.save('startup/ip_address_is.mp3')

    if os.path.exists('startup/ip_address.mp3') is False:
        obj = gTTS(text=ip, lang=language, slow=False)
        obj.save('startup/ip_address.mp3')

    button = aiy.voicehat.get_button()

    os.system("mpg321 startup/instructions.mp3")

    while True:
        button.wait_for_press()
        os.system("mpg321 startup/ip_address_is.mp3")
        os.system("mpg321 startup/ip_address.mp3")


if __name__ == '__main__':
    main()