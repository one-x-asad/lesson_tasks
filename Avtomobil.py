class Avtomibil():
    def __init__(self,rangi,modeli,yili,yurgan_km="0"):
        self.rangi=rangi
        self.modeli=modeli
        self._yili=yili
        self.yurgan_km=yurgan_km
        
    def get_info(self):
        return self.rangi,self.modeli,self._yili,self.yurgan_km
    
    def get_rangi(self):
        return self.rangi
    
    def get_modeli(self):
        return self.modeli
    
a=Avtomibil("qora", "chevrolet", "2020", 10)

print(a.get_modeli())
print(a.get_info())
print(a.get_rangi())
