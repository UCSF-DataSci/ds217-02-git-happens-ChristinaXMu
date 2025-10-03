#!/usr/bin/env python3
# src/data_analysis_functions.py

import os

def load_data(filename):
    """Generic loader that checks file extension"""
    if filename.endswith('.csv'):
        return load_csv(filename)
    else:
        raise ValueError("Unsupported file type")

def load_csv(filename):
    """Load CSV data into a list of student dictionaries"""
    students = []
    with open(filename, 'r') as f:
        lines = f.readlines()[1:]  # skip header
        for line in lines:
            name, age, grade, subject = line.strip().split(',')
            students.append({
                "name": name,
                "age": int(age),
                "grade": int(grade),
                "subject": subject
            })
    return students

def analyze_data(students):
    grades = [s['grade'] for s in students]
    stats = {
        "total_students": len(students),
        "average_grade": sum(grades)/len(grades),
        "highest_grade": max(grades),
        "lowest_grade": min(grades),
        "subjects": {},
        "grade_distribution": {}
    }
    for s in students:
        stats['subjects'][s['subject']] = stats['subjects'].get(s['subject'], 0) + 1
    stats['grade_distribution'] = analyze_grade_distribution(grades)
    return stats

def analyze_grade_distribution(grades):
    dist = {'A':0,'B':0,'C':0,'D':0,'F':0}
    for g in grades:
        if g >= 90:
            dist['A'] += 1
        elif g >= 80:
            dist['B'] += 1
        elif g >= 70:
            dist['C'] += 1
        elif g >= 60:
            dist['D'] += 1
        else:
            dist['F'] += 1
    return dist

def generate_report(stats):
    report = "Analysis Report\n\n"
    report += f"Total number of students: {stats['total_students']}\n"
    report += f"Average grade: {stats['average_grade']:.1f}\n"
    report += f"Highest grade: {stats['highest_grade']}\n"
    report += f"Lowest grade: {stats['lowest_grade']}\n\n"
    report += "Students per subject:\n"
    for subj, count in stats['subjects'].items():
        report += f"  {subj}: {count}\n"
    report += "\nGrade distribution:\n"
    for grade, count in stats['grade_distribution'].items():
        percent = count / stats['total_students'] * 100
        report += f"  {grade}: {count} ({percent:.1f}%)\n"
    return report

def save_results(report, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        f.write(report)

def main():
    students = load_data('data/students.csv')
    stats = analyze_data(students)
    report = generate_report(stats)
    save_results(report, 'output/analysis_report.txt')
    print("Advanced analysis complete. Report saved to output/analysis_report.txt")

if __name__ == "__main__":
    main()