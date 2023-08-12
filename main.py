from parser import InputParser
from player import Player

player = Player("Bob")

parser = InputParser()
while True:
    parser.await_input()