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

    def StoreStudentScore(self):
        """
        Collect student data from user input and store it in the CSV file.
        """
        while True:
            print("\n1. Save student data")
            print("2. Go Back")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                rollno = input("Enter student roll number: ")
                name = input("Enter student name: ").capitalize()
                english = input("Enter English score: ")
                maths = input("Enter Maths score: ")
                science = input("Enter Science score: ")

                # Create dictionary to store student record
                student_record = {
                    "Rollno": rollno,
                    "name": name,
                    "english": english,
                    "maths": maths,
                    "science": science
                }

                # Check missing values
                missing_value = [key for key, value in student_record.items() if not value]

                if missing_value:
                    print(f"Failed to store data, following parameters missing: {','.join(missing_value)}")

                else:
                    try:
                        with open(self.csv_file, "a", newline="") as file:
                            field = ['Rollno', 'name', 'english', 'maths', 'science']
                            write = csv.DictWriter(file, fieldnames=field)
                            write.writerow(student_record)
                            print("Record Inserted Successfully.")

                    except Exception as e:
                        print("File not found")
                        exit()

            elif choice == 2:
                self.mainMenu()
            else:
                print("Invalid input. Enter correct choice")

    def mainMenu(self):
        """
        Display the main menu and handle user input.
        """
        while True:
            print("\n-----Main Menu-----")
            print("1. Retrieve Data")
            print("2. Store Student record")
            print("3. Exit")
            choice = int(input("Enter choice: "))

            if choice == 1:
                rollno = input("Enter student roll number: ")
                record = self.RetriveStudentScore(rollno)
                if record:
                    print(f"Student record for Roll number {rollno}: {record}")
            elif choice == 2:
                self.StoreStudentScore()
            elif choice == 3:
                exit()
            else:
                print("Enter correct choice")

f = studentScore('student_data.csv')
f.mainMenu()
