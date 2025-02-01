class Mishka():
    def __init__(self,rangi,firma,turi="sinsiz"):
        self.rangi=rangi
        self.firma=firma
        self.turi=turi
        
    def info(self):
        return self.rangi,self.firma,self.turi
    
a=Mishka("qora", "blood")

print(a.info())