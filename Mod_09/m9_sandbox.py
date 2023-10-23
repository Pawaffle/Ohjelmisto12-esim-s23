import random

class Student:
    count = 0

    def __init__(self, name, age='ei ole tiedossa'):
        self.name = name
        self.age = age
        self.credits = 0
        Student.count += 1
        print(f'Uusi opiskelja on luotu. Opiskeljoiden määrä nyt on: {Student.count}')

    def say_hello(self):
        print(f'Terve! Minun nimi on {self.name} ja ikä {self.age} \n'
              f'Minulla on {self.credits} opintopistetta')

    def change_name(self, new_name):
        self.name = new_name

    def add_credits(self, new_credits):

        # if new_credits < 0: return

        if self.credits + new_credits < 0:
            self.credits = 0
        else:
            self.credits += new_credits


juoppa1 = Student('Joonas', 25)
#juoppa1.say_hello()
juoppa1.add_credits(5)
#juoppa1.say_hello()

#print(Student)
#print(juoppa1)

juoppa2 = Student('Veeti')
#juoppa2.say_hello()

luokka = []

for i in range(10):

    new_student = Student('Opiskelja_' + str(i), random.randint(18,40))
    new_student.add_credits(30)
    #new_student.say_hello()
    luokka.append(new_student)

    #Student('Opiskelja ' + str(i), random.randint(18,40)).say_hello()

luokka.append(juoppa1)
luokka.append(juoppa2)

print('\n Nyt kadotaan kuka on listassa \n')

for student in luokka:
    student.say_hello()