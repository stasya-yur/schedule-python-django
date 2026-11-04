import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from school.models import Subject, Teacher, ClassRoom, Student

def main_menu():
    choice = ''
    while choice != 'n':
        choice = input("Оберіть дію: 1. Додати предмет, 2. Додати вчителя, 3. Додати клас, 4. Додати учня, n. Закінчити роботу")

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
        elif choice == "n" or choice == 'вихід':
            print("Ви вийшли з застосунку.")
            break
        else:
            print("Такого варіанту не існує.")

print("Вітаю у застосунку!")
main_menu()