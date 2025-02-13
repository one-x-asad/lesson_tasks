class User():
    def __init__(self, name, surname, fullname, username, email, password):
        self.name = name
        self.surname = surname
        self.fullname = fullname
        self.username = username
        self.email = email
        self.password = password

    def info(self):
        return self.name, self.surname, self.fullname, self.username, self.email, self.password
    
    def get_name(self):
        return self.name
    
    def get_surname(self):
        return self.surname
    
    def get_fullname(self):
        return self.fullname
    
    def get_username(self):
        return self.username
    
    def get_email(self):
        return self.email
    
    def get_password(self):
        return self.password
    
class No_user(User):
    def __str__(self):
        return self.name,self.surname,self.fullname,self.username,self.email,self.password

a1 = No_user("asadbek1", "usmonov1", "asadbek usmonov1", "one_x_asad1", "noinsofjon1@gmail.com", 12345678)
a2 = No_user("asadbek2", "usmonov2", "asadbek usmonov2", "one_x_asad2", "noinsofjon2@gmail.com", 123456789)
a3 = No_user("asadbek3", "usmonov3", "asadbek usmonov3", "one_x_asad3", "noinsofjon3@gmail.com", 12345678910)

print(a1.info())
print(a1.get_name())
print(a1.get_surname())
print(a1.get_fullname())
print(a1.get_username())
print(a1.get_email())
print(a1.get_password())
print(a1.__str__())

print(a2.info())
print(a2.get_name())
print(a2.get_surname())
print(a2.get_fullname())
print(a2.get_username())
print(a2.get_email())
print(a2.get_password())
print(a2.__str__())

print(a3.info())
print(a3.get_name())
print(a3.get_surname())
print(a3.get_fullname())
print(a3.get_username())
print(a3.get_email())
print(a3.get_password())
print(a3.__str__())
