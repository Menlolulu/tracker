# Homework: put all swim meets and cube solves from the excel sheets into the JSON

from CubeSolve import CubeSolve
from SwimTime import SwimTime
import json

def create_cube_solve():
    date = input("What is the date of the solve? ")
    location = input("What is the location")
    event = input("What is the event")
    round = int(input("What is the round"))
    rank = int(input("What is the rank"))
    time1 = float(input("What was the first time?"))
    time2 = float(input("What was the second time?"))
    time3 = float(input("What was the third time?"))
    time4 = float(input("What was the fourth time?"))
    time5 = float(input("What was the fifth time?"))
    times = [time1, time2, time3, time4, time5]

    solve = CubeSolve()
    solve.date = date
    solve.location = location
    solve.event = event
    solve.round = round
    solve.rank = rank
    solve.solves = times

    return solve

savedata = json.load(open("savedata.json"))
ucberkeley = savedata["cube_solves"][1]

solve = CubeSolve()
solve.from_dict(ucberkeley)

print(solve)

# print("--- Gunn High ---")

# Gunnhigh = SwimTime() 
# print(Gunnhigh.location)
# print(Gunnhigh.date)
# print(Gunnhigh.stroke)
# print(Gunnhigh.length)
# print(Gunnhigh.time)
# print(Gunnhigh.rank)
# print(Gunnhigh.note)