import aiy.voicehat
import glob
import random
import os


def main():

    files = glob.glob('sesame_street/*.mp3')
    max = len(files)

    button = aiy.voicehat.get_button()

    while True:
        print('ready')
        button.wait_for_press()
        selected = random.randint(0, max-1)
        selected_file = files[selected]
        os.system('mpg321 ' + selected_file)


if __name__ == '__main__':
    main()