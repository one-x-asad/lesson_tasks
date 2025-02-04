class Videokarta():
    def __init__(self,nomi,turi,pamyati,kuler_soni):
        self.nomi=nomi
        self.turi=turi
        self.pamyati=pamyati
        self.kuler_soni=kuler_soni
    
    def info(self):
        return self.nomi,self.turi,self.pamyati,self.kuler_soni
    
    def get_turi(self):
        return self.turi
    
a1=Videokarta("RX", 2000, "2GB", "2ta")
a2=Videokarta("RTX", 5090, "12GB", "3ta")

class NVIDIA(Videokarta):
    
    def get_nomi(self):
        return self.nomi
    
    def get_pamyati(self):
        return self.pamyati
    
    
a3=NVIDIA("RTX", 3050, "6GB", "3ta")
a4=NVIDIA("GTX", 1050, "4GB", "2ta")

print(a1.info())
print(a1.get_turi())

print(a2.info())
print(a2.get_turi())

print(a3.info())
print(a3.get_turi())
print(a3.get_nomi())
print(a3.get_pamyati())

print(a4.info())
print(a4.get_turi())
print(a4.get_nomi())
print(a4.get_pamyati())