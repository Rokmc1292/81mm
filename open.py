# 2022041018 김태욱
'''
조건: 5명의 학생의 세개의 교과목 (영어, C-언어, 파이썬)에 대하여 
키보드로부터 학번, 이름, 영어점수, C-언어 점수, 파이썬 점수를 입력받아 총점, 평균, 학점, 등수를 계산하는 프로그램 작성
- 입력 함수, 총점/평균 계산 함수,  학점계산 함수, 등수계산 함수, 출력 함수 
- 삽입 함수, 삭제 함수, 탐색함수(학번, 이름), 정렬(총점)함수, 80점이상 학생 수 카운트 함수
'''
# 학생 클래스 정의
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

# 학생 리스트
students = []

def input_students(): # 입력함수
    for _ in range(5):
        number = input("학번: ")
        name = input("이름: ")
        english = int(input("영어: "))
        c_language = int(input("C언어: "))
        python = int(input("파이썬: "))
        students.append(Student(number, name, english, c_language, python))
    update_ranks()

def update_ranks(): # 등수계산함수
    for s1 in students:
        s1.rank = 1
        for s2 in students:
            if s1.total < s2.total:
                s1.rank += 1

def print_students(): # 출력함수
    print("==================================================")
    print("학번\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
    print("==================================================")
    for s in students:
        print(s)

def insert_student(): # 삽입함수
    number = input("학번: ")
    name = input("이름: ")
    english = int(input("영어: "))
    c_language = int(input("C언어: "))
    python = int(input("파이썬: "))
    students.append(Student(number, name, english, c_language, python))
    update_ranks()

def remove_student(): # 삭제함수
    number = input("삭제할 학생의 학번: ")
    name = input("삭제할 학생의 이름: ")
    for s in students:
        if s.number == number and s.name == name:
            students.remove(s)
            update_ranks()
            print("학생 정보가 삭제되었습니다.")
            return
    print("해당 학생을 찾을 수 없습니다.")

def search_student(): # 탐색함수
    number = input("찾을 학생의 학번: ")
    name = input("찾을 학생의 이름: ")
    for s in students:
        if s.number == number and s.name == name:
            print(s)
            return
    print("해당 학생을 찾을 수 없습니다.")

def sort_students(): # 정렬함수수
    students.sort(key=lambda s: s.total, reverse=True)
    update_ranks()
    print("총점을 기준으로 정렬되었습니다.")

def count_above_80(): # 80점 이상 학생수 카운트함수수
    count = sum(1 for s in students if s.average >= 80)
    print(f"80점 이상인 학생 수: {count}")

def main():
    input_students()
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
            print_students()
        elif choice == "2":
            insert_student()
        elif choice == "3":
            remove_student()
        elif choice == "4":
            search_student()
        elif choice == "5":
            sort_students()
        elif choice == "6":
            count_above_80()
        elif choice == "7":
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 번호를 입력해주세요.")

if __name__ == "__main__":
    main()
