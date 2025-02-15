class Telefon():
    def __init__(self,rang,kattaligi,uzunligi,nomi,pamyati):
        self.rang=rang
        self.kattaligi=kattaligi
        self.uzunligi=uzunligi
        self.nomi=nomi
        self.pamyati=pamyati
    
    def info(self):
        return self.rang,self.kattaligi,self.uzunligi,self.nomi,self.pamyati
     
    def get_rang(self):
        return self.rang
    
    def get_kattaligi(self):
        return self.kattaligi
    
    def get_uzunligi(self):
        return self.uzunligi
    
a1=Telefon("oq", "10SM", "10SM", "nophone1", "64GB")
a2=Telefon("qora", "15SM", "15SM", "nophone2", "128GB")
a3=Telefon("qizil", "20SM", "20SM", "nophone3", "256GB")
a4=Telefon("ko'k", "25SM", "25SM", "nophone4", "512GB")

print(a1.info())
print(a2.info())
print(a3.info())
print(a4.info())

class Product():
    def __init__(self,rang,kattaligi,uzunligi,nomi,chiqarilgan,tami,vazni,sifati):
        self.rang=rang
        self.kattaligi=kattaligi
        self.uzunligi=uzunligi
        self.nomi=nomi
        self.chiqarilgan=chiqarilgan
        self.tami=tami
        self.vazni=vazni
        self.sifati=sifati
        
    def info(self):
        return self.rang,self.kattaligi,self.uzunligi,self.nomi,self.chiqarilgan,self.tami,self.vazni,self.sifati
     
    def get_rang(self):
        return self.rang
    
    def get_kattaligi(self):
        return self.kattaligi
    
b1=Product("sariq", "7sm", "2sm", "banan", "15fevral", 'shirin', "40g", "yaxshi")
b2=Product("yashil", "5sm", "4sm", "olma", "15fevral", 'shirin', "150g", "yaxshi")
b3=Product("qizil", "4sm", "2sm", "qalampir", "15fevral", 'achchiq', "20g", "yaxshi")

print(b1.info())
print(b2.info())
print(b3.info())

class Shakalad(Product):
    
    def get_rang(self):
        return self.rang
    
    def get_vazni(self):
        return self.vazni
    
    def get_uzunligi(self):
        return self.uzunligi

a4=Shakalad("sariq", "7sm", "2sm", "banan", "15fevral", 'shirin', "40g", "yaxshi")
a5=Shakalad("yashil", "5sm", "4sm", "olma", "15fevral", 'shirin', "150g", "yaxshi")
a6=Shakalad("qizil", "4sm", "2sm", "qalampir", "15fevral", 'achchiq', "20g", "yaxshi")

print(a4.get_rang())
print(a5.get_vazni())
print(a6.get_uzunligi())

class Parta():
    def __init__(self,rang,kattaligi,uzunligi,nomi,vazni):
        self.rang=rang
        self.kattaligi=kattaligi
        self.uzunligi=uzunligi
        self.nomi=nomi
        self.vazni=vazni
    
    def info(self):
        return self.rang,self.kattaligi,self.uzunligi,self.nomi,self.vazni
     
    def get_rang(self):
        return self.rang
    
    def get_kattaligi(self):
        return self.kattaligi

class Stol(Parta):
    
    def get_uzunligi(self):
        return self.uzunligi
    
class Parta1(Stol):
    
    def get_nomi(self):
        return self.nomi

c1=Parta1("oq", "50SM", "100SM", "mister", "1kg")
c2=Parta1("qora", "55SM", "110SM", "mister1", "1,5kg")
c3=Parta1("oq", "60SM", "120SM", "mister2", "2kg")

print(c1.info())
print(c2.get_uzunligi())
print(c3.get_nomi())

class User:
    def __init__(self, password):
        self.password = password
    
    def tekshir_password(self, kiritilgan_password):
        if kiritilgan_password == self.password:
            print("parol to'g'ri")
        else:
            print("parol xato")

d1= User("password123")

print(d1.tekshir_password("password123"))
print(d1.tekshir_password("wiehfuhguehg"))

class Magazin:
    def __init__(self,rang,kattaligi,uzunligi,nomi,narx):
        self.rang=rang
        self.kattaligi=kattaligi
        self.uzunligi=uzunligi
        self.nomi=nomi
        self.narx=narx
        
    def narx_tek(self, narxi):
        if narxi>=10000:
            print("o'rta")
        else:
            print("arzon")

m1=Magazin("qora", "10M", "10M", "boylar qo'ltig'i", 100000)
m2=Magazin("qora", "10M", "10M", "boylar qo'ltig'i", 1000)

print(m1.narx_tek(100000))
print(m2.narx_tek(1000))

class Telefon:
    def __init__(self, marka, model, narx):
        self.marka = marka
        self.model = model
        self.narx = narx

    def telefon_tekshir(self):
        telefonlar = ("Samsung", "Apple", "Google", "OnePlus")
        
        if self.marka in telefonlar:
            print("Bu yaxshi telefon")
        else:
            print("Bu telefonning markasi unchalik yaxshi emas")


t1 = Telefon("Samsung", "Galaxy S21", "2 yarim million")
t2 = Telefon("Nokia", "pro max", "10ming")


t1.telefon_tekshir() 
t2.telefon_tekshir()