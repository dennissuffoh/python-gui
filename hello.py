#create class

class staff:
    grade = 5
    total_hours =180
    def __init__(self,name,age,dept,basic):
        self.name = name
        self.age = age
        self.dept = dept
        self.basic = basic

    def total_overtime(self):
        return self.total_hours - 180

    def hourly_rate(self):
        return self.basic/self.total_hours

s1=staff('adam',23,'eden',1000)

print(type(s1))
print(s1.name)
print(s1.total_hours)
print(s1.grade)
print(s1.hourly_rate())
print(s1.total_overtime())