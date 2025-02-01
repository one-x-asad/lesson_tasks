class Ruchka():
    def __init__(self,brend,pasta):
        self.brend=brend
        self._pasta=pasta
        
    def get_info(self):
        return self.brend,self._pasta
    
alfa1=Ruchka("alfa","ko'k")


print(alfa1.get_info())