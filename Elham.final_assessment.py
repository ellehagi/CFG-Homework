"""
TASK 1

Design a parent class called CFGStudent.

It should have general attributes like name, surname, age, email, student id
and methods to fetch student’s full name and student’s id.

Design a child class called NanoStudent, which  inherits from CFGStudent class.
This class should have exactly the same attributes as its parent class,
as well as an additional one called ‘specialization’ and course grades.

The child class ‘generate_id’ method should override its parent method to add the suffix ‘NANO’
in front of the id.

New methods ‘add_new_grade’ and ‘get_course_grades’ should be added.
You can use  it as a skeleton code for your classes OR adjust it and create your own.

SEE NOTES BELOW

"""


class CFGStudent:

    def __init__(self, name, surname, age, email, student_id):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.student_id = student_id

    @staticmethod
    def generate_id(self):
        'your code goes here'
        'create a random new id, which is any number between 1,000 and 10,000'
        self.student_id = 6000

        return f"{self.student_id}"
        'return id as a string'

        "Example '8754' "

    def get_id(self):
        'your code goes here'
        'fetch student id'
        return f"{self.student_id}"
    def get_fullname(self):
        "Expected outcome should be 'Name Surname' "
        'your code goes here'
        return f"My name is {self.name} {self.surname}"

class NanoStudent(CFGStudent):

    def __init__(self, name,surname,age,email,student_id,specialization,course_grades):
        'your code goes here'
        super().__init__(name, surname,age,email,student_id)
        self.specialization = specialization
        self.course_grades = course_grades

    @staticmethod
    def generate_id(self, student_id):
        'your code goes here'
        'create a random new id, which is a word NANO followed by any number between 1,000 and 10,000'
        'return id as a string'
        "Example 'NANO1234' "
        self.student_id = 'NANO1234'

    def add_new_grade(self, 'your code goes here'):
        'your code goes here'
        'update course_grades container'


        "Example: pass in a task name and its grade, so that both are added to course_grades"

    def get_course_grades(self):
        'your code goes here'
        'fetch course grades container and its values'



############################################

# Example run

s = CFGStudent('Anna', 'Smith', 18, 'anna@mail.com')  # do not pass ID, it should be generated automatically
print(s.get_fullname())
# returns 'Anna Smith'
print(s.student_id)
# returns '3868' or some other random number

cfg_s = NanoStudent('Software', name='Mia', surname='Papandopulu', age=20, email='mia@mail.com')
print(cfg_s.get_fullname())
# returns 'Mia Papandopulu'
print(cfg_s.get_id())
# returns 'NANO6180' or some other random number

cfg_s.add_new_grade('theory', 95)
cfg_s.add_new_grade('project', 78)
print(cfg_s.get_course_grades())
# returns {'theory': 95, 'project': 78}



"""
TASK 2

Given an index limit, find all corresponding Fibonacci values up to that limit in a sequence 
and return the sum of all even Fibonacci numbers. See more details in the task description in 
your assessment paper. 
"""


##### TESTS ####

def even_fibonacci_sum(n):
    # check that the input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return even_fibonacci_sum(n-1) + even_fibonacci_sum(n-2)

for n in range(1,30):
    print(n,":" ,even_fibonacci_sum(n))

print(even_fibonacci_sum(limit=10))  # should be 44
print(even_fibonacci_sum(limit=15))  # should be 188
print(even_fibonacci_sum(limit=1))   # should be 0

# I could not figure how to return the even numbers only



"""
TASK 3

Validate subsequence. Use suggested tests below to check
correctness of your solution. 
"""



#### TESTS ####

def is_valid_subsequence(array, sequence):
	i = 0
	for num in array:
		if i == len(sequence):
			break
		if sequence[i] == num:
			i += 1
	return i == len(sequence)

array1 = [5,1,22,25,6,-1,8,10]
sequence1 = [1,6,-1,-2]

print(is_valid_subsequence(array1, sequence1))  # FALSE


array2 = [5,1,22,25,6,-1,8,10]
sequence2 = [1,6,-1, 10]

print(is_valid_subsequence(array2, sequence2))  # TRUE


array3 = [5,1,22,25,6,-1,8,10]
sequence3 = [25]

print(is_valid_subsequence(array3, sequence3))  # TRUE



"""
TASK 4

WRITTEN ASSIGNMENT

Write a review on how 'class Employee' can be improved.
(See PDF document with the code example)
"""

"""
Following the Solid principles, a class should have a single responsibility 
and incorporating the db_engine attribute into employee class made the code a little messy. 
The db_engine attribute should have been its own class. I believe the code would have been a lot better if the person 
created a db_engine class the inherited from the class employee.
"""