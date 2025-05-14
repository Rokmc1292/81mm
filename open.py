# 2022041018 소프트웨어학부 김태욱
'''
n명의 학생의 세개의 교과목 (영어, C-언어, 파이썬)에 대하여 
키보드로부터 학번, 이름, 영어점수, C-언어 점수, 파이썬 점수를 입력받아 총점, 평균, 학점, 등수를 계산하는 프로그램 작성
- 입력 함수, 총점/평균 계산 함수,  학점계산 함수, 등수계산 함수, 출력 함수 
- 삽입 함수, 삭제함수, 탐색 함수(학번, 이름), 정렬(총점)함수, 80점이상 학생 수 카운트 함수
몽고 db를 이용하여 데이터베이스를 구현함함
'''
from pymongo import MongoClient

class Student:
    def __init__(self, number, name, english, c_language, python):
        self.number = number
        self.name = name
        self.english = english
        self.c_language = c_language
        self.python = python
        self.total = english + c_language + python
        self.average = self.total / 3
        self.grade = self.get_grade()
        self.rank = 1

    def get_grade(self):
        if self.average >= 90:
            return "A"
        elif self.average >= 80:
            return "B"
        elif self.average >= 70:
            return "C"
        elif self.average >= 60:
            return "D"
        else:
            return "F"

    def __str__(self):
        return f"{self.number}\t{self.name}\t{self.english}\t{self.c_language}\t{self.python}\t{self.total}\t{self.average:.2f}\t{self.grade}\t{self.rank}"

    def to_dict(self):
        return {
            "number": self.number,
            "name": self.name,
            "english": self.english,
            "c_language": self.c_language,
            "python": self.python,
            "total": self.total,
            "average": self.average,
            "grade": self.grade,
            "rank": self.rank
        }

class StudentManager:
    def __init__(self, n):
        self.client = MongoClient("mongodb://localhost:27018/")
        self.db = self.client["school"]
        self.collection = self.db["students"]
        self.student_num = n

    def input_students(self):
        for _ in range(self.student_num):
            number = input("학번: ")
            name = input("이름: ")
            english = int(input("영어: "))
            c_language = int(input("C언어: "))
            python = int(input("파이썬: "))
            student = Student(number, name, english, c_language, python)
            self.collection.insert_one(student.to_dict())
        self.update_ranks()

    def update_ranks(self):
        students = list(self.collection.find())
        students.sort(key=lambda s: s['total'], reverse=True)  
    
        for rank, student in enumerate(students, start=1):
            self.collection.update_one(
            {"number": student["number"], "name": student["name"]},
            {"$set": {"rank": rank}}  
        )


    def print_students(self):
        print("==================================================================")
        print("학번\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
        print("==================================================================")
        for s in self.collection.find().sort("rank"):
            print(f"{s['number']}\t{s['name']}\t{s['english']}\t{s['c_language']}\t{s['python']}\t{s['total']}\t{s['average']:.2f}\t{s['grade']}\t{s['rank']}")

    def insert_student(self):
        number = input("학번: ")
        name = input("이름: ")
        english = int(input("영어: "))
        c_language = int(input("C언어: "))
        python = int(input("파이썬: "))
        student = Student(number, name, english, c_language, python)
        self.collection.insert_one(student.to_dict())
        self.update_ranks()

    def remove_student(self):
        number = input("삭제할 학생의 학번: ")
        name = input("삭제할 학생의 이름:")
        result = self.collection.delete_one({"number": number,"name":name})
        if result.deleted_count:
            print("학생 정보가 삭제되었습니다.")
        else:
            print("해당 학생을 찾을 수 없습니다.")
        self.update_ranks()

    def search_student(self):
        number = input("찾을 학생의 학번: ")
        name = input("찾을 학생의 이름:")
        student = self.collection.find_one({"number": number,"name":name})
        if student:
            print(f"{student['number']}\t{student['name']}\t{student['english']}\t{student['c_language']}\t{student['python']}\t{student['total']}\t{student['average']:.2f}\t{student['grade']}\t{student['rank']}")
        else:
            print("해당 학생을 찾을 수 없습니다.")

    def sort_students(self):
        print("총점을 기준으로 정렬된 목록입니다:")
        self.update_ranks()
        self.print_students()

    def count_above_80(self):
        count = self.collection.count_documents({"average": {"$gte": 80}})
        print(f"80점 이상인 학생 수: {count}")


def main():
    n = int(input("학생수를 입력하세요: "))
    manager = StudentManager(n)
    manager.input_students()
    while True:
        print("\n메뉴:")
        print("1. 학생 목록 출력")
        print("2. 학생 추가")
        print("3. 학생 삭제")
        print("4. 학생 검색")
        print("5. 총점 기준 정렬")
        print("6. 80점 이상 학생 수 출력")
        print("7. 종료")
        choice = input("선택: ")
        if choice == "1":
            manager.print_students()
        elif choice == "2":
            manager.insert_student()
        elif choice == "3":
            manager.remove_student()
        elif choice == "4":
            manager.search_student()
        elif choice == "5":
            manager.sort_students()
        elif choice == "6":
            manager.count_above_80()
        elif choice == "7":
            print("프로그램을 종료합니다.")
            break

if __name__ == "__main__":
    main()
