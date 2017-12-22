#!/usr/bin/env python3
import sys
import os 
import time 
import random
import configparser
import sqlite3
import argparse 


workdir = os.path.abspath('assets')
database_path = os.path.join(workdir, 'coins.db')
conn = sqlite3.connect(database_path)
cur = conn.cursor()

config = configparser.ConfigParser()
config.read('config.ini')

background = config.get('SETTINGS', 'background')
coin_type = config.get('SETTINGS', 'coin')
num_flips = config.get('SETTINGS', 'flips')


# wrapper over os.system('clear'/'cls')
def clear_screen():

    if sys.platform == "win32":
        os.system('cls')

    else:
        os.system('clear')

def coin_flip(coin=coin_type, flips=num_flips, bg=background):
    bg_types = {'light' : 0, 'dark' : 1}
    coin_sides = {0 : 'head', 1 : 'tail'}

    os.system('setterm -cursor off')

    flip = 0

    while flip < flips:

        for a in range(0,360,15):
            side_coin_ascii = cur.execute('''SELECT light_coin_ascii, dark_coin_ascii FROM coin_side\
            WHERE coin_type=? AND angle=?''',\
            (coin, a)).fetchone()[bg_types[bg]]

            print(side_coin_ascii)
            time.sleep(.2)
            clear_screen()

        clear_screen()
        time.sleep(.2)

        flip += 1 

    result = random.randint(0,1)
    face_coin_ascii = cur.execute('''SELECT light_coin_ascii, dark_coin_ascii FROM coin_face\
            WHERE coin_type=? AND face=?''',\
            (coin, coin_sides[result])).fetchone()[bg_types[bg]]

    print(face_coin_ascii)
    print(coin_sides[result].upper() + 'S' + '!')

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
