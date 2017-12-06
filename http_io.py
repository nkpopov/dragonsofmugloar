#!/usr/bin/env python3

def get_game_url():
    """ URL for initiating the game round """
    return "http://www.dragonsofmugloar.com/api/game"

def get_solution_url(gameid):
    """ URL for sending solution (dragon) """
    return "http://www.dragonsofmugloar.com/api/game/" + \
        str(gameid) + "/solution"

def get_weather_url(gameid):
    """ URL for requesting weather for the corresponding battle """
    return "http://www.dragonsofmugloar.com/weather/api/report/" + \
        str(gameid)

def get_headers():
    """ Appropriate HTTP headers """
    return {'Content-type': 'application/json', 'Accept': 'text/plain'}


