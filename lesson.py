class User():
    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        self.password=password

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

x=User("vali", "valibeshbarmoq777@gmail.com", 12345)

print(x.get_email())
print(x.get_name())
print(x.get_password())