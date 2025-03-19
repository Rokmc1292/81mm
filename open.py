# 2022041018 김태욱
# 5명의 학생의 세개의 교과목 (영어, C-언어, 파이썬)에 대하여  키보드로부터 입력받아 총점, 평균, 학점, 등수를 계산하는 프로그램
import sys

# 클래스를 이용하여 학생을 구현한다
class Student:
  def __init__(self, number,name, english, c_language, python):
    self.number = number
    self.name = name
    self.english = english
    self.c_language = c_language
    self.python = python
    self.total = 0
    self.average = 0
    self.grade = 0
    self.rank = 1 
    
  def __str__(self):
    return f"{self.number}\t{self.name}\t{self.english}\t{self.c_language}\t{self.python}\t{self.total}\t{self.average:.2f}\t{self.grade}\t{self.rank}"

students = []
def input_student():
  for i in range(5):
    number = input("학번:")
    name = input("이름:")
    english = input("영어:")
    c_language = input("C언어:")
    python = input("파이썬:")
    students.append(Student(number,name,int(english),int(c_language),int(python)))
  
def total_and_avg(students):
  for st in students:
    st.total = st.english + st.c_language + st.python
    st.average = st.total / 3
  
def get_grade(students):
  for st in students:
    if st.average >= 90:
      st.grade = "A"
    elif st.average >= 80:
     st.grade = 'B'
    elif st.average >= 70:
      st.grade = 'C'
    elif st.average >= 60:
      st.grade = 'D'
    else:
      st.grade = 'F'
  
def get_rank(students):
  for s1 in students:
    for s2 in students:
      if s1.average < s2.average:
        s1.rank += 1

def print_student():
  print("==================================================")
  print("\n이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
  print("\n==================================================\n")
  for s in students:
    print(s)

input_student()
total_and_avg(students)
get_grade(students)
get_rank(students)
print_student()