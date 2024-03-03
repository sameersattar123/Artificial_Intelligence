from Lab04.Agent import Agent

class VaccumAgent(Agent.Agent):
 def __init__(self): 
     pass
 def sense(self,env):
    self.environment = env
 def act(self): 
    if self.environment.currentRoom.status == 'dirty':
       return 'clean' 
    if self.environment.currentRoom.location == 'A': 
       return 'right' 
    else:
       return 'left'