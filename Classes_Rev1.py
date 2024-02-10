# Review of classes.

class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)
    else: print("Grade value is of different type")

ndago = Student('Daniel Ndago', 16)
haruna = Student('Kwabena Haruna', 30)
gumma = Student('Simon Gumma', 32)

class Grade:
  minimum_passing = 65
  def __init__(self, score):
    self.score = score
  
gumma.add_grade(Grade(100)) # Adds 100% score to pieter grades.