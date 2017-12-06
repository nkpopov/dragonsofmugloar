#!/usr/bin/env python3

import requests
import json
import xml.etree.ElementTree as et
import characters as ch
import http_io

def get_knight():
    """ This function fetches the game. Namely it requests new game
    identifier and knight qualities from the server. It returns the
    tuple (int, characters.Knight). 
    """
    response = requests.get(http_io.get_game_url())
    response_dict = json.loads(response.text)

    print(response_dict['knight'])
    return response_dict['gameId'], ch.Knight(response_dict['knight'])

def get_weather(gameid):
    """ Fetch the weather report for the game. The function gets
    integer game identifier from arguments and returns string with
    weather description.

    Arguments:
      gameid: int. Game identifier
    """
    response = requests.get(http_io.get_weather_url(gameid))
    rootnode = et.fromstring(response.text)

    print(rootnode[3].text)
    return rootnode[3].text

def fight_battle(gameid, dragon):
    """ Start the battle by sending the dragon parameters to the
    server. This function implements the last step of the game. It
    returns True in case of victory and False otherwise.

    Arguments:
      gameid: int. Game identifier
      dragon: ch.Dragon. Dragon to fight knight
    """

    url      = http_io.get_solution_url(gameid)
    request  = json.dumps({'dragon': dragon.qualities})
    response = requests.put(url, data=request, headers=http_io.get_headers())
    result   = json.loads(response.text)

    print(response.text)
    return result['status' ] == 'Victory'
    



