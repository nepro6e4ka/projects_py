import pickle 
import os
# os.path.getsize - to know about file size
'''pickle:
dumps() - serialize object
converting data into bytes
loads() - deserialize'''


class Student:
    def __init__(self, full_name, number, email, assessments):
        self.full_name = full_name
        self.number = number
        self.email = email
        self.assessments = assessments
        # create atributes for this 
        # sample class

    def change_full_name(self, full_name):
        self.full_name = full_name
    
    def change_number(self, number):
        self.number = number
    
    def change_email(self, email):
        self.email = email
    
    def change_assessments(self, assessments):
        self.assessments = assessments
    
    '''
    def __str__(self):
        return '1'
    this method "__str__(self)" allows you to see info about 
    class "Student": 
    input:Student('qwe', 9, 2, 5) --> output:1
    '''

    def __str__(self):
        st = self.assessments.split()
        avg = sum(list(map(int, st))) / len(st)
        return f"Full name: {self.full_name} \nPhone number: {self.number} \nE-mail: {self.email} \nAssessments: {self.assessments} \nAverage: {avg} \nThis is a full information abouut this student!"
    
def get_inf():
    name = input('Enter the full name of the student, whitch you would like to add: ')
    number = input("Enter this student's phone number: ")
    email = input("Enter this student's e-mail: ")
    assessments = input("Enter this student's assessments with space(" "): ")

    student = Student(name, number, email, assessments)
    return student 

print(get_inf())







