#!/usr/bin/env python3
from console import *
import json
import time 
import random
import configparser
import argparse 

config = configparser.ConfigParser()
config.read("config.ini")
background = config.get('SETTINGS', 'background')
coin_type = config.get('SETTINGS', 'coin')
num_flips = config.get('SETTINGS', 'flips')

with open("assets.json") as f:
    assets = json.load(f)

def coin_flip(coin=coin_type, flips=int(num_flips), bg=background):
    # Can't figure out how to support this
    # bg_types = {'light' : 0, 'dark' : 1}
    coin_sides = {0 : 'head', 1 : 'tail'}


    flip = 0

    clear_screen()
    hide_cursor()
    while flip < flips:

        for a in range(0,360,15):
            side_coin_ascii = assets[coin]['side'][str(a)]
            print(side_coin_ascii)
            time.sleep(.1)
            clear_screen()

        clear_screen()
        time.sleep(.1)

        flip += 1 

    result = random.randint(0,1)
    face = coin_sides[result]
    face_coin_ascii = assets[coin][face]

    print(face_coin_ascii)
    print(face.upper() + 'S!')
    show_cursor()

def Main():
    parser = argparse.ArgumentParser(description="Flips a coin of a specified\
    type") 

    # Defaults are determined based on config.ini
    parser.add_argument("-b", "--bg", default=background, help="Defines\
            if the ascii will be dark or light")

    parser.add_argument("-c", "--coin", default=coin_type, help="Defines what\
    type of coin will be flipped")

    parser.add_argument("-f", "--flips", default=num_flips, help="Defines how many\
    times the coin will rotate 360 degrees before displaying the face;\
    if flips is zero it will only display the result of the flip")

    args = parser.parse_args()

    args_dict = vars(args)
    args_dict['flips'] = int(args_dict['flips'])

    coin_flip(**args_dict)


if __name__ == "__main__":
    Main()
