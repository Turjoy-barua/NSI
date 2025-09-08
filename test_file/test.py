class Student:
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks 
    def avg(self):
        total = 0
        for x in self.marks:
            total+=x
        print(f"the average is {total/3}")
c1 = Student("turjoy", [10, 20, 30])
c1.avg()