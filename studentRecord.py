import csv

class studentScore:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def RetriveStudentScore(self, rollno):
        """
        Retrieve and return student data for given roll number.
        """
        try:
            with open(self.csv_file, "r") as file:
                read = csv.DictReader(file)

                for element in read:
                    if element["Rollno"] == rollno:
                        return element

            print(f"No records found for Roll number {rollno}")

        except FileNotFoundError:
            print("File not found")
            exit()

    def mainMenu(self):
        """
        Display the main menu and handle user input.
        """
        while True:
            print("\n-----Main Menu-----")
            print("1. Retrieve Data")
            print("2. Exit")
            choice = int(input("Enter choice: "))

            if choice == 1:
                rollno = input("Enter student roll number: ")
                record = self.RetriveStudentScore(rollno)
                if record:
                    print(f"Student record for Roll number {rollno}: {record}")
            elif choice == 2:
                exit()
            else:
                print("Enter correct choice")

f = studentScore('student_data.csv')
f.mainMenu()
