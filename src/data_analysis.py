#!/usr/bin/env python3
"""
Student Grade Analysis - Modular Version
This demonstrates __main__ execution control and modular design
"""

import csv
from pathlib import Path

def load_students(csv_file):
    """Load student data from CSV file."""
    students = []
    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({
                    'name': row['name'],
                    'age': int(row['age']),
                    'grade': int(row['grade']),
                    'subject': row['subject']
                })
    except FileNotFoundError:
        print(f"Error: File {csv_file} not found")
    except Exception as e:
        print(f"Error loading data: {e}")

    return students

def calculate_average(grades):
    """Calculate the average of a list of grades."""
    if not grades:
        return 0
    return sum(grades) / len(grades)

def find_highest_grade(grades):
    """Find the highest grade in a list."""
    if not grades:
        return 0
    return max(grades)

def save_results_to_file(filename, students, average, highest):
    """Save analysis results to a file."""
    try:
        with open(filename, 'w') as file:
            file.write("Student Grade Analysis\\n")
            file.write("=" * 30 + "\\n\\n")

            file.write("Individual Grades:\\n")
            for student in students:
                file.write(f"{student['name']}: {student['grade']}\\n")

            file.write(f"\\nSummary:\\n")
            file.write(f"Average grade: {average:.1f}\\n")
            file.write(f"Highest grade: {highest}\\n")
            file.write(f"Total students: {len(students)}\\n")

        print(f"Results saved to {filename}")
        return True
    except Exception as e:
        print(f"Error saving file: {e}")
        return False

def main():
    """Main function to run the analysis."""
    print("Student Grade Analysis - Modular Version")
    print("=" * 40)

    # Load data from CSV
    students = load_students('data/students.csv')

    if not students:
        print("No student data to analyze")
        return

    # Calculate statistics
    grades = [student['grade'] for student in students]
    average = calculate_average(grades)
    highest = find_highest_grade(grades)

    # Display results
    print(f"Analyzed {len(students)} students")
    print(f"Average grade: {average:.1f}")
    print(f"Highest grade: {highest}")

    # Save results
    output_file = 'output/analysis_report.txt'
    Path('output').mkdir(exist_ok=True)

    if save_results_to_file(output_file, students, average, highest):
        print("✅ Analysis complete!")
    else:
        print("❌ Analysis failed")

# This code only runs when the script is executed directly
# It won't run when the script is imported as a module
if __name__ == "__main__":
    main()
