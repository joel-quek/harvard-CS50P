class Student:
    def __init__(self,name,house):
        self.name=name
        self.house=house

    def __str__ (self):
        return f"{self.name} from {self.house}"
# ----------------------------------------------------------
    @property #getter
    def name(self):
        return self._name

    @name.setter #setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name
#---------------------------------------------------------
    @property #getter
    def house (self):
        return self._house

    @house.setter #setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
#---------------------------------------------------------
def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

main()