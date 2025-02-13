try:
    print(a)
    a=1
except NameError:
    print("o'zgaruchi topilmadi")

try:
    a=10
    b=0
    
    javob= 10/0
except ZeroDivisionError:
    print("nolga bo'lingan son javobi ham 0 bo'ladi")

try:
    x = "harf" + 10
except TypeError:
    print("Xatolik siz son kiritishingiz kerak edi")
