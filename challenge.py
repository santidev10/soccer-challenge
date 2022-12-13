#!/usr/bin/env python3
import re

def initialize_standings(standings, match_array):
    for match in match_array:
        result = re.match(r"([A-Za-z ]+) (\d), ([a-zA-Z ]+) (\d)", match)
        team1 = result.group(1)
        team2 = result.group(3)
        if team1 not in standings:
            standings[team1] = 0
        if team2 not in standings:
            standings[team2] = 0

def update_standings(team1, score1, team2, score2, standings):
        if score1 > score2:
                standings[team1] += 3
        elif score1 < score2:
            standings[team2] += 3
        else:
            standings[team1] += 1
            standings[team2] += 1     

def print_standings(standings):
    ordered_standings = dict(sorted(standings.items(), key=lambda item: item[1], reverse=True))
    idx = 1
    for line in ordered_standings.items():
        formatted_line = f"{idx}. {line[0]}, {line[1]} pts"
        idx += 1
        print(formatted_line)
# 
def main():
    standings = {}
    with open('sample-input.txt', 'r') as f:
        match_array = [line.strip() for line in f.readlines()]
        initialize_standings(standings, match_array)
        for match in match_array:
            result = re.match(r"([A-Za-z ]+) (\d), ([a-zA-Z ]+) (\d)", match)
            update_standings(result.group(1), int(result.group(2)), result.group(3), int(result.group(4)), standings)
    print_standings(standings)


if  __name__ == "__main__":
    main()