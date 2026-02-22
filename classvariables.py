# class variables = shared amoung all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objeccts create from that class

class Student:
    class_year = 2024 #class variables: they are defined outside the constructor, can be accessed for all objects. They allow you to share data among all objects
    num_students = 0
    def __init__(self, name, age ):
        self.name = name #Intance variables: are defined inside the constructor
        self.age = age
        Student.num_students += 1 #Use Student.num_students to refer to the class variable. This function increments the number of student 1 by one


def main():

    student1 = Student("Spongebob", 31) #Constructure
    student2 = Student("Patrick", 35) #Constructure
    student3 = Student("Squidward", 55)
    student4 = Student("Sandy", 27)

    print(student1.name)
    print(student1.age)
    print(Student.class_year) #In this case, you can use either Student.class_year or student1.class_year to access this class variable but Student.class_year is more readable
    
    print("------------------------------------")
    
    print(student2.name)
    print(student2.age)
    print(Student.class_year) #In this case, you can use either Student.class_year or student1.class_year to access this class variable but Student.class_year is more readable
    
    print("------------------------------------")

    print(f"My graduating class of {Student.class_year} students \n") #This is a class variable. It belongs to all objects


if __name__ == "__main__":
    main()
