class Students():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def average(self):
        total = 0
        sub_count = 0
        for number in self.marks:
            total += number
            sub_count += 1
        return(total//sub_count)
nori = Students("nori", [10, 20, 30])
print(nori.average())

jony = Students("jony", [20, 20, 30])
print(jony.average())