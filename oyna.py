class Oyna():
    def __init__(self,razmer,firma,qalinligi,rangi="oq"):
        self.razmer=razmer
        self.firma=firma
        self.rangi=rangi
        self.qalinligi=qalinligi
        
    def get_info(self):
        return self.razmer,self.firma,self.rangi
    
    def get_razmer(self):
        return self.razmer
    
    def get_firma(self):
        return self.firma
    
    def get_qalinligi(self):
        return self.qalinligi
    
    def get_rangi(self):
        return self.rangi
    
a=Oyna("10SM", "uzb", "5SM")
b=Oyna("15SM", "rus", "6SM")
c=Oyna("20SM", "eng", "9SM")
d=Oyna("25SM", "kazak", "10SM")

print(a.get_info())
print(a.get_firma())
print(a.get_qalinligi())
print(a.get_rangi())
print(a.get_razmer())

print(b.get_info())
print(b.get_firma())
print(b.get_qalinligi())
print(b.get_rangi())
print(b.get_razmer())

print(c.get_info())
print(c.get_firma())
print(c.get_qalinligi())
print(c.get_rangi())
print(c.get_razmer())

print(d.get_info())
print(d.get_firma())
print(d.get_qalinligi())
print(d.get_rangi())
print(d.get_razmer())

