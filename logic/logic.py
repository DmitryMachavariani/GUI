class Student:
    def __init__(self):
        self.ARRAY = []

    @staticmethod
    def getinfo(self, id):
        data = self.filllist()
        if id in data:
            return data[id]

    def addstudent(self, data):
        if isinstance(data, list):
            self.ARRAY.append(data)

    def loadstudent(self, filename):
        try:
            f = open(filename, "r")
            try:
                data = f.readlines()
                for i in data:
                    explode = i.split(':')
                    self.ARRAY.append([explode[0], explode[1], explode[2]])

                return self.ARRAY
            except IOError:
                print("Не могу прочитать файл")
        except IOError:
            print("Ошибка открытия файла")

    @staticmethod
    def savestudent(data, filename):
        try:
            file = open(filename, "w")
            try:
                for i in data:
                    for j in i:
                        file.write(str(j) + ":")
                    file.write("\n")
            except IOError as e:
                print(e)
            finally:
                file.close()

        except IOError as e:
            print(e)
