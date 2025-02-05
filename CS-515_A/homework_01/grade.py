# -*- coding: utf-8 -*-
"""
School: Stevens Institute of Technology
Course: CS-515_A
Instructor: Prof. Rocco Polimeni
----- ----- ----- ----- -----
Homework 01 - C, grade.py
Requirement: Calculating Letter Grades
----- ----- ----- ----- -----
@author: Yujun Kong
"""


def calculate(number_grade: str) -> str:
    """ conclude a letter grade based on a given specific mumerical grade. """

    try:
        float(number_grade)
    except Exception:
        return "N/A"
    else:
        num = float(number_grade)

    if number_grade < 0 or number_grade > 100:
        return "N/A"
    else:
        num = float(number_grade)

    if num < 0:
        return "N/A"
    elif num > 100:
        return "N/A"

    if 0 <= num < 60:
        return "F"
    elif 60 <= num < 70:
        return "D"
    elif 70 <= num < 80:
        return "C"
    elif 80 <= num < 90:
        return "B"
    elif 90 <= num <= 100:
        return "A"


def manual_test() -> None:
    """ raise a manual testing to validate correctness. """

    ipt_val = input("\nInput a numeric grade to get a letter grade: ")
    print(f"Number-grade {ipt_val} is letter-graded '{calculate(ipt_val)}'\n")


def main():
    """ main program entry point. """

    manual_test()


if __name__ == "__main__":
    main()
