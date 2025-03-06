# Homework: put all swim meets and cube solves from the excel sheets into the JSON

from CubeSolve import CubeSolve
from SwimTime import SwimTime
import json

savedata = json.load(open("savedata.json"))
ucberkeley = savedata["cube_solves"][1]

solve = CubeSolve()
solve.from_dict(ucberkeley)

print(solve.average())

# print("--- Gunn High ---")

# Gunnhigh = SwimTime()
# print(Gunnhigh.location)
# print(Gunnhigh.date)
# print(Gunnhigh.stroke)
# print(Gunnhigh.length)
# print(Gunnhigh.time)
# print(Gunnhigh.rank)
# print(Gunnhigh.note)