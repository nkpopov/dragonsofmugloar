#!/usr/bin/env python3

import characters as ch
import battle
import pickle
import numpy as np
import itertools as it

def dragon_skills_list():
    """ Return list of all possible permutations for dragon's skills """
    return [(scale, claw, wing, fire) for scale in range(11) \
            for claw in range(11) for wing in range(11) \
            for fire in range(11) if (scale + claw + wing + fire) == 20]

def accumulate(fname, size=10):
    """ Accumulate dataset for models training. The dataset consist of
    tuples (str, ch.Knight, ch.Dragon, bool) that describe weather
    report, knight, dragon and battle outcome correspondingly. Note
    that dataset is accumulated by performing battles of all possible
    dragons with random knights @size times.
    
    Arguments:
      fname: str. Dataset file name
      size: int. Multiple of dataset size
    """
    dataset = []
    counter = 0
    skills  = dragon_skills_list()
    for (scale, claw, wing, fire), i in it.product(skills, range(size)):

        print("-- Game #%05d" % (counter))
        gameid, knight = battle.get_knight()
        weather = battle.get_weather(gameid)
        dragon = ch.Dragon(scale, claw, wing, fire)
        result = battle.fight_battle(gameid, dragon)
        dataset.append((weather, knight, dragon, result))
        print((knight.to_list(), dragon.to_list(), result))
        counter += 1

    pickle.dump(dataset, open(fname, "wb"))
            
def read(fname):
    """ Read dataset from the binary file. The function returns list
    of tuples (str, ch.Knight, ch.Dragon, bool). Each tuple describes
    weather report, knight, dragon and battle outcome correspondingly.

    Arguments:
      fname: str. Dataset file name
    """
    data = pickle.load(open(fname, "rb"))
    return data

if __name__ == '__main__':

    # Accumulate dataset
    fname = './dataset.bin'
    accumulate(fname, 12)

    # Read dataset from file
    # data = read(fname)
    # print(data)

