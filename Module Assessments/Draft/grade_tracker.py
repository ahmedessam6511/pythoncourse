def read_grades(file_path):
    try:
        with open(file_path, 'r') as file:
            grades = [float(line.strip()) for line in file.readlines()]
        return grades
    except FileNotFoundError:
        print("File not found. Please ensure the file path is correct.")
        return []
    except ValueError:
        print("Invalid data in file. Please ensure all lines contain valid grades.")
        return []

def write_grades(file_path, grades):
    try:
        with open(file_path, 'w') as file:
            for grade in grades:
                file.write(f"{grade}\n")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)

def main():
    file_path = 'grades.txt'
    grades = read_grades(file_path)

    while True:
        try:
            grade = float(input("Enter a grade (or type 'done' to finish): "))
            grades.append(grade)
        except ValueError:
            break

    write_grades(file_path, grades)
    average_grade = calculate_average(grades)
    print(f"Average grade: {average_grade:.2f}")

if __name__ == "__main__":
    main()