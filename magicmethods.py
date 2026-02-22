# Magic methods = Dunder methods (double underscore) __init__,__str__,__eq__
#                 They are automatically called by many of Python's built-in operations.
#                 They allow developers to define or customize the behavior of objects

class Student:

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __str__(self):
        return f"name: {self.name} gpa: {self.gpa}"
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __gt__(self, other):
        return self.gpa > other.gpa

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self. author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        if key == 'author':
            return self.author

def main():
    student1 = Student("Spongebob", 3.2)
    student2 = Student("Patrick", 2.0)
    print(student1)
    print(student1 == student2)
    print(student1 > student2)

    book1 = Book("The Hobbit", "J.R.R Tolkien", 310)
    book2 = Book("Harry Potter and the Philosopher's stone", "J.K. Rowling", 223)
    book3 = Book("The Lion", "J.R.R Tolkien", 172)
    print(book3)
    print(book1 == book3)
    print(book2 < book3)

    print(book2['title'])

if __name__=="__main__":
    main()
