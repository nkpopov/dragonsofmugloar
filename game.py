#!/usr/bin/env python3

import sys
import argparse
import naive_model
import battle

if __name__ == '__main__':

    # Parse command line arguments
    parser = argparse.ArgumentParser(sys.argv[0])
    group  = parser.add_argument_group('mandatory arguments')
    group.add_argument('--n_games', dest='n_games', action='store', \
        type=int, help='Amount of games to play')
    args = parser.parse_args()
    if args.n_games is None:
        parser.print_help()
        sys.exit(1)

    # Play the game specified amount of times and record
    # outcomes. The current implementation uses naive model that
    # always returns the same dragon. As one can notice this is pretty
    # bad strategy. You can replace the navie_model with better one.

    n_games = args.n_games
    results = [0] * n_games
    for i in range(n_games):
        print("-- Game #%03d" % (i))
        game_id, knight = battle.get_knight()
        weather = battle.get_weather(game_id)
        dragon = naive_model.get_dragon(knight, weather)

        print(dragon.qualities)
        results[i] = battle.fight_battle(game_id, dragon)

    # Evaluate model's performance 
    print("performance: %f" % (sum(results) / n_games))
    
    
