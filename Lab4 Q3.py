import random
class Robot2:
    def __init__(self):
        self.saying = []

    def setSayings(self,saying):
        self.saying = saying
        
    def speak(self):
        print(random.choice(self.saying))

r1 = Robot2()      
u1 = ["Exterminate, Exterminate!", "I obey!","You cannot escape.", "Robots do not feel fear.","The Robots must survive!" ]          
r1.setSayings(u1)
print("Robot r1 says: ")
r1.speak()

print("Robot r2 says: ")     
r2 = Robot2()       
u2 = [ "I obey!" ]        
r2.setSayings(u2);        
r2.speak()  
