# Homework: put all swim meets and cube solves from the excel sheets into the JSON

from CubeSolve import CubeSolve
from SwimTime import SwimTime
import json

# def create_cube_solve():
#     date = input("What is the date of the solve? ")
#     location = input("What is the location? ")
#     event = input("What is the event? ")
#     round = int(input("What is the round? "))
#     rank = int(input("What is the rank? "))
#     time1 = float(input("What was the first time? "))
#     time2 = float(input("What was the second time? "))
#     time3 = float(input("What was the third time? "))
#     time4 = float(input("What was the fourth time? "))
#     time5 = float(input("What was the fifth time? "))
#     times = [time1, time2, time3, time4, time5]


#     solve = CubeSolve()
#     solve.date = date
#     solve.location = location
#     solve.event = event
#     solve.round = round
#     solve.rank = rank
#     solve.solves = times

#     return solve

# savedata = json.load(open("savedata.json"))

# solve = create_cube_solve()
# savedata["cube_solves"].append(
#     json.loads(solve.to_json())
# )
# json.dump(savedata, open("savedata.json", "w"))


def create_swim_time():
    date = input(" What is the date of the swim meet? ")
    location = input(" What is the location of the meet ")
    stroke = input(" What is the stroke? ")
    length = input(" what is the length of the event")
    time = input(" What is the time it took for you to finishe ")
    rank = input(" What is the rank of the event")
    note = input(" What notes or idea you have about the event")

    swim_time = SwimTime 
    swim_time.date = date
    swim_time.location = location
    swim_time.stroke = stroke 
    swim_time.length = length
    swim_time.time = time
    swim_time.rank = rank
    swim_time.note = note

    return swim_time

solve = create_swim_time()


# print("--- Gunn High ---")

# Gunnhigh = SwimTime() 
# print(Gunnhigh.location)
# print(Gunnhigh.date)
# print(Gunnhigh.stroke)
# print(Gunnhigh.length)
# print(Gunnhigh.time)
# print(Gunnhigh.rank)
# print(Gunnhigh.note)