import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from logic.logic import Student

student = Student()

root = tkinter.Tk()
root.geometry("400x250+150+150")
root.resizable(0, 0)
root.title("Я типо программист")

t = ttk.Treeview(root)
t["columns"] = ("firstname", "lastname", "group")
t["show"] = "headings"

t.column("#0", width=1, anchor="center")
t.column("firstname", width=30)
t.column("lastname", width=30)
t.column("group", width=1, anchor="center")

t.heading("firstname", text="Имя")
t.heading("lastname", text="Фамилия")
t.heading("group", text="№ группы")

opendialog = filedialog.askopenfilename()
data = student.loadstudent(opendialog)
for i in data:
    t.insert("", "end", values=(i[0], i[1], i[2]))

t.pack(side="top", fill="both")

def parse(data):
    array = []
    for item in data.get_children():
        array.append(data.item(item)["values"])
    dialog = filedialog.asksaveasfilename()
    student.savestudent(array, dialog)

def adddata(data):
    if data[0].strip() == "" or data[1].strip() == "" or data[2].strip() == "":
        messagebox.showerror("Ошибка", "Поля не заполнены")
    else:
        t.insert("", "end", values=(data[0], data[1], data[2]))
        student.addstudent(data)

def newform():
    window = tkinter.Toplevel()
    window.resizable(0, 0)
    window.title("Добавление студента")

    frame = tkinter.Frame(window)

    labelname = tkinter.Label(frame, text="Имя").grid(row=0, column=0)
    labellastname = tkinter.Label(frame, text="Фамилия").grid(row=1, column=0)
    labelgroup = tkinter.Label(frame, text="Группа").grid(row=2, column=0)

    inputname = tkinter.Entry(frame)
    inputname.grid(row=0, column=1)

    inputlastname = tkinter.Entry(frame)
    inputlastname.grid(row=1, column=1)

    inputgroup = tkinter.Entry(frame)
    inputgroup.grid(row=2, column=1)

    button = tkinter.Button(window, text="Добавить")
    button.bind("<Button-1>", lambda event: adddata([inputname.get(), inputlastname.get(), inputgroup.get()]))
    frame.pack(fill="both")
    button.pack(side="bottom")

btnSave = tkinter.Button(root, text="Сохранить")
btnSave.bind("<Button-1>", lambda event: parse(t))
btnSave.pack(side="right")

btnAdd = tkinter.Button(root, text="Добавить", command=newform)
btnAdd.pack(side="left")

btnDelete = tkinter.Button(root, text="Удалить")
btnDelete.bind("<Button-1>", lambda event: t.delete(t.selection()))
btnDelete.pack(side="left")

root.mainloop()
