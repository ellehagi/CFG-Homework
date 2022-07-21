
class Student:
# these methods set diffrent attributes into a variable
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()

    def add_subjects(self, all_subjects):
        for subj in all_subjects:
            self.add_subjects[subj] = None




class CFGStudent(Student):

    def __init__(self, stream, name, age, id):
        super().__init__(stream, name, age, id)
        self.specialization = stream
# this method adds the subject onto the dictionary
    def add_subject(self, subject):
        self.subjects[subject] = None

    # this method removes a subject from the dictionary
    def remove_subject(self, subject):
        self.subjects.pop(subject)

    def view(self):
        for subject in self.subjects.keys():
            print(subject)
    def get_grade(self, subject, grade):
        self.subjects[subject] = grade

    def get_overall_grade(self):
        current = dict({(k,v) for k,v in self.subjects.items() if v is not None})
        return sum(current.values()) / len(current.values())
