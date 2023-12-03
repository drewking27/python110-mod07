# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   AKing,12/2/23,Completed Assignment
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.


# TODO Create a Person Class
class Person:
    """
    A class representing person data
        Properties:
    - first_name (str): The student's first name.
    - last_name (str): The student's last name.
    ChangeLog:
    - AKing, 12.2.2023: Created the class.
    """
# TO-DO Add first_name and last_name properties to the constructor (Done)
def __init(self, first_name = '', last_name = ''):
    self.first_name = first_name
    self.last_name = last_name
# TO-DO Create a getter and setter for the first_name property (Done)
# Creating the getter for first_name
@property
def first_name(self):
    return self.__first_name.title()
# Creating setter for first name
@first_name.setter
def first_name(self, value):
    if value.isalpha() or value == "":
        self.__first_name = value
    else:
        raise ValueError("The first name should only contain letters.")
# TO-DO Create a getter and setter for the last_name property (Done)
# Getter for last_name
@property
def last_name(self):
    return self.__last_name.title()
# Setter for last_name
@last_name.setter
def last_name(self, value):
    if value.isalpha() or value == "":
        self.__last_name = value
    else:
        raise ValueError("The last name should only be letters.")
# TO-DO Override the __str__() method to return Person data (Done)
# Override the __str__() method
def __str__(self):
    return f'{self.first_name},{self.last_name}'
# TO-DO Create a Student class the inherits from the Person class (Done)
class Student(Person):
    """
    A class representing student data.
    Properties:
    - first_name (str): The student's first name. # Inherited from Person class
    - last_name (str): The student's last name. # Inherited from Person class
    - course_name - the course that the student is registering for
    ChangeLog:
    - AKing, 12.2.2023: Created the class.

    """
# TO-DO call to the Person constructor and pass it the first_name and last_name data (Done)
def __init__(self, first_name = '', last_name = '', course_name = ''):
    # Passing parameter data to Person class
    super().__init__(first_name = first_name, last_name = last_name)
    self.course_name = course_name
# TO-DO add a assignment to the course_name property using the course_name parameter (Done)


# TO-DO add the getter for course_name (Done)
# Creating getter for course_name
@property
def course_name(self):
    return self.__course_name.title()
# TO-DO add the setter for course_name (Done)
# Creating setter
@course_name.setter
def course_name(self, value):
    if value.isalpha() or not value.isalpha() or value == "":
        self.__course_name = value
    else:
        raise ValueError("There was a non-specific error")
    # Overriding the default __str__() method
# TO-DO Override the __str__() method to return the Student data (Done)
def __str__(self):
    return f'{self.first_name},{self.last_name},{self.course_name}'


# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    AKing,1.1.2030,Created Class
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from a json file and loads it into a list of dictionary rows

        ChangeLog: (Who, When, What)
        AKing,1.1.2030,Created function

        :param file_name: string data with name of file to read from
        :param student_data: list of dictionary rows to be filled with file data

        :return: list
        """

        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)

        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        AKing,1.1.2030,Created function

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be writen to the file

        :return: None
        """

        try:
            list_of_dict_data = []
            for students in student_data:
                students_json = {"FirstName": student.first_name,
                                 "LastName": student.last_name,
                                 "CourseName": student.course_name}
                # Append data to list
                list_of_dict_data.append(students_json)
            # Open enrollments.json and write list
            file = open(file_name,"w")
            json.dump(list_of_dict_data, file)
            file.close()

            print()
            print('*' * 50)
            print("The following data is saved: \n")

            for student in student_data:
                print(f'{student.first_name},'
                      f'{student.last_name},'
                      f'{student.course_name}')
                print('*' * 50)
        except TypeError as e:
            IO.output_error_messages(message="Ensure data is in JSON format", error=e)
        except Exception as e:
            IO.output_error_messages(message="There was a non specific error", error=e)
        finally:
            if file.closed == False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    RRoot,1.2.2030,Added menu output and input functions
    RRoot,1.3.2030,Added a function to display the data
    RRoot,1.4.2030,Added a function to display custom error messages
    AKing,12/2/23, edited class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

        ChangeLog: (Who, When, What)
        AKing,1.3.2030,Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        AKing,1.1.2030,Created function


        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        AKing,1.1.2030,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):
        """ This function displays the student and course names to the user

        ChangeLog: (Who, When, What)
        AKing,1.1.2030,Created function

        :param student_data: list of dictionary rows to be displayed

        :return: None
        """

        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the student's first name and last name, with a course name from the user

        ChangeLog: (Who, When, What)
        AKing,1.1.2030,Created function

        :param student_data: list of dictionary rows to be filled with input data

        :return: list
        """

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student)
            print()
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data


# Start of main body

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
