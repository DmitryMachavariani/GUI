from logic.logic import Student

student = Student()

def printtable():
    lenfield = 19

    print("____________________________________________________________")
    print("|\t\tИмя\t\t\t|\t\tФамилия\t\t|\t\tГруппа\t\t|")
    print("____________________________________________________________")
    for i in student.ARRAY:
        print("|%s" % i[0], end="")
        for j in range(0, lenfield - len(i[0])):
            print(" ", end="")
        print("|", end="")

        print("%s" % i[1], end="")
        for j in range(0, lenfield - len(i[1])):
            print(" ", end="")
        print("|", end="")

        print("%s" % i[2], end="")
        for j in range(0, lenfield - len(i[2])):
            print(" ", end="")
        print("|")

        print("____________________________________________________________")

def delete():
    id = int(input("Введите номер студента: "))
    try:
        student.ARRAY.pop(id)
    except IndexError as e:
        print("Студента с таким номером нету")

def add():
    firstname = input("Введите имя: ")
    lastname = input("Введите фамилию: ")
    group = input("Введите группу: ")

    student.ARRAY.append([firstname, lastname, group])
    print("Студент успешно добавлен")

def printmenu():
    return input("Выберите пункт(д - добавить, у - удалить, с - сохранить, в - выход): ")

student.loadstudent("test.txt")
printtable()
while True:
    menu = printmenu()
    if menu == "в":
        print("До свидания!")
        break
    elif menu == "у":
        delete()
    elif menu == "д":
        add()
    elif menu == "с":
        student.savestudent(student.ARRAY, "test.txt")

    printtable()
