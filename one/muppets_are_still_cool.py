import aiy.voicehat
import glob
import random
import os


def main():
    # Gets a list of files from the muppets folder
    files = glob.glob('muppets/*.mp3')

    # files will now be a list of mp3's
    # sort of like...
    # (one.mp3, two.mp3, three.mp3, four.mp3, five.mp3)
    # each item on the list has a position starting at Zero.
    # one.mp3 -> position 0
    # two.mp3 -> position 1
    # three.mp3 -> position 2
    # and so on, this will be important later

    # Gets number of files in the list
    max = len(files)

    # creates an object that will allow us to know information about the box's button
    button = aiy.voicehat.get_button()

    # will repeat the indented forever.  Well at least until we kill the script (ctrl+c)
    while True:

        # outputs the word "ready" to the screen
        print('ready')

        # will pause the script until the button is pushed
        button.wait_for_press()

        # will select a random number between 0 and 19 ( 20 files minus 1 b/c we start at position Zero)
        random_number = random.randint(0, max-1)

        # we use that random number to select one of the mp3's in the list
        # selected_file = 'muppets/-------.mp3'
        selected_file = files[random_number]

        # mpg321 %s % selected_file = mpg321 muppets/--------.mp3
        # this tells the device to use the mpg321 program to play the mp3
        os.system('mpg321 %s' % selected_file)


if __name__ == '__main__':
    main()
