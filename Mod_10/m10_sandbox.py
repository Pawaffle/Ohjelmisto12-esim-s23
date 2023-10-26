import random
names = ['Veeti', 'Pavel', 'Miro', 'Anna', 'Petteri', 'Katarina', 'Max', 'Matias', 'Sofi']
all_students = {}

'''

    1) Tehdään 3 opiskeljaa
    2) Luodaan kolme kurssia, kursseihin 1 ja 2 lisätän opiskeljoita
    3) Viimeisenä 2 koulua, Metropolia ja Laurea
    
Kurssi toimi omana luokkanaan 
Kurilla on:
    + nimi
    + lista opiskeljoista

'''

############################### FUNCTONS ################################

def screen_refresh():
    print('\n'*30)

def new_student_in_course(qty, course_name):
    for i in range(qty):
        st = Student(names[random.randint(0, 8)], str(random.randint(18, 30)))
        print(st)
        course = new_course(course_name)
        course.students.append(st)
        all_students[st.name] = st


def new_course(input):
    course = Course(input)
    return course

def add():
    print('What do you want to add?')
    var = course_or_student()
    if var == 'course':
        new_course()
    elif var == 'student':
        qty = int(input('How many studients? :'))
        course_name = input('Wish course you wanna use? :')
        new_student_in_course(qty, course_name)

############################### OBJECTS #################################

class Course:
    def __init__(self, new_name):
        self.name = new_name
        self.students = []

    def remove_student(self,student):
        self.students.remove(student)

    def check_course(self):
        print(f'Kurssin nimi on {self.name}')
        for student in self.students:
            print(f'Kursilla on: {student.name}')

    def add_credits_to_all(self,credits):
        for student in self.students:
            student.add_credits(credits)
            student.say_hello()


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


################################# MENU ###################################

def course_or_student():
    print(f'''
    1) Student
    2) Course 
    ''')

    var = int(input('>'))
    while var != (1 or 2):
        print('Wrong input, please try again')
        var = int(input('>'))

    if var == 1:
        var = 'student'
    else:
        var = 'course'

    return var


def menu():
    screen_refresh()
    command = ['', 'Add', 'Find', 'Delete', 'List', 'Exit']
    print()
    for i, c in enumerate(command):
        if i > 0:
            print(f'{i}) {c}')

def main():

    menu()
    number = input('\nAnna sopivan komennon numero: ')
    print()

    while number != '5':

        if number == '1':
            add()
        # elif number == '2':
        #     find()
        # elif number == '3':
        #     delete()
        # elif number == '4':
        #     list()


############################################################################

print(f'''Terve!
      Tämä ohjelma tarkotettu koulun rakentamiseksi''')

main()

print('MOROOOOO')

# math = Course('Matikka')
# new_student_in_course(3,math)
# math.check_course()
#
# math.add_credits_to_all(10)
# math.check_course()





