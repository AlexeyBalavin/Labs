class get_LineAndObjects:
    def get_lines(file_name):
      with open(file_name, encoding="utf-8") as f:
        lines = f.read().split('\n')[1:]
      return lines
    
    
    def get_objects(lines):
      objects = []
      for line in lines:
        lst = line.split("|")
        objects.append(Student(lst[0], lst[1], lst[2], lst[3], lst[4], lst[5], lst[6], lst[7]))
      return objects
    

class Student:
  def __init__(self, i, full_name, group, age, gender,num1,num2,num3):
    self.id = int(i)
    sn, fn, on = tuple(full_name.split(" "))
    self.first_name = fn
    self.second_name = sn
    self.other_name = on
    self.group = group
    self.age = int(age)
    self.gender = gender
    self.sred = round((int(num1) + int(num2) + int(num3))/3, 1)
  def __str__(self):
    return f"{self.second_name} {self.first_name} {self.sred}"
      