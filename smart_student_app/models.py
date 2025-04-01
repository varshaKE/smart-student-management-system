from django.db import models

# Create your models here.

class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    usertype=models.CharField(max_length=100)
    

class Department(models.Model):
    dept_name = models.CharField(max_length=150)

class Teacher(models.Model):
    login=models.ForeignKey(Login,on_delete=models.CASCADE)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    dob=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)


class Parent(models.Model):
    login=models.ForeignKey(Login,on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    phone_no = models.CharField(max_length=150)
    email = models.CharField(max_length=150)

class Course(models.Model):
    course_name = models.CharField(max_length=150)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)

class Student(models.Model):
    login = models.ForeignKey(Login, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    relation = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    gender = models.CharField(max_length=150)
    dob = models.CharField(max_length=150)
    phone_no = models.CharField(max_length=150)
    religion = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    qualification = models.CharField(max_length=150)
    aadhaar_no = models.CharField(max_length=150)

class Semester(models.Model):
    sem = models.CharField(max_length=150)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Subject(models.Model):
    subject_name = models.CharField(max_length=150)
    sem = models.ForeignKey(Semester, on_delete=models.CASCADE)

class Complaint(models.Model):
    login = models.ForeignKey(Login, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=150)
    reply = models.CharField(max_length=150)
    date = models.CharField(max_length=150)

class Announcement(models.Model):
    announcement = models.CharField(max_length=150)
    date = models.CharField(max_length=150)


class AssignTeacher(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.CharField(max_length=150)

class Assignments(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    assignment = models.CharField(max_length=150)
    due_date = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    date = models.CharField(max_length=150)
    
class UploadAssignments(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignments, on_delete=models.CASCADE)
    file = models.FileField()
    grade = models.CharField(max_length=150)
    date = models.CharField(max_length=150)
    status = models.CharField(max_length=150)
    marks = models.CharField(max_length=150)
    
    
class InternalMarks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.CharField(max_length=150)
    date = models.CharField(max_length=150)
    status = models.CharField(max_length=150)


class newAttandacess(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    at_date = models.CharField(max_length=150)
    at_status = models.CharField(max_length=150)
    
# class Attendance(models.Model):
#     month = models.CharField(max_length=10)  # e.g., "March"
#     year = models.IntegerField()  # e.g., 2024
#     weekday_count = models.IntegerField(default=0)  # Count of weekdays

#     def __str__(self):
#         return f"{self.month} {self.year}: {self.total_weekdays} days"
    
