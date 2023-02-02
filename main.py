import random
import time 
# class cat():
#     """
#     Для чего этот класс?
#     """
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def meeow(self):
#         return self.name + " Мияу Мияу Мияу "

#     def eat(self):
#         return self.name + " Кушает"
    
#     def play(self):
#         return self.name + " Играет"
    
#     def sleep(self):
#         return self.name + " Уснула"


#     def __str__(self):
#         return f"Вы не указали что вернуть"

# cat1 = cat("Musi",2)
# cat2 = cat("German",3)

# print(cat1.meeow())




# class people():
    
#     def __init__(self, name):
#         self.name = name
#         # self.age = age
#         # self.gender = gender
#         # self.birthday = birthday
#         # self.target = target
#         # self.work = work
#         # self.pet = pet
#     def privet(self):
#         return "Всем привет, я " + self.name
#     def birthday(self):
#         return self.name +" родился 11.06.2001 году , сейчас мне 21 " 
#     def target(self):
#         return "У " + self.name + " цель стать пиздатым айтишником "
#     def work(self):
#         return "На данный момент " + self.name + " не работает, он учиться ITC Bootcamp"
#     def pet(self):
#         return "У " + self.name + " нету домашних животных, так как у него алергия на шерсть"
#     def poka(self):
#         return "Всем пока, удачи братишка)"
#     def __str__(self):
#         return f"!!!"

# people1 = people("Ади")

# print(people1.privet())
# time.sleep(2)
# print(people1.birthday())
# time.sleep(2)
# print(people1.target())
# time.sleep(2)
# print(people1.work())
# time.sleep(2)
# print(people1.pet())
# time.sleep(2)
# print(people1.poka())




class Calculator():
    def __init__(self, arg1,arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def add(self):
        return f"{self.arg1 + self.arg2} + плюс"

    def sub(self):
        return f"{self.arg1 - self.arg2} - минус"

    def mul(self):
        return f"{self.arg1 * self.arg2} * умножение"

    def div(self):
        try:
            return f"{self.arg1 // self.arg2} / деление"
        except ZeroDivisionError:
            return "На ноль делить нельзя"

arg1 = int(input("Введите первое число: "))
arg2 = int(input("Введите второе число: "))
cal1 = Calculator(arg1,arg2)

print(cal1.add())
print(cal1.sub())
print(cal1.mul())
print(cal1.div())
