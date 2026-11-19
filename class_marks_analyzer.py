"""
PS No. 22 - Class Marks Analyzer
Rungta International Skills University - School of Computer Science and Engineering
Bachelor of Technology - Computer Science and Engineering

Problem Statement:
    Create a program that takes the marks of a class as a list, validates them
    and uses NumPy to calculate the mean, median, highest, lowest, standard
    deviation, pass count and the number of students above average.

Language : Python 3
Concepts : NumPy, Lists, Functions, Statistics

Rules:
    - Marks are entered as numbers separated by spaces and must be from 0 to 100.
    - Pass mark is 40.
    - Standard deviation is the population value (numpy's default, ddof=0).
"""

import numpy as np


def get_marks():
    """
    Reads marks of a class as space-separated numbers from the console,
    validates them and converts them into a NumPy array.

    Returns:
        numpy.ndarray: A 1-D array of valid marks (floats), each in [0, 100].
    """
    while True:
        raw_input_line = input("Enter the marks of the class (separated by spaces): ").strip()

        if not raw_input_line:
            print("Error: No marks entered. Please try again.\n")
            continue

        tokens = raw_input_line.split()
        marks_list = []
        invalid_tokens = []

        for token in tokens:
            try:
                value = float(token)
            except ValueError:
                invalid_tokens.append(token)
                continue

            if value < 0 or value > 100:
                print(f"Invalid: Marks must be between 0 and 100. '{token}' is out of range.")
                continue

            marks_list.append(value)

        if invalid_tokens:
            invalid_str = ", ".join(invalid_tokens)
            print(f"Invalid marks '{invalid_str}'. Enter numbers only.")

        if not marks_list:
            print("No valid marks were entered. Please try again.\n")
            continue

        # Convert validated list of marks into a NumPy array
        return np.array(marks_list)


def analyze_marks(marks, pass_mark=40):
    """
    Analyzes a NumPy array of marks using NumPy statistical functions.

    Args:
        marks (numpy.ndarray): Array of student marks.
        pass_mark (int/float): Minimum mark required to pass. Default is 40.

    Returns:
        dict: A dictionary containing mean, median, highest, lowest,
              standard deviation, passed count, failed count,
              pass percentage and number of students above average.
    """
    total_students = marks.size

    mean_marks = np.mean(marks)
    median_marks = np.median(marks)
    highest_mark = np.max(marks)
    lowest_mark = np.min(marks)
    std_dev = np.std(marks)  # population standard deviation (ddof=0)

    passed_count = int(np.sum(marks >= pass_mark))
    failed_count = total_students - passed_count
    pass_percentage = (passed_count / total_students) * 100

    above_average_count = int(np.sum(marks > mean_marks))

    return {
        "total_students": total_students,
        "mean": mean_marks,
        "median": median_marks,
        "highest": highest_mark,
        "lowest": lowest_mark,
        "std_dev": std_dev,
        "passed": passed_count,
        "failed": failed_count,
        "pass_percentage": pass_percentage,
        "above_average": above_average_count,
    }


def display_results(results):
    """
    Prints the analysis results in a neat, readable format.

    Args:
        results (dict): Dictionary returned by analyze_marks().
    """
    print("\n----- Class Marks Analysis Report -----")
    print(f"Total Students     : {results['total_students']}")
    print(f"Mean               : {results['mean']:.2f}")
    print(f"Median             : {results['median']:.2f}")
    print(f"Highest Mark       : {results['highest']:.2f}")
    print(f"Lowest Mark        : {results['lowest']:.2f}")
    print(f"Standard Deviation : {results['std_dev']:.2f}")
    print(f"Passed             : {results['passed']} of {results['total_students']}")
    print(f"Failed             : {results['failed']} of {results['total_students']}")
    print(f"Pass Percentage    : {results['pass_percentage']:.2f}%")
    print(f"Above Average      : {results['above_average']} students")
    print("----------------------------------------\n")


def main():
    print("===== Class Marks Analyzer =====\n")
    marks = get_marks()
    results = analyze_marks(marks)
    display_results(results)


if __name__ == "__main__":
    main()
