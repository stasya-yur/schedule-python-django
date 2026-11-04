import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from school.models import Subject, Teacher, ClassRoom, Student, Schedule, Grade


def main_menu():
    choice = ''
    while choice != 'n':
        choice = input("Оберіть дію: \n1. Додати предмет, \n2. Додати вчителя, \n3. Додати клас, \n4. Додати учня, \n5. Додати заняття в розклад, \n6. Поставити оцінку, \n7. Подивитись розклад для окремого класу, \nn. Закінчити роботу ")

        if choice == "1":
            title = input("Введіть назву предмета: ")
            description = input("Введіть опис предмета: ")
            if Subject.objects.filter(title=title).exists():
                print("Предмет з такою назвою вже існує. ")
            else:
                Subject.objects.create(title=title, description=description)
                print("Новий предмет успішно створено.")

        elif choice == "2":
            name = input("Введіть ім'я нвоого вчителя: ")
            last_name = input("Введіть прізвище нового вчителя: ")
            subjects_list = Subject.objects.all()
            teacher_subject = input(f"Оберіть предмет для вчителя: {subjects_list}")
            while not Subject.objects.filter(title=teacher_subject).exists():
                print("Ви ввели некоректний предмет.")
                teacher_subject = input(f"Оберіть предмет для вчителя: {subjects_list}")
            subject_object = Subject.objects.get(title=teacher_subject)
            Teacher.objects.create(name=name, last_name=last_name, subject=subject_object)
            print("Новий вчитель успішно доданий.")

        elif choice == '3':
            title = input("Введіть код класу: ")
            year = input("В якому році це клас стартував? ")
            if ClassRoom.objects.filter(title=title).exists() and ClassRoom.objects.filter(year=year).exists():
                print("Цей клас вже доданий до бази даних.")
            else:
                ClassRoom.objects.create(title=title, year=year)
                print("Клас доданий.")

        elif choice == '4':
            name = input("Введіть ім'я учня: ")
            last_name = input("Введіть прізвище учня: ")
            classes = ClassRoom.objects.all()
            clas = input(f"Оберіть клас учня: {classes}")
            while not ClassRoom.objects.filter(title=clas).exists():
                print("Такого класу не існує.")
                clas = input(f"Оберіть клас учня: {classes}")
            class_object = ClassRoom.objects.get(title=clas)
            Student.objects.create(name=name, last_name=last_name, classroom=class_object)
            print("Студента успішно додано.")

        elif choice == "5":
            day = input("Оберіть день тижня: ")
            time = input("Оберіть час (ГГ:ХХ): ")
            subject = input(f"{Subject.objects.all()} \nОберіть предмет: ")
            while not Subject.objects.filter(title=subject).exists():
                print("Такого предмету не існує.")
                subject = input("Оберіть предмет: ")
            subject_object = Subject.objects.get(title=subject)
            clas = input(f"{ClassRoom.objects.all()}\nОберіть клас: ")
            while not ClassRoom.objects.filter(title=clas).exists():
                print("Такого класу не існує.")
                clas = input(f"Оберіть клас: ")
            class_object = ClassRoom.objects.get(title=clas)
            teacher_last_name = input(f"{Teacher.objects.filter(subject=subject_object)}\nВведіть прізвище вчителя: ")
            while not Teacher.objects.filter(last_name=teacher_last_name).exists():
                print("Такого вчителя не зареєстровано.")
                teacher_last_name = input(f"Введіть прізвище вчителя: ")
            if Teacher.objects.filter(last_name=teacher_last_name, subject=subject_object).count()>1:
                teacher_name = input(f"{Teacher.objects.filter(last_name=teacher_last_name)}\nВведіть ім'я вчителя: ")
                while not Teacher.objects.filter(name=teacher_name).exists():
                    print("Такого вчителя не зареєстровано.")
                    teacher_last_name = input(f"Введіть ім'я вчителя: ")
                teacher_object = Teacher.objects.get(name = teacher_name, last_name = teacher_last_name)
            else:
                teacher_object = Teacher.objects.get(last_name = teacher_last_name)
            Schedule.objects.create(day_of_week=day, hour_of_start=time, subject=subject_object, classroom=class_object, teacher=teacher_object)
            print("Успішно додано.")
        elif choice =="6":
            student = input(f"{Student.objects.all()}\nОберіть студента (ім'я, прізвище через пробіл): ").split()
            while not Student.objects.filter(name = student[0], last_name = student[1]):
                print("Помилка. Перевірте правильність введених даних.")
                student = input("Оберіть студента (ім'я, прізвище клас через пробіл): ").split()
            if Student.objects.filter(name = student[0], last_name = student[1]).count()>1:
                while True:
                    classroom = input(f"{Student.objects.filter(name=student[0], last_name=student[1])}\n В якому класі навчається студентка? (код рік)").split()
                    try:
                        classroom_object = ClassRoom.objects.get(title = classroom[0], year = classroom[1])
                        student_object = Student.objects.get(name=student[0], last_name=student[1],classroom=classroom_object)
                        break
                    except:
                        print("Перевірте правильність введених даних.")
            student_object = Student.objects.get(name=student[0], last_name=student[1])
            subject = input(f"{Subject.objects.all()}\nОберіть предмет: ")
            subject_object = Subject.objects.get(title=subject)
            while True:
                try:
                    grade = int(input("Введіть оцінку: "))
                    break
                except:
                    print("Введіть ціле число!")
            date = input("Введіть дату (ГГГ-ММ-ДД): ")
            Grade.objects.create(student = student_object, subject = subject_object, grade=grade,date=date)
            print("Оцінку записано в журнал.")
        elif choice =="7":
            classroom = input(f"{ClassRoom.objects.all()}\nДля якого класу ви б хотіли переглянути розклад? (код, рік) ").split(", ")
            while not ClassRoom.objects.filter(title=classroom[0], year=classroom[1]):
                print("Такого класу не зареєстровано")
                classroom = input(f"Для якого класу ви б хотіли переглянути розклад? (код, рік) ").split(", ")
            classroom_object = ClassRoom.objects.get(title=classroom[0], year=classroom[1])
            for day in ['Понеділок', 'Вівторок', 'Середа','Четвер',"П'ятниця"]:
                print(f"----{day}----")
                print(Schedule.objects.filter(day_of_week = day))

        elif choice == "n" or choice == 'вихід':
            print("Ви вийшли з застосунку.")
            break
        else:
            print("Такого варіанту не існує.")

print("Вітаю у застосунку!")
main_menu()