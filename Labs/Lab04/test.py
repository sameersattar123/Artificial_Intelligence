from modules.VaccumAgent import VaccumAgent
from modules.TwoRoomVacuumCleanerEnvironment import TwoRoomVaccumCleanerEnvironment

vcagent = VaccumAgent()
env = TwoRoomVaccumCleanerEnvironment(vcagent) 
env.executeStep(50)

print(vcagent.score)