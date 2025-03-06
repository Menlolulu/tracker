from CubeSolve import CubeSolve
from SwimTime import SwimTime
ucberkeley = CubeSolve()

print("--- UC Berkeley --")

print(ucberkeley.event)
print(ucberkeley.average())
print(ucberkeley.location)

print("--- Crystal Springs ---")

crystalsprings = CubeSolve()

crystalsprings.event = "3x3x3"
crystalsprings.location = "Crystal Springs"

print(crystalsprings.event)
print(crystalsprings.best())
print(crystalsprings.location)

print("--- Gunn High ---")

Gunnhigh = SwimTime()
print(Gunnhigh.location)
print(Gunnhigh.date)
print(Gunnhigh.stroke)
print(Gunnhigh.length)
print(Gunnhigh.time)
print(Gunnhigh.rank)
print(Gunnhigh.note)