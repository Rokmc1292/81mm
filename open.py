# 2022041018 김태욱
'''
조건: 5명의 학생의 세가의 교과몰 (영어, C-언어, 파이썬)에 대해 
키보드로부터 학번, 이름, 영어점수, C-언어 점수, 파이썬 점수를 입력받아 총점, 평균, 학점, 등수를 계산하는 프로그램 작성
- 입력 함수, 총점/평균 계산 함수,  학점계산 함수, 등수계산 함수, 출력 함수 
- 생입 함수, 삭제 함수, 탐색함수(학번, 이름), 정렬(총점)함수, 80점이상 학생 수 카운트 함수
'''

class Student:
    # 학생객체의 생성자
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

    #  학생의 학점을 계산하는 메소드
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
    # 객체를 출력하면 호출되는 함수
    def __str__(self):
        return f"{self.number}\t{self.name}\t{self.english}\t{self.c_language}\t{self.python}\t{self.total}\t{self.average:.2f}\t{self.grade}\t{self.rank}"


class StudentManager:
    def __init__(self):
        self.students = []

    # 학생들을 입력받는함수
    def input_students(self):  
        for _ in range(5):
            number = input("학번: ")
            name = input("이름: ")
            english = int(input("영어: "))
            c_language = int(input("C언어: "))
            python = int(input("파이썬: "))
            self.students.append(Student(number, name, english, c_language, python))
        self.update_ranks()
        
     # 학생들의 등수계산함수
    def update_ranks(self): 
        for s1 in self.students:
            s1.rank = 1
            for s2 in self.students:
                if s1.total < s2.total:
                    s1.rank += 1

    # 학생생 출력함수
    def print_students(self):  
        print("==================================================")
        print("학번\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
        print("==================================================")
        for s in self.students:
            print(s)
            
     # 학생들 삽입함수
    def insert_student(self):  
        number = input("학번: ")
        name = input("이름: ")
        english = int(input("영어: "))
        c_language = int(input("C언어: "))
        python = int(input("파이썬: "))
        self.students.append(Student(number, name, english, c_language, python))
        self.update_ranks()

    # 학생 삭제함수
    def remove_student(self):  
        number = input("삭제할 학생의 학번: ")
        name = input("삭제할 학생의 이름: ")
        for s in self.students:
            if s.number == number and s.name == name:
                self.students.remove(s)
                self.update_ranks()
                print("학생 정보가 삭제되었습니다.")
                return
        print("해당 학생을 찾을 수 없습니다.")

    # 학생 탐색함수
    def search_student(self):  
        number = input("찾을 학생의 학번: ")
        name = input("찾을 학생의 이름: ")
        for s in self.students:
            if s.number == number and s.name == name:
                print(s)
                return
        print("해당 학생을 찾을 수 없습니다.")

    # 학생 정렬함수
    def sort_students(self):  
        self.students.sort(key=lambda s: s.total, reverse=True)
        self.update_ranks()
        print("총점을 기준으로 정렬되었습니다.")

     # 80점 이상 학생 수 카운트 함수
    def count_above_80(self):  
        count = sum(1 for s in self.students if s.average >= 80)
        print(f"80점 이상인 학생 수: {count}")


def main():
    manager = StudentManager()
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
